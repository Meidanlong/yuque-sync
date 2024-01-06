import os
from typing import List, Dict

from sync.biz.local_blog_biz import get_content_posts_path, get_blog_content, get_blog_detail, remove_blog_and_file, \
    update_local_doc, insert_local_doc
from sync.domain.doc_detail import DocDetail
from sync.service.cnblog_service import get_cnblog_recent_post, delete_cnblog_post, get_cnblog_key, new_cnblog_post, \
    update_cnblog_post


def sync_local(yuque_doc_dict: Dict[int, DocDetail]):
    # 1、初始化新插入博客列表
    insert_doc_list: List[DocDetail] = list(yuque_doc_dict.values())
    # 2、本地项目content下目录与语雀目录进行对比，分别区分删除和更新。
    content_path = get_content_posts_path()
    # 3、对比本地存在路径
    for root, dirs, files in os.walk(content_path):
        for file in files:
            if file == '.DS_Store':
                continue
            # 获取文件路径
            local_file_path = os.path.join(root, file)
            # 获取博客概览
            local_doc_detail = get_blog_detail(get_blog_content(local_file_path))
            if local_doc_detail is None:
                # 3.1、本地博客不存在博客信息，则直接删除
                remove_blog_and_file(local_file_path)
                print('sync_local-[local_doc_detail is None]-remove: ', local_file_path)
                continue
            # 本地博客存在博客信息，则获取语雀博客信息
            yuque_doc_detail: DocDetail = yuque_doc_dict.get(local_doc_detail.doc_id)
            if yuque_doc_detail is None:
                # 3.2、如果语雀中不存在该博客，则表明已从语雀中删除，故删除本地文件
                remove_blog_and_file(local_file_path)
                print('sync_local-[yuque_doc_detail is None]-remove: ', local_file_path)
                continue
            # 本地博客存在 且 语雀博客存在
            if yuque_doc_detail.content is None:
                # 3.3、如果语雀文档没有内容则删除博客
                remove_blog_and_file(local_file_path)
                insert_doc_list.remove(yuque_doc_detail)
            local_update_time = local_doc_detail.update_time
            yuque_update_time = yuque_doc_detail.update_time
            if local_update_time is None or yuque_update_time > local_update_time:
                # 3.4、如果本地博客更新时间戳为空 或者 语雀博客更新时间戳大于本地时间戳 则 更新本地博客
                update_local_doc(yuque_doc_detail)
                # 维护
                insert_doc_list.remove(yuque_doc_detail)
                print('sync_local-update: ', local_file_path)
    # 4、插入（本地没有的博客）剩余博客
    for doc_detail in insert_doc_list:
        insert_local_doc(doc_detail)
        print('sync_local-insert: ', doc_detail.title)


def sync_cnblog(yuque_doc_dict: Dict[int, DocDetail]):
    # 1、获取全部博客园的博客列表
    cnblog_map = get_cnblog_recent_post()
    # 2、初始化博客园删除博客列表
    delete_doc_list = list(cnblog_map.values())
    # 3、对比博客园已有博客（反向对比）
    for yuque_doc_detail in yuque_doc_dict.values():
        cnblog_doc = cnblog_map.get(get_cnblog_key(yuque_doc_detail), None)
        if yuque_doc_detail.content is None:
            # 3.1、如果语雀文档没有内容则删除博客
            delete_doc_list.remove(cnblog_doc)
            continue
        if cnblog_doc is None:
            # 3.2、如果博客园不存在该博客，则新增
            new_cnblog_post(yuque_doc_detail.title, yuque_doc_detail.content, yuque_doc_detail.tags)
            print('sync_cnblog-insert: ', yuque_doc_detail.title)
            continue
        cnblog_update_time = cnblog_doc.get('dateCreated', None)
        yuque_update_time = yuque_doc_detail.update_time
        if cnblog_update_time is None or yuque_update_time > cnblog_update_time:
            # 3.3、更新该博客
            update_cnblog_post(cnblog_doc['post_id'], yuque_doc_detail.title, yuque_doc_detail.content,
                               yuque_doc_detail.tags)
            # 维护
            delete_doc_list.remove(cnblog_doc)
            print('sync_cnblog-update: ', yuque_doc_detail.title)
    # 4、语雀中不存在的博客进行删除
    for cnblog_doc in delete_doc_list:
        delete_cnblog_post(cnblog_doc['post_id'])
        print('sync_cnblog-delete: ', cnblog_doc['title'])


def compare_and_update_docs(yuque_doc_dict: Dict[int, DocDetail]):
    sync_local(yuque_doc_dict)
    sync_cnblog(yuque_doc_dict)
