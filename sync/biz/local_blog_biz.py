import os

import yaml

from sync.domain.doc_pojo import DocDetail, DocOverview
from sync.service.yuque_service import get_yuque_doc

overview_tag = '---'

overview_format = '''\
---
{overview_yml}
---
{blog_content}
'''


def get_content_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'content'))


def get_blog_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as md_file:
        return md_file.read()


def get_blog_overview(file_content: str):
    index_one = file_content.find(overview_tag)
    index_two = file_content[index_one + len(overview_tag):].find(overview_tag) + len(overview_tag)
    overview = file_content[index_one + len(overview_tag):index_two]
    return yaml.load(overview, Loader=yaml.FullLoader)


def remove_blog_and_file(path: str):
    # 如果递归“content”目录则直接跳出
    if path == get_content_path():
        return
    # 文件或目录不存在，则直接返回
    if not os.path.exists(path):
        return
    # 判断路径是文件还是目录
    if os.path.isfile(path):
        # 文件：如果文件存在，则删除
        print('remove file:', path)
        os.remove(path)
    elif os.path.isdir(path):
        # 目录：如果目录为空（下面无文件），则删除该目录
        if not os.listdir(path):
            print('remove dir:', path)
            os.rmdir(path)
        else:
            return
    # 递归调用
    remove_blog_and_file(os.path.abspath(os.path.join(path, '..')))


def del_yml_useless_line(s):
    s = s.split('\n', 1)[-1]
    if s.find('\n') == -1:
        return ''
    return s.rsplit('\n', 1)[0]


def generate_blog(doc_detail: DocDetail) -> str:
    doc_overview = DocOverview(doc_detail)
    # 1、获取文章顶部预览
    overview_yml = del_yml_useless_line(yaml.dump(data=doc_overview, allow_unicode=True))
    # 2、获取文章详情
    doc_content = get_yuque_doc(doc_detail.book_id, doc_detail.doc_id)
    all_blog_content = overview_format.format(overview_yml=overview_yml, blog_content='这是一篇博客。')
    return all_blog_content
