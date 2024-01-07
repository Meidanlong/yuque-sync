from sync.biz.local_blog_biz import local_push_pages
from sync.biz.sync_docs_biz import compare_and_update_docs
from sync.biz.yuque_blog_biz import get_yuque_published_docs
from sync.domain.constant.private_data import EXCLUDE_BOOKS


def yuque_sync():
    compare_and_update_docs(get_yuque_published_docs(exclude_books=EXCLUDE_BOOKS))


def push_pages():
    local_push_pages()
