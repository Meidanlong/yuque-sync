import os
from datetime import datetime
from typing import List

import yaml

from sync.requst_api import request_repo, request_book_docs


def get_content_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'content'))




class DocDetail():
    doc_id: str
    title: str
    tags: []
    uri: str
    slug: str
    update_time: datetime
    type: str
    def __init__(self, doc_id, title, tags, uri):
        self.doc_id=doc_id
        self.title=title
        self.tags=tags
        self.uri=uri


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
                doc_dict.update({doc['doc_id']: DocDetail(doc_id=doc['doc_id'], title=title, tags=tags, uri=location_uri)})

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
            doc_detail.update_time = doc['updated_at']

    return doc_dict


# 1、获取公开的已发布的文档，及文档所归属的目录（标签）
doc_dict = get_published_docs(['知识脉络'])
print('执行成功: {}'.format([doc for doc in doc_dict.keys()]))
# 2、直接与本地项目content下目录进行对比，分别区分新增、更新和删除。将新文档目录文件替换原文件
content_path = get_content_path()
for doc_detail in doc_dict.values():
    tags = doc_detail.tags
    # 获取文章路径
    doc_path = content_path
    for tag in tags:
        doc_path = os.path.join(doc_path, tag)
    doc_path = os.path.join(doc_path, doc_detail.title)
    print(doc_path)
    # 判断文章是否存在
    if not os.path.exists(doc_path):
        # 如果文章不存在，则获取文章详情并创建文章
        # 问题，如何判断删除的文章？
        pass

# 3、遍历文档目录，创建不存在的目录

# 4、新增、更新和删除文件，并同步到云平台

# 5、发布本地博客代码，更新个人博客









