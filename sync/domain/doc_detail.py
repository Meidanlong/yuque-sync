from datetime import datetime


class DocDetail:
    doc_id: str = None
    book_id: int = None
    # 应包含博客园文章标识
    cnblog_id: int = None
    title: str = None
    tags: [] = None
    # uri: str = None
    # slug: str = None
    update_time: datetime = None
    draft = False
