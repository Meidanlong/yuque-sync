from datetime import datetime


class YuqueBlog:
    id: str # 语雀文档id
    book_id: str # 知识库id
    title: str
    tags: []
    uri: str
    slug: str
    update_time: datetime

    def __init__(self, doc_id, title, tags, uri):
        self.doc_id = doc_id
        self.title = title
        self.tags = tags
        self.uri = uri
