import json
import xmlrpc.client
import time
from datetime import datetime

from sync.domain.constant.contants import DATE_FORMAT
from sync.domain.constant.private_data import CNBLOG_METAWEBLOG_API, CNBLOG_USERNAME, CNBLOG_TOKEN

DEFAULT_RECENT_BLOG_COUNT = 1000


def get_cnblog_recent_post() -> {}:
    client = xmlrpc.client.ServerProxy(CNBLOG_METAWEBLOG_API)
    cnblog_details = client.metaWeblog.getRecentPosts(CNBLOG_USERNAME, CNBLOG_USERNAME, CNBLOG_TOKEN,
                                                      DEFAULT_RECENT_BLOG_COUNT)
    print('读取博客，篇数：%d' % len(cnblog_details))
    cnblog_map = {}
    for cnblog in cnblog_details:
        xml_rpc_time = cnblog['dateCreated']
        cnblog['dateCreated'] = datetime.strptime(xml_rpc_time.value, DATE_FORMAT)  # string
        tags = str(cnblog['mt_keywords']).replace(',', '/')
        cnblog_map.update({tags+"@"+cnblog['title']: cnblog})

    print(json.dumps(cnblog_map, default=str))

    return cnblog_map


def new_cnblog_post(title, content, category, keywords):
    # 构建发布内容
    struct = {
        'title': title,
        'dateCreated': 0,
        'description': content,
    }
    if category is not None:
        struct['categories'] = ['[Markdown]', category]
    else:
        struct['categories'] = ['[Markdown]']

    if keywords is not None:
        struct['mt_keywords'] = keywords

    client = xmlrpc.client.ServerProxy(CNBLOG_METAWEBLOG_API)
    post_id = client.metaWeblog.newPost('', CNBLOG_USERNAME, CNBLOG_TOKEN, struct, True)
    print('发布成功' + post_id)
    time.sleep(20)  # 博客园每分钟不能发布超过3篇




if __name__ == '__main__':
    get_cnblog_recent_post()
    # new_post('title14', '# Content2', 'cate1', 'linux,gpu,cuda')
