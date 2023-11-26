import requests

import os

yuque_access_token = os.environ.get('yuque_access_token')

project_path = os.path.abspath(os.path.dirname(__file__))

print(project_path)

# 知识库列表
url = 'https://www.yuque.com/api/v2/groups/meidanlong/repos'

params = {'offset': 0, 'limit': 100}
headers = {'accept': 'application/json', 'X-Auth-Token': yuque_access_token}

res = requests.get(url=url, headers=headers, params=params)

print("response:", res.text)
