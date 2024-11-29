from sync.biz.sync_docs_biz import compare_and_update_docs
from sync.biz.yuque_blog_biz import get_yuque_published_docs
from sync.domain.constant.private_data import INCLUDE_BOOKS


def yuque_sync():
    yuque_docs = get_yuque_published_docs(include_books=INCLUDE_BOOKS)
    compare_and_update_docs(yuque_docs)


if __name__ == '__main__':
    yuque_sync()
