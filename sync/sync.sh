#!/bin/bash

export PYTHONPATH=./

python -c "from sync.app import yuque_sync; yuque_sync()"

apt-get install hugo
hugo deploy

python -c "from sync.app import push_pages; push_pages()"
