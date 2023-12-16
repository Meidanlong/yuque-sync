#!/bin/bash

export yuque_access_token=8RJsszjXfqrpxbsCW8RqmgtEQsfmeiNuyPZAKME1

github_token=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
github_url=https://github.com/Meidanlong/yuque-sync.git
github_git=${github_url#*//}

# 正式workflows
#export PYTHONPATH=./
#python sync/get_yuque_docs.py

# 本地环境
#export PYTHONPATH=../
#python get_yuque_docs.py

# 同步github
git remote set-url origin 'https://'${github_token}'@'${github_git}
git config --global user.email "meidanlong@gmail.com"
git config --global user.name "meidanlong"
git add .
git commit -m "sync-job"
git remote -v
git push -f