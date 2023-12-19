---
book_id: 28973507
cnblog_id: '17913035'
doc_id: 88782628
tags:
- 云容器化
- Docker
- Docker 安装
title: Docker安装Sentinel
---
`Docker`安装`Sentinel`控制台
<a name="P2QUg"></a>
# 一、搜索镜像
```shell
docker search sentinel
```
<a name="YDZGI"></a>
# 二、拉取镜像
```shell
docker pull bladex/sentinel-dashboard
```
<a name="xeC45"></a>
# 三、启动容器
```shell
docker run --name mysentinel --restart=always -p 8858:8858 -d bladex/sentinel-dashboard 
```
<a name="vfTaa"></a>
# 四、登录控制台
登录地址：[http://localhost:8858/](http://localhost:8858/)<br />用户名：sentinel<br />默认密码：sentinel

