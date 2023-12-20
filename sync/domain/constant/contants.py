import os

# 日期格式化
DATE_FORMAT = '%Y%m%dT%H:%M:%S'

GET_REPO_LIST_URL = 'https://www.yuque.com/api/v2/users/{login}/repos'
GET_BOOK_LIST_URL = 'https://www.yuque.com/api/v2/repos/{book_id}/docs'
GET_DOC_DETAIL_URL = 'https://www.yuque.com/api/v2/repos/{book_id}/docs/{id}'
GET_USR_URL = 'https://www.yuque.com/api/v2/user'

EXCLUDE_FILES = ['.DS_Store']

TARGET_DIR = os.path.join('content', 'posts')
OS_SEP = os.sep
