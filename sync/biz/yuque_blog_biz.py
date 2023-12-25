from datetime import datetime
from typing import List

import yaml

from sync.domain.constant.contants import DATE_FORMAT
from sync.domain.doc_detail import DocDetail
from sync.service.yuque_service import get_yuque_doc, get_yuque_book, get_yuque_repo


def get_yuque_published_docs(exclude_books: List[str]) -> dict:
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
                doc_id = doc['doc_id']
                doc_detail = DocDetail()
                doc_detail.doc_id = doc_id
                doc_detail.book_id = book_id
                doc_detail.title = title
                doc_detail.tags = tags
                doc_dict.update({doc_id: doc_detail})
                print('add doc: doc_id={doc_id}'.format(doc_id=doc_id))

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
                print('pop doc: doc_id={doc_id}'.format(doc_id=doc_id))
                continue

            doc_detail = doc_dict[doc_id]
            # 记录文档详情
            # 获取博客内容
            doc_content = get_yuque_doc(book_id, doc_id)
            print('get_yuque_doc: book_id={book_id}, doc_id={doc_id}'.format(book_id=book_id, doc_id=doc_id))
            doc_detail.content = doc_content
            # 获取更新时间
            update_time_str = str(doc['updated_at']).replace('-', '')
            update_time_str = update_time_str[:update_time_str.find('.')]
            print('the update time of {title} is: {update_time_str}'.format(title=doc_detail.title, update_time_str=update_time_str))
            doc_detail.update_time = datetime.strptime(update_time_str, DATE_FORMAT)
            doc_dict.update({doc_id: doc_detail})
    print('get_yuque_published_docs: ', len(doc_dict))
    return doc_dict
