import os

import toml
from pypinyin import lazy_pinyin


def get_hugo_config():
    config_path = os.path.join(os.path.dirname(__file__), '../../config.toml')
    with open(config_path, 'r') as file:
        config = toml.load(file)
        print(config['menu']['main'])


def hugo_path_config(tags: list):
    dir_list = []
    for index, tag in enumerate(tags):
        single_dir = {'identifier': tag, 'name': tag, 'url': tag, 'weight': index}
        # dir_pinyin = convert_to_pinyin(tag)
        dir_list.append(single_dir)
    return {
        'menu': {
            'main': dir_list
        }
    }


def convert_to_pinyin(s):
    return ''.join(lazy_pinyin(s))
