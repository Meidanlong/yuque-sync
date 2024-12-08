import json

import requests

from sync.domain.contants import GET_REPO_LIST_URL, GET_BOOK_LIST_URL, GET_DOC_DETAIL_URL, GET_USR_URL, \
    GET_BOOK_TOC_URL, get_yuque_access_token


def get_yuque_repo():
    # 知识库列表
    url = GET_REPO_LIST_URL.format(login=get_yuque_user()['login'])
    params = {'offset': 0, 'limit': 100, 'type': 'Book'}
    return request_yuque(url, params)


def get_yuque_book(book_id: int):
    # 获取知识库目录详情
    url = GET_BOOK_LIST_URL.format(book_id=book_id)
    params = {'offset': 0, 'limit': 100}
    return request_yuque(url, params)


def get_yuque_book_toc(book_id: int):
    url = GET_BOOK_TOC_URL.format(book_id=book_id)
    return request_yuque(url, None)


def get_yuque_doc(book_id: int, doc_id: str):
    url = GET_DOC_DETAIL_URL.format(book_id=book_id, id=doc_id, format='markdown')
    return request_yuque(url, None)


def get_yuque_user():
    return request_yuque(GET_USR_URL, None)


def request_yuque(url: str, params: {}):
    headers = {'accept': 'application/json', 'X-Auth-Token': get_yuque_access_token()}
    res = requests.get(url=url, headers=headers, params=params)
    return json.loads(res.text)['data']
