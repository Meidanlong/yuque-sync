#!/bin/bash

export PYTHONPATH=../

python -c "from app import yuque_sync; yuque_sync()"

hugo deploy

python -c "from app import push_pages; push_pages()"
