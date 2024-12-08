from datetime import datetime
from typing import List

from sync.domain.contants import DATE_FORMAT
from sync.domain.doc_detail import DocDetail
from sync.service.yuque_service import get_yuque_doc, get_yuque_repo, get_yuque_book_toc


def get_yuque_published_docs(include_books: List[str]) -> dict:
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
        # 不在筛选知识库中
        if include_books and not include_books.__contains__(book_name):
            continue
        # 私密的知识库
        if book['public'] == 0:
            continue
        # 获取目录
        doc_contents = get_yuque_book_toc(book_id)
        for doc in doc_contents:
            if doc['type'] == 'META':
                continue
            leaf = not doc['child_uuid']
            title = doc['title']
            uuid = doc['uuid']
            parent_uuid = doc['parent_uuid']
            tags: List[str] = []
            doc_detail = DocDetail()
            if parent_uuid:
                # 有父级节点
                parent = content_dict[parent_uuid]
                tags += parent['tags']
            if not leaf:
                # 不是叶子节点
                tags.append(title)
                content_dict.update({uuid: {'title': title, 'tags': tags, 'leaf': leaf}})
                doc_detail.leaf = False
            if doc['type'] == 'DOC':
                # 所有文档结点，对象包装
                doc_id = doc['doc_id']
                doc_detail.doc_id = doc_id
                doc_detail.book_id = book_id
                doc_detail.title = title
                doc_detail.tags = tags
                doc_dict.update({doc_id: doc_detail})
                print('add doc: doc_id={doc_id}'.format(doc_id=doc_id))

        # 遍历结果字典
        copy_doc_dict = doc_dict.copy()
        for doc_detail in copy_doc_dict.values():
            doc_info = get_yuque_doc(doc_detail.book_id, doc_detail.doc_id)
            # 如果文档未发布，则移除
            if (doc_info['published_at'] is None or doc_info['updated_at'] is None
                    or doc_info['public'] == 0 or doc_info['status'] == 0):
                # public	公开性(0:私密, 1:公开, 2:企业内公开)
                # status	状态(0:草稿, 1:发布)
                doc_dict.pop(doc_info['id'])
            doc_content = doc_info['body']
            doc_detail.content = doc_content
            print(
                '{title} get_yuque_doc: book_id={book_id}, doc_id={doc_id}, doc_content size={doc_content_size}'.format(
                    title=doc_detail.title, book_id=doc_detail.book_id, doc_id=doc_detail.doc_id,
                    doc_content_size=len(doc_content)))
            # 获取更新时间
            update_time_str = str(doc_info['updated_at']).replace('-', '')
            update_time_str = update_time_str[:update_time_str.find('.')]
            print('the update time of {title} is: {update_time_str}'.format(title=doc_detail.title,
                                                                            update_time_str=update_time_str))
            doc_detail.update_time = datetime.strptime(update_time_str, DATE_FORMAT)
    print('get_yuque_published_docs: ', len(doc_dict))
    return doc_dict
