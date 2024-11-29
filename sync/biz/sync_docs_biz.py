import json
import os
from typing import List, Dict

from sync.biz.local_blog_biz import get_content_posts_path, get_file_content, get_blog_detail, remove_blog_and_file, \
    update_local_doc, insert_local_doc
from sync.domain.doc_detail import DocDetail


def compare_and_update_docs(yuque_doc_dict: Dict[int, DocDetail]):
    sync_local_nav_sidebar(yuque_doc_dict)
    sync_local_docs(yuque_doc_dict)

def sync_local_nav_sidebar(yuque_doc_dict: Dict[int, DocDetail]):
    nav_content = format_nav(yuque_doc_dict)
    update_script_file(nav_content, 'nav')
    sidebar_content = format_sidebar(yuque_doc_dict)
    update_script_file(sidebar_content, 'sidebar')


def format_nav(doc_dict):
    result = {}
    for doc in doc_dict.values():
        tags = doc.tags
        title = doc.title

        if len(tags) == 2 and tags[-1] == title:
            category = tags[0]
            if category not in result:
                result[category] = {'text': category, 'items': []}

            result[category]['items'].append({
                'text': title,
                'link': f'/{"/".join(tags)}/{title}'
            })
    nav = list(result.values())
    return f"export default {json.dumps(nav, indent=2, ensure_ascii=False)}"

def format_sidebar(doc_dict):
    sidebar = {}
    for doc in doc_dict.values():
        tags = doc.tags
        title = doc.title
        if len(tags) >= 2:
            key = f'/{tags[0]}/{tags[1]}'
            if key not in sidebar:
                sidebar[key] = []

            if len(tags) > 2:
                group = tags[2]
            else:
                group = tags[1]  # 使用当前目录名称，即第二个tag

            group_index = next((i for i, item in enumerate(sidebar[key]) if item['text'] == group), None)
            if group_index is None:
                sidebar[key].append({'text': group, 'items': []})
                group_index = len(sidebar[key]) - 1

            sidebar[key][group_index]['items'].append({
                'text': title,
                'link': f'/{"/".join(tags)}/{title}'
            })
    return f"export default {json.dumps(sidebar, indent=2, ensure_ascii=False)}"

def update_script_file(content, file_name):
    # 获取脚本文件的绝对路径
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 从 script_dir 回退两级到项目根目录
    project_root = os.path.abspath(os.path.join(script_dir, '..', '..'))
    # 构建文件的绝对路径
    absolute_file_path = os.path.join(project_root, '.vitepress/theme/script/', file_name + ".mts")
    # 确保目标目录存在
    os.makedirs(os.path.dirname(absolute_file_path), exist_ok=True)
    # 打开文件，使用 'w' 模式会清除原有内容
    with open(absolute_file_path, 'w', encoding='utf-8') as file:
        # 写入新内容
        file.write(content)

def sync_local_docs(yuque_doc_dict: Dict[int, DocDetail]):
    # 1、初始化新插入博客列表
    insert_doc_list: List[DocDetail] = list(yuque_doc_dict.values())
    # 2、本地项目content下目录与语雀目录进行对比，分别区分删除和更新。
    content_path = get_content_posts_path()
    # 3、对比本地存在路径
    for root, dirs, files in os.walk(content_path):
        # 跳过 'public' 文件夹
        if 'public' in dirs:
            dirs.remove('public')
        for file in files:
            # 跳过 '.DS_Store' 和主页 'index.md' 文件
            if file == '.DS_Store' or file == 'index.md':
                continue
            # 获取文件路径
            local_file_path = os.path.join(root, file)
            # 获取博客概览
            local_doc_detail = get_blog_detail(get_file_content(local_file_path))
            if local_doc_detail is None:
                # 3.1、本地博客不存在博客信息，则直接删除
                remove_blog_and_file(local_file_path)
                print('sync_local-[local_doc_detail is None]-remove: ', local_file_path)
                continue
            # 本地博客存在博客信息，则获取语雀博客信息
            yuque_doc_detail: DocDetail = yuque_doc_dict.get(local_doc_detail.doc_id)
            if yuque_doc_detail is None:
                # 3.2、如果语雀中不存在该博客，则表明已从语雀中删除，故删除本地文件
                remove_blog_and_file(local_file_path)
                print('sync_local-[yuque_doc_detail is None]-remove: ', local_file_path)
                continue
            # 本地博客存在 且 语雀博客存在
            if yuque_doc_detail.content is None:
                # 3.3、如果语雀文档没有内容则删除博客
                remove_blog_and_file(local_file_path)
                insert_doc_list.remove(yuque_doc_detail)
            local_update_time = local_doc_detail.update_time
            yuque_update_time = yuque_doc_detail.update_time
            if local_update_time is None or yuque_update_time > local_update_time:
                # 3.4、如果本地博客更新时间戳为空 或者 语雀博客更新时间戳大于本地时间戳 则 更新本地博客
                update_local_doc(yuque_doc_detail)
                # 维护
                insert_doc_list.remove(yuque_doc_detail)
                print('sync_local-update: ', local_file_path)
    # 4、插入（本地没有的博客）剩余博客
    for doc_detail in insert_doc_list:
        insert_local_doc(doc_detail)
        print('sync_local-insert: ', doc_detail.title)


