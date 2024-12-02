# 密钥
import os

# 语雀环境
YUQUE_LOGIN = 'meidanlong'
INCLUDE_BOOKS = ['博客专栏']


# 密钥
def get_yuque_access_token():
    return os.getenv('YUQUE_ACCESS_TOKEN')
