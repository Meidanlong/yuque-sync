from sync.biz.sync_docs_biz import get_published_docs, compare_and_update_docs
from sync.domain.constant.private_data import EXCLUDE_BOOKS

doc_dict = get_published_docs(exclude_books=EXCLUDE_BOOKS)
compare_and_update_docs(doc_dict)
