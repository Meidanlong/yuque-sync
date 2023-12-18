from datetime import datetime


class DocDetail:
    doc_id: str
    book_id: int
    # 应包含博客园文章标识
    cnblog_id: int
    title: str
    tags: []
    # uri: str
    # slug: str
    update_time: datetime
    draft = False


class DocOverview:
    doc_id: str
    book_id: int
    title: str
    tags: []
    date: datetime
    draft = False
    # 应包含博客园文章标识
    cnblog_id: int

    def __init__(self, doc_detail: DocDetail):
        self.doc_id = doc_detail.doc_id
        self.book_id = doc_detail.book_id
        self.title = doc_detail.title
        self.tags = doc_detail.tags
        self.date = doc_detail.update_time