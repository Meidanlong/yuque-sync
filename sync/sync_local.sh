#!/bin/bash

export PYTHONPATH=../

python -c "from app import sync_yuque; sync_yuque()"

hugo deploy

python -c "from app import push_pages; push_pages()"
