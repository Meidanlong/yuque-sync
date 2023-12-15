#!/bin/bash


export yuque_access_token=8RJsszjXfqrpxbsCW8RqmgtEQsfmeiNuyPZAKME1

# 正式workflows
export PYTHONPATH=./
python sync/get_yuque_docs.py

# 本地环境
#export PYTHONPATH=../
#python get_yuque_docs.py