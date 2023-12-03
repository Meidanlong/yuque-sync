import os

import requests
import json

# yuque_access_token = os.environ.get('yuque_access_token')


yuque_access_token = '8RJsszjXfqrpxbsCW8RqmgtEQsfmeiNuyPZAKME1'

def request_repo():
    # 知识库列表
    books_url = 'https://www.yuque.com/api/v2/groups/meidanlong/repos'
    params = {'offset': 0, 'limit': 100, 'type': 'Book'}
    headers = {'accept': 'application/json', 'X-Auth-Token': yuque_access_token}
    return request_yuque(books_url, headers, params)


def request_book_docs(book_id: int):
    # 获取知识库目录详情
    book_doc_url = 'https://www.yuque.com/api/v2/repos/{}/docs'.format(book_id)
    params = {'offset': 0, 'limit': 100}
    headers = {'accept': 'application/json', 'X-Auth-Token': yuque_access_token}
    return request_yuque(book_doc_url, headers, params)


def request_yuque(url: str, headers: {}, params: {}):
    res = requests.get(url=url, headers=headers, params=params)
    return json.loads(res.text)['data']
