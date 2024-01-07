#!/bin/bash

export PYTHONPATH=./

python -c "from sync/app import sync_yuque; sync_yuque()"

hugo deploy

python -c "from sync/app import push_pages; push_pages()"
