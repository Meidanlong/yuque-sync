import xmlrpc.client
from datetime import datetime

from sync.domain.constant.contants import DATE_FORMAT, OS_SEP, CNBLOG_TOKEN
from sync.domain.constant.private_data import CNBLOG_METAWEBLOG_API, CNBLOG_USERNAME
from sync.domain.doc_detail import DocDetail

DEFAULT_RECENT_BLOG_COUNT = 1000


def get_cnblog_recent_post() -> {}:
    cnblog_details = get_cnblog_client().metaWeblog.getRecentPosts(CNBLOG_USERNAME, CNBLOG_USERNAME, CNBLOG_TOKEN,
                                                                   DEFAULT_RECENT_BLOG_COUNT)
    print('读取博客，篇数：%d' % len(cnblog_details))
    cnblog_map = {}
    for cnblog in cnblog_details:
        xml_rpc_time = cnblog['dateCreated']
        cnblog['dateCreated'] = datetime.strptime(xml_rpc_time.value, DATE_FORMAT)  # string
        tags = str(cnblog['mt_keywords']).replace(',', OS_SEP)
        cnblog_map.update({tags + "@" + cnblog['title']: cnblog})
    return cnblog_map


def new_cnblog_post(title, content, tags: []):
    # 构建发布内容
    struct = {
        'title': title,
        'dateCreated': 0,
        'description': content,
    }
    if tags is not None:
        # 切换操作系统会造成混乱
        struct['categories'] = ['[Markdown]', OS_SEP.join(tags)]
        struct['mt_keywords'] = ','.join(tags)
    else:
        struct['categories'] = ['[Markdown]']

    post_id = get_cnblog_client().metaWeblog.newPost('', CNBLOG_USERNAME, CNBLOG_TOKEN, struct, True)
    print(f'{title}发布成功 -> {post_id}'.format(title=title, post_id=post_id))
    return post_id


def update_cnblog_post(post_id, title, content, tags: []):
    # 构建发布内容
    struct = {
        'title': title,
        'dateCreated': 0,
        'description': content,
    }
    if tags is not None:
        struct['categories'] = ['[Markdown]', OS_SEP.join(tags)]
        struct['mt_keywords'] = ','.join(tags)
    else:
        struct['categories'] = ['[Markdown]']

    post_id = get_cnblog_client().metaWeblog.editPost(post_id, CNBLOG_USERNAME, CNBLOG_TOKEN, struct, True)
    print(f'{title}更新成功 -> {post_id}'.format(title=title, post_id=post_id))


def delete_cnblog_post(cnblog_id: int):
    return get_cnblog_client().blogger.deletePost('', str(cnblog_id), CNBLOG_USERNAME, CNBLOG_TOKEN, True) > 0


def get_cnblog_client():
    client = xmlrpc.client.ServerProxy(CNBLOG_METAWEBLOG_API)
    return client


def get_cnblog_key(doc_detail: DocDetail):
    cnblog_map_key: str
    if doc_detail.tags is not None:
        # 博客园对keyword进行了排序
        cnblog_map_key = OS_SEP.join(sorted(doc_detail.tags))
    cnblog_map_key += '@' + doc_detail.title
