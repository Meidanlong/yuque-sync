---
book_id: 28973507
cnblog_id: '17913029'
doc_id: 133594690
tags:
- 云容器化
- Docker
- Docker 安装
title: docker-compose 安装
update_time: 2023-08-23 03:21:25
---
<a name="V48J4"></a>
## 一、下载
```shell
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
<a name="Z9aV4"></a>
## 二、赋予执行权限
```shell
sudo chmod +x /usr/local/bin/docker-compose
```
<a name="capQC"></a>
## 三、创建软链接
```shell
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```
<a name="cJr80"></a>
## 四、测试
```shell
docker-compose --version
```

