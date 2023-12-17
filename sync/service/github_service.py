from github import Github, UnknownObjectException

from sync.domain.constant.private_data import GITHUB_TOKEN, REPO_NAME, REPO_BRANCH


def get_repo():
    # 使用access token
    g = Github(GITHUB_TOKEN)
    # 获取仓库，替换成你的仓库名字
    return g.get_user().get_repo(REPO_NAME)


def push_origin(file_path: str, file_content: str, commit_message: str):
    repo = get_repo()
    try:
        # 检查文件是否在仓库中
        contents = repo.get_contents(file_path, ref="refs/heads/" + REPO_BRANCH)
        repo.update_file(contents.path, commit_message, file_content, contents.sha, branch=REPO_BRANCH)
        print(f"文件 '{file_path}' 已更新.")
    except UnknownObjectException as e:
        # 如果文件不存在，那就创建它
        repo.create_file(file_path, commit_message, file_content, branch=REPO_BRANCH)
        print(f"文件 '{file_path}' 已创建.")


if __name__ == '__main__':
    # 文件路径和文件内容
    file_path = "content/posts/dew.md"
    file_content = "## File content 更新"
    # 提交信息
    commit_message = "deploy"
    push_origin(file_path, file_content, commit_message)
