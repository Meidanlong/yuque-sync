import os

import requests
import json

from sync.domain.constant.contants import GET_REPO_LIST_URL, GET_BOOK_LIST_URL, GET_DOC_DETAIL_URL
from sync.domain.constant.private_data import YUQUE_LOGIN, YUQUE_ACCESS_TOKEN


def get_yuque_repo():
    # 知识库列表
    url = GET_REPO_LIST_URL.format(login=YUQUE_LOGIN)
    params = {'offset': 0, 'limit': 100, 'type': 'Book'}
    return request_yuque(url, params)


def get_yuque_book(book_id: int):
    # 获取知识库目录详情
    url = GET_BOOK_LIST_URL.format(book_id=book_id)
    params = {'offset': 0, 'limit': 100}
    return request_yuque(url, params)


def get_yuque_doc(book_id: int, doc_id: str):
    url = GET_DOC_DETAIL_URL.format(book_id=book_id, id=doc_id, format='markdown')
    return request_yuque(url, None)['body']


def request_yuque(url: str, params: {}):
    headers = {'accept': 'application/json', 'X-Auth-Token': YUQUE_ACCESS_TOKEN}
    res = requests.get(url=url, headers=headers, params=params)
    return json.loads(res.text)['data']
