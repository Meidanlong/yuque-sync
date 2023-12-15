from datetime import datetime


class DocDetail:
    doc_id: str
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


class DocOverview:
    doc_id: str
    title: str
    tags: []
    date: datetime
    draft = False

    def __init__(self, docDetail: DocDetail):
        self.doc_id = docDetail.doc_id
        self.title = docDetail.title
        self.tags = docDetail.tags
        self.date = docDetail.update_time