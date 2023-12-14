import os

import yaml

from sync.get_yuque_docs import DocDetail

overview_tag = '---'


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
        os.remove(path)
    elif os.path.isdir(path):
        # 目录：如果目录为空（下面无文件），则删除该目录
        if not os.listdir(path):
            os.rmdir(path)
        else:
            return
    # 递归调用
    remove_blog_and_file(os.path.abspath(os.path.join(path, '..')))


def generate_blog(doc_detail: DocDetail):
    pass
