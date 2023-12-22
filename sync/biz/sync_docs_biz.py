import os
from datetime import datetime
from typing import List, Dict

import yaml

from sync.biz.local_blog_biz import get_content_posts_path, get_blog_content, get_blog_detail, remove_blog_and_file, \
    generate_blog
from sync.domain.constant.contants import DATE_FORMAT
from sync.domain.doc_detail import DocDetail
from sync.service.cnblog_service import get_cnblog_recent_post, delete_cnblog_post
from sync.service.yuque_service import get_yuque_book, get_yuque_repo


def get_published_docs(exclude_books: List[str]) -> dict:
    # 目录字典 用于记录目录层级
    content_dict = {}
    # 文档字典
    doc_dict = {}

    # 获取知识库及子目录层级
    # 知识库列表
    books = get_yuque_repo()
    for book in books:
        book_id = book['id']
        book_name = book['name']
        # 排除知识库
        if exclude_books.__contains__(book_name):
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
                # 有父级节点
                parent = content_dict[parent_uuid]
                tags += parent['tags']
            else:
                # 如果该元素没有父级元素，则在tag添加知识库名称
                tags.append(book_name)
            if not leaf:
                # 不是叶子节点
                tags.append(title)
                content_dict.update({uuid: {'title': title, 'tags': tags, 'leaf': leaf}})
            else:
                # 叶子结点，对象包装
                doc_detail = DocDetail()
                doc_detail.doc_id = doc['doc_id']
                doc_detail.book_id = book_id
                doc_detail.title = title
                doc_detail.tags = tags
                doc_dict.update({doc['doc_id']: doc_detail})
                print('doc_dict add', doc['doc_id'])

        # 获取知识库目录详情
        docs = get_yuque_book(book_id)
        for doc in docs:
            # 如果文档不在doc_dict中记录（可能不是叶子节点），则跳过
            doc_id = doc['id']
            if not doc_dict.__contains__(doc_id):
                continue
            # 如果文档未发布，则移除
            if (doc['published_at'] is None or doc['updated_at'] is None
                    or doc['public'] == 0 or doc['status'] == 0):
                # public	公开性(0:私密, 1:公开, 2:企业内公开)
                # status	状态(0:草稿, 1:发布)
                doc_dict.pop(doc_id)
                print('doc_dict pop', doc_id)
                continue

            doc_detail = doc_dict[doc_id]
            # 记录文档详情
            update_time_str = str(doc['updated_at']).replace('-', '')
            update_time_str = update_time_str[:update_time_str.find('.')]
            print('{} updated at : {}'.format(doc_id, update_time_str))
            doc_detail.update_time = datetime.strptime(update_time_str, DATE_FORMAT)

    return doc_dict


def compare_and_update_docs(yuque_doc_dict: Dict[int, DocDetail]):
    # 1、本地项目content下目录与语雀目录进行对比，分别区分删除和更新。
    content_path = get_content_posts_path()
    # 2、遍历文档目录，查找存在差异的博客
    insert_blogs: List[DocDetail] = list(yuque_doc_dict.values())
    update_blogs: List[DocDetail] = []
    delete_blogs: List[DocDetail] = []
    # 3、获取全部博客园的博客列表
    cnblog_map = get_cnblog_recent_post()
    for root, dirs, files in os.walk(content_path):
        for file in files:
            if file == '.DS_Store':
                continue
            # 获取文件路径
            local_file_path = os.path.join(root, file)
            # 获取博客内容
            local_doc_content = get_blog_content(local_file_path)
            # 获取博客概览
            local_doc_detail = get_blog_detail(local_doc_content)
            if local_doc_detail:
                # 如果本地博客概览存在，则执行的操纵为删除或更新
                try:
                    # 如果本地博客不存在doc_id，或者语雀文档不包含该doc_id，则删除该文件
                    yuque_doc_detail: DocDetail = yuque_doc_dict.get(local_doc_detail.doc_id)
                    # 获取博客园中博客
                    cnblog_remote_detail = get_cnblog_detail(cnblog_map, local_doc_detail)

                    # 1、删除操作
                    if yuque_doc_detail is None:
                        # 博客园中存在该博客，则添加到删除列表等待被删除
                        if cnblog_remote_detail:
                            local_doc_detail.cnblog_id = cnblog_remote_detail['postid']
                        delete_blogs.append(local_doc_detail)
                        raise KeyError('yuque blog removed')
                    # 完善博客园ID
                    yuque_doc_detail.cnblog_id = cnblog_remote_detail['postid']

                    # 2、更新操作
                    # 比对时间戳，如果语雀的时间戳更新，则同样删除该文件，并记录在insert_blogs，等待后续重新创建
                    local_update_time = local_doc_detail.update_time
                    yuque_update_time = yuque_doc_detail.update_time
                    if local_update_time is None or yuque_update_time is None:
                        # 问题数据，直接删除
                        insert_blogs.remove(yuque_doc_detail)
                        raise KeyError('yuque blog updated')
                    if yuque_update_time > local_update_time:
                        insert_blogs.remove(yuque_doc_detail)
                        update_blogs.append(yuque_doc_detail)
                        raise KeyError('yuque blog updated')
                except KeyError as e:
                    print(e)
                    remove_blog_and_file(local_file_path)
            else:
                # 如果本地博客概览不存在，则表明不是所维护的博客，根据业务定义直接删除
                remove_blog_and_file(local_file_path)

    # 3、删除语雀博客
    for doc_detail in delete_blogs:
        print('删除博客：', doc_detail.title)
        delete_cnblog_post(doc_detail.cnblog_id)

    # 4、更新语雀博客
    for doc_detail in update_blogs:
        print('更新博客：', doc_detail.title)
        generate_blog(doc_detail)

    # 5、插入语雀博客
    for doc_detail in insert_blogs:
        print('插入博客：', doc_detail.title)
        generate_blog(doc_detail)


def get_cnblog_detail(cnblog_map, doc_detail):
    tags = doc_detail.tags
    title = doc_detail.title
    cnblog_map_key: str
    if tags is not None:
        # 博客园对keyword进行了排序
        cnblog_map_key = '/'.join(sorted(tags))
    cnblog_map_key += '@' + title
    try:
        cnblog_detail = cnblog_map[cnblog_map_key]
        return cnblog_detail
    except KeyError as e:
        print(e)
        return None
