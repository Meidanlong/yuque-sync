---
book_id: 28973507
cnblog_id: '17913032'
doc_id: 83015745
tags:
- 云容器化
- Docker
- Docker 安装
title: Docker安装Nacos
---
<a name="J4qkj"></a>
# 一、单机部署
<a name="s9bWj"></a>
## 1、拉取镜像
```shell
# 拉取镜像
docker pull nacos/nacos-server
```
<a name="uxYYX"></a>
## 2、数据库配置
MySQL创建数据库名为nacos_config并导入官方脚本<br />[nacos-db-2-1-0.sql](https://github.com/alibaba/nacos/blob/2.1.0/config/src/main/resources/META-INF/nacos-db.sql)<br />注意版本标签，否则会遇到[Nacos配置：发布失败，请检查参数是否正确](https://www.yuque.com/meidanlong/tzty91/lgnwkq?view=doc_embed)问题
<a name="avTcY"></a>
## 3、创建挂载
```shell
mkdir -p /usr/local/docker/nacos/logs                  
mkdir -p /usr/local/docker/nacos/init.d          
touch /usr/local/docker/nacos/init.d/custom.properties
```
<a name="LNi1G"></a>
## 4、创建和启动容器
```shell
docker run -it \
--privileged \
--name wtnacos \
--restart=always \
--net wtnet \ # 指定自己网段
-p 8848:8848 \
-p 9848:9848 \
-e MODE=standalone \
-e JVM_XMS=256m \
-e JVM_XMX=256m \
-e SPRING_DATASOURCE_PLATFORM=mysql \
-e MYSQL_SERVICE_HOST=172.18.0.3 \
-e MYSQL_SERVICE_PORT=3306 \
-e MYSQL_SERVICE_DB_NAME=nacos \
-e MYSQL_SERVICE_USER=root \
-e MYSQL_SERVICE_PASSWORD=meisql \
-v wtnacosvolume:/home/nacos/init.d/custom.properties \
-v wtnacosvolume:/home/nacos/logs \
nacos/nacos-server
```
**补充**：查看MySql内网IP地址
```shell
# mymysql 为容器名称
docker inspect mymysql
```
```json
"Networks": {
  "bridge": {
    "IPAMConfig": null,
    "Links": null,
    "Aliases": null,
    "NetworkID": "6e13c6b5d82b75aaabe10e2834159a75359a9eef651adb358d88e19e361c33f2",
    "EndpointID": "9c05e373d79ee78464c672f6881765758599b16584bb4b7832cdd982a03e71e1",
    "Gateway": "172.17.0.1",
    "IPAddress": "172.17.0.3", <--
    "IPPrefixLen": 16,
    "IPv6Gateway": "",
    "GlobalIPv6Address": "",
    "GlobalIPv6PrefixLen": 0,
    "MacAddress": "02:42:ac:11:00:03"
  }
}
```
<a name="SHJ3W"></a>
## 5、访问Nacos网址
`http://ip:8848/nacos`<br />账号：nacos<br />密码：nacos

