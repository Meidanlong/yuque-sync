#!/bin/bash

cd ..
export PYTHONPATH=./

python -c "from sync.app import yuque_sync; yuque_sync()"

#brew install hugo
hugo deploy

python -c "from sync.app import push_pages; push_pages()"
