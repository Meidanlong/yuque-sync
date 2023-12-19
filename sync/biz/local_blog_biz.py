import os

import yaml

from sync.domain.doc_detail import DocDetail
from sync.service.cnblog_service import new_cnblog_post, update_cnblog_post
from sync.service.github_service import push_github_origin
from sync.service.yuque_service import get_yuque_doc

overview_tag = '---'

overview_format = '''\
---
{overview_yml}
---
{blog_content}
'''


def get_content_posts_path():
    return os.path.abspath(
        os.path.join(os.path.join(os.path.dirname(__file__), os.path.pardir), os.path.pardir, 'content/posts'))


def get_blog_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as md_file:
        return md_file.read()


def get_blog_detail(file_content: str) -> DocDetail:
    index_one = file_content.find(overview_tag)
    index_two = file_content[index_one + len(overview_tag):].find(overview_tag) + len(overview_tag)
    overview = file_content[index_one + len(overview_tag):index_two]
    blog_overview = yaml.load(overview, Loader=yaml.FullLoader)
    doc_detail = DocDetail()
    try:
        doc_detail.doc_id = blog_overview['doc_id']
        doc_detail.title = blog_overview['title']
        doc_detail.tags = blog_overview['tags']
        doc_detail.update_time = blog_overview['update_time']
        doc_detail.cnblog_id = blog_overview['cnblog_id']
    except KeyError as e:
        print(e)
    return doc_detail


def remove_blog_and_file(path: str):
    # 如果递归“content”目录则直接跳出
    if path == get_content_posts_path():
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
    # 1、获取文章详情
    doc_content = get_yuque_doc(doc_detail.book_id, doc_detail.doc_id)
    cnblog_id = doc_detail.cnblog_id
    if cnblog_id is not None:
        # 更新博客园
        update_cnblog_post(cnblog_id, doc_detail.title, doc_content, doc_detail.tags)
    else:
        # 插入博客园，获取博客园id
        cnblog_id = new_cnblog_post(doc_detail.title, doc_content, doc_detail.tags)
    doc_detail.cnblog_id = cnblog_id
    # 2、拼装文章顶部预览
    overview_yml = del_yml_useless_line(yaml.dump(data=doc_detail, allow_unicode=True))
    all_blog_content = overview_format.format(overview_yml=overview_yml, blog_content=doc_content)
    # 3、生成本地博客文件
    content_path = get_content_posts_path()
    file_name = doc_detail.title + '.md'
    relative_directory = '/'.join(doc_detail.tags)
    relative_path = os.path.join(relative_directory, file_name)
    file_directory = os.path.join(content_path, relative_directory)
    file_path = os.path.join(file_directory, file_name)
    # 检查目录是否存在，不存在则创建
    if not os.path.exists(file_directory):
        os.makedirs(file_directory)
    # 在指定目录创建文件，并写入内容
    with open(file_path, 'w') as file:
        file.write(all_blog_content)
        # 4、同步github
        commit_log = 'push remote'
        push_github_origin(relative_path, all_blog_content, commit_log)
