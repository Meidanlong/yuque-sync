import os
from datetime import datetime
from typing import List

import yaml

from sync.blog_editor import get_content_path
from sync.domain.constant.contants import DATE_FORMAT
from sync.doc_pojo import DocDetail
from sync.requst_api import request_repo, request_book_docs



def get_published_docs(exclude_books: List[str]) -> dict:
    # 目录字典 用于记录目录层级
    content_dict = {}
    # 文档字典
    doc_dict = {}

    # 获取知识库及子目录层级
    # 知识库列表
    books = request_repo()
    for book in books:
        # 排除知识库
        if exclude_books.__contains__(book['name']):
            continue
        # 私密的知识库
        if book['public'] == 0:
            continue
        # 获取目录
        doc_contents = yaml.load(book['toc_yml'], Loader=yaml.FullLoader)
        for doc in doc_contents:
            if doc['type'] == 'META':
                continue
            leaf = not doc['child_uuid']
            title = doc['title']
            uuid = doc['uuid']
            parent_uuid = doc['parent_uuid']
            tags: List[str] = []
            if parent_uuid:
                parent = content_dict[parent_uuid]
                tags += parent['tags']
            if not leaf:
                tags.append(title)
                content_dict.update({uuid: {'title': title, 'tags': tags, 'leaf': leaf}})
            else:
                location_uri = ''
                for tag in tags:
                    location_uri += "{}/".format(tag)
                # doc_dict.update({doc['doc_id']: {'title': title, 'tags': tags, 'uri': location_uri}})
                doc_dict.update(
                    {doc['doc_id']: DocDetail(doc_id=doc['doc_id'], title=title, tags=tags, uri=location_uri)})

        # 获取知识库目录详情
        docs = request_book_docs(book['id'])
        for doc in docs:
            # 如果文档不在doc_dict中记录（可能不是叶子节点），则跳过
            doc_id = doc['id']
            if not doc_dict.__contains__(doc_id):
                continue
            # 如果文档未发布，则移除
            if not doc['published_at']:
                doc_dict.pop(doc_id)
                continue

            doc_detail = doc_dict[doc_id]
            # 记录文档详情
            doc_detail.slug = doc['slug']
            update_time_str = str(doc['updated_at']).replace('-', '')
            update_time_str = update_time_str[:update_time_str.find('.')]
            doc_detail.update_time = datetime.strptime(update_time_str, DATE_FORMAT)

    return doc_dict


# 1、获取公开的已发布的文档，及文档所归属的目录（标签）
doc_dict = get_published_docs(exclude_books=['知识脉络'])
print('执行成功: {}'.format([doc for doc in doc_dict.keys()]))
# 2、本地项目content下目录与语雀目录进行对比，分别区分删除和更新。
content_path = get_content_path()

for doc_detail in doc_dict.values():
    tags = doc_detail.tags
    # 获取文章路径
    doc_path = content_path
    for tag in tags:
        doc_path = os.path.join(doc_path, tag)
    doc_path = os.path.join(doc_path, doc_detail.title)
    # print(doc_path)
    # 判断文章是否存在
    if not os.path.exists(doc_path):
        # 如果文章不存在，则获取文章详情并创建文章
        # 问题，如何判断删除的文章？
        pass

# 3、遍历文档目录，创建不存在的目录

# 4、新增、更新和删除文件，并同步到云平台

# 5、发布本地博客代码，更新个人博客


if __name__ == "__main__":
    doc_dict = get_published_docs(exclude_books=['知识脉络'])
    content_path = get_content_path()

    insert_blogs: List[DocDetail] = []
    update_blogs: List[DocDetail] = []
    delete_blogs = []
    for root, dirs, files in os.walk(content_path):
        for file in files:
            if file == '.DS_Store':
                continue
            # 获取文件路径
            file_path = os.path.join(root, file)
            # 获取博客内容
            blog_content = get_blog_content(file_path)
            # 获取博客概览
            blog_overview = get_blog_overview(blog_content)
            if blog_overview:
                # 如果本地博客概览存在，则执行的操纵为删除或更新
                try:
                    # 获取博客概览信息
                    # 如果本地博客不存在doc_id，或者语雀文档不包含该doc_id，则删除该文件
                    doc_id_ = blog_overview['doc_id']
                    yuque_blog_overview: DocDetail = doc_dict.get(doc_id_)
                    if not yuque_blog_overview:
                        delete_blogs.append(blog_overview)
                        raise KeyError('yuque blog removed')
                    # 比对时间戳，如果语雀的时间戳更新，则同样删除该文件，并记录在insert_blogs，等待后续重新创建
                    blog_time = blog_overview['date']
                    yuque_time = yuque_blog_overview.update_time
                    if yuque_time > blog_time:
                        update_blogs.append(yuque_blog_overview)
                        raise KeyError('yuque blog updated')
                    else:
                        insert_blogs.append(yuque_blog_overview)
                except KeyError as e:
                    remove_blog_and_file(file_path)
                    # pass
            else:
                # 如果本地博客概览不存在，则表明不是所维护的博客，根据业务定义直接删除
                remove_blog_and_file(file_path)

    # 插入语雀博客
    for doc_detail in insert_blogs:
        print('插入博客：', doc_detail.title)
        all_blog_content = generate_blog(doc_detail)
        print(all_blog_content)

    # 插入语雀博客
    for doc_detail in update_blogs:
        print('更新博客：', doc_detail.title)
        all_blog_content = generate_blog(doc_detail)
        print(all_blog_content)

    # 插入语雀博客
    for doc_detail in delete_blogs:
        print('删除博客：', doc_detail['title'])
