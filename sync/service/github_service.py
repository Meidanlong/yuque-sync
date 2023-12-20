import os

from github import Github, UnknownObjectException

from sync.domain.constant.contants import TARGET_DIR
from sync.domain.constant.private_data import GITHUB_TOKEN


def get_github_repo(repo_name:str):
    # 使用access token
    g = Github(GITHUB_TOKEN)
    # 获取仓库，替换成你的仓库名字
    return g.get_user().get_repo(repo_name)


def push_github_origin(repo_name: str, branch:str, file_path: str, file_content: str, commit_message: str):
    repo = get_github_repo(repo_name)
    total_file_path = os.path.join(TARGET_DIR, file_path)
    try:
        # 检查文件是否在仓库中
        contents = repo.get_contents(total_file_path, ref="refs/heads/" + branch)
        repo.update_file(contents.path, commit_message, file_content, contents.sha, branch=branch)
        print(f"文件 '{file_path}' 已更新.")
    except UnknownObjectException as e:
        # 如果文件不存在，那就创建它
        repo.create_file(total_file_path, commit_message, file_content, branch=branch)
        print(f"文件 '{file_path}' 已创建.")
