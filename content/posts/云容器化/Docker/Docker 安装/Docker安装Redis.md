---
book_id: 28973507
cnblog_id: '17913034'
doc_id: 84165048
tags:
- 云容器化
- Docker
- Docker 安装
title: Docker安装Redis
---
<a name="sEPWS"></a>
# 一、拉取镜像
```shell
docker pull redis

docker 
```
<a name="DXFVu"></a>
# 二、运行Redis
```shell
docker run --name myredis -p 6379:6379 -d redis
```
<a name="WjSqo"></a>
# 三、连接Redis-cli
```shell
docker exec -it java_redis redis-cli
```

