from datetime import datetime
from typing import List

import requests
import json
import yaml
import os

yuque_access_token = os.environ.get('yuque_access_token')
# yuque_access_token = '8RJsszjXfqrpxbsCW8RqmgtEQsfmeiNuyPZAKME1'

project_path = os.path.abspath(os.path.dirname(__file__))

print(project_path)




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
    books_url = 'https://www.yuque.com/api/v2/groups/meidanlong/repos'
    params = {'offset': 0, 'limit': 100, 'type': 'Book'}
    headers = {'accept': 'application/json', 'X-Auth-Token': yuque_access_token}
    res = requests.get(url=books_url, headers=headers, params=params)
    for book in json.loads(res.text)['data']:
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
        book_doc_url = 'https://www.yuque.com/api/v2/repos/{}/docs'.format(book['id'])
        params = {'offset': 0, 'limit': 100}
        headers = {'accept': 'application/json', 'X-Auth-Token': yuque_access_token}
        res = requests.get(url=book_doc_url, headers=headers, params=params)
        for doc in json.loads(res.text)['data']:
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
print('执行成功: {}'.format(len(doc_dict)))
# 2、比对上次留存的文档目录，分别区分新增、更新和删除。将新文档目录文件替换原文件

# 3、遍历文档目录，创建不存在的目录

# 4、新增、更新和删除文件，并同步到云平台

# 5、发布本地博客代码，更新个人博客









