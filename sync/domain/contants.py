import os

# 日期格式化
DATE_FORMAT = '%Y%m%dT%H:%M:%S'
# 排除文件
EXCLUDE_FILES = ['.DS_Store']
# 系统分割符
OS_SEP = os.sep
# 本地文件保存目录（相对于项目根目录）
TARGET_DIR = os.path.join('docs')

# 请求
GET_REPO_LIST_URL = 'https://www.yuque.com/api/v2/users/{login}/repos'
GET_BOOK_TOC_URL = 'https://www.yuque.com/api/v2/repos/{book_id}/toc'
GET_BOOK_LIST_URL = 'https://www.yuque.com/api/v2/repos/{book_id}/docs'
GET_DOC_DETAIL_URL = 'https://www.yuque.com/api/v2/repos/{book_id}/docs/{id}'
GET_USR_URL = 'https://www.yuque.com/api/v2/user'

# 语雀环境
YUQUE_LOGIN = 'meidanlong'
INCLUDE_BOOKS = ['博客专栏']


# 密钥
def get_yuque_access_token():
    return os.getenv('YUQUE_ACCESS_TOKEN')
