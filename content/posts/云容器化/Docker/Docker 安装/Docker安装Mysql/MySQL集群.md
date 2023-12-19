---
book_id: 28973507
cnblog_id: '17913031'
doc_id: 83097028
tags:
- 云容器化
- Docker
- Docker 安装
- Docker安装Mysql
title: MySQL集群
---
<a name="Y9HNN"></a>
# 一、MySQL集群方案
<a name="wiS8y"></a>
## 1、常见MySQL集群方案
<a name="pc1eB"></a>
### 1.1、Replication
**特点**：

- 速度快
- 弱一致性

适用于`低价值`数据：

- 日志
- 新闻
- 帖子
<a name="Xj4EB"></a>
### 1.2、PXC
**特点**：

- 速度慢
- 强一致性

适用于`高价值`数据：

- 订单
- 账户
- 财务
<a name="hkaUF"></a>
#### 1.2.1、PXC原理
全称（Percona XtraDB Cluster）<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1657588969278-85d73d0a-960a-4369-a245-014d4449e2cf.png#averageHue=%23d5aea1&clientId=u91d8e52d-7d4c-4&errorMessage=unknown%20error&from=paste&height=194&id=ua8da4cf5&originHeight=388&originWidth=776&originalType=binary&ratio=1&rotation=0&showTitle=false&size=103527&status=error&style=none&taskId=ub5d443e5-67a5-4925-a59c-6388c80f227&title=&width=388)<br />任何数据库节点都是可读可写的<br />建议PXC使用PerconaServer（MySQL改进版，性能提升很大）
<a name="YP0Lw"></a>
#### 1.2.2、PXC方案与Replication方案的对比
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1657589088909-947b15df-cb7c-4301-a362-d91710a34b6c.png#averageHue=%23f6e7e5&clientId=u91d8e52d-7d4c-4&errorMessage=unknown%20error&from=paste&height=328&id=ua41b4b9f&originHeight=656&originWidth=1102&originalType=binary&ratio=1&rotation=0&showTitle=false&size=162214&status=error&style=none&taskId=udf5efd7f-18f5-46fa-89aa-44e5b56992e&title=&width=551)<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1657589132631-9eb2edce-90d4-418c-adb0-eba7d664f5c7.png#averageHue=%23f4e6e4&clientId=u91d8e52d-7d4c-4&errorMessage=unknown%20error&from=paste&height=253&id=u19593258&originHeight=506&originWidth=706&originalType=binary&ratio=1&rotation=0&showTitle=false&size=69144&status=error&style=none&taskId=u9cf62a69-4f5c-4e52-8ce6-01f1382d176&title=&width=353)
<a name="dv4l8"></a>
#### 1.2.3、PSC的数据强一致性
PSC同步复制，失误再所有集群节点要么同时提交，要么不提交<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1657589251633-586a703c-61e7-4ab7-b6e7-3ece9982e760.png#averageHue=%23f4e1df&clientId=u91d8e52d-7d4c-4&errorMessage=unknown%20error&from=paste&height=282&id=u315ba5ee&originHeight=564&originWidth=1032&originalType=binary&ratio=1&rotation=0&showTitle=false&size=140955&status=error&style=none&taskId=uef7441b5-a2eb-467e-8b09-6426f2c0d02&title=&width=516)<br />Replication采用异步复制，无法保证数据的一致性<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1657589301978-4dc6e585-a219-41ee-8fa8-5b3e8148cab9.png#averageHue=%23f4e3e0&clientId=u91d8e52d-7d4c-4&errorMessage=unknown%20error&from=paste&height=165&id=ue9e75c39&originHeight=330&originWidth=918&originalType=binary&ratio=1&rotation=0&showTitle=false&size=67480&status=error&style=none&taskId=u50d8fbe5-37cf-419c-8cb4-56afca33ef1&title=&width=459)
<a name="PR0LM"></a>
# 二、搭建PXC集群
<a name="hE9nU"></a>
## 1、拉取镜像
```shell
# 拉取镜像
docker pull percona/percona-xtradb-cluster:5.7.21

# 修改镜像名称
docker tag percona/percona-xtradb-cluster:5.7.21 pxc

# 删除原镜像
docker rmi percona/percona-xtradb-cluster:5.7.21

# 本地安装
docker load < /home/soft/pxc.tar.gz
```
<a name="ggKmK"></a>
## 2、创建内部网段
出于安全考虑，需要给PXC集群实例创建Docker内部网络
```shell
# 创建网段
docker network create net1

# 规定具体网段，子网掩码24位
docker network create --subnet=172.18.0.0/24 net1

# 查看网段信息
docker network inspect net1

# 删除网段
docker network rm net1
```
<a name="lH8YN"></a>
## 3、创建Docker卷
将数据映射到宿主机的目录上<br />容器中的PXC节点映射数据目录的解决办法
```shell
# 创建数据卷
docker volume create --name v1

# 查看卷信息
docker (volume) inspect v1

# 删除卷
docker volume rm v1
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1657590198445-a76d9960-905e-46cc-ad95-051f88e0acec.png#averageHue=%230d0b0a&clientId=u91d8e52d-7d4c-4&errorMessage=unknown%20error&from=paste&height=292&id=u2b272557&originHeight=584&originWidth=1370&originalType=binary&ratio=1&rotation=0&showTitle=false&size=264385&status=error&style=none&taskId=u85296a95-7eb9-4013-8618-fd40bf68182&title=&width=685)
<a name="wsFCz"></a>
## 4、创建PXC容器
```shell
docker run -d -p 3306:3306 \
-v v1:/var/lib/mysql \
-e MYSQL_ROOT_PASSWORD=adc123456 \
-e CLUSTER_NAME=PXC \
# 数据库节点同步密码
-e XTRABACKUP_PASSWORD=abc123456 \
# -e CLUSTER_JOIN=node1
# 最高权限
--privileged \
--name node1 \
--net net1 \
--ip 172.18.0.2 \
pxc
```
`第二个节点及以后的节点`需要更改的配置：

1. 端口号
2. 集群加入节点
3. 名称
4. IP
<a name="JNrHe"></a>
### 必须主节点能连接上，再去创建其他节点

- 因为主节点创建之后，它需要初始化PXC集群环境，生成各种配置文件，所以消耗的时间比较长，你等待一分钟左右的时间，然后用客户端连接主节点，如果能连接上，说明主节点已经创建成功。这时候再去创建其他PXC节点。
- 如果你刚创建完主节点，就去创建其他节点。因为主节点还不能正常访问，其他从节点连接不上主节点，无法加入PXC集群，所以你创建的所有从节点都处在闪退的状态。正确的做法是每创建一个节点，能用客户端访问了，再去创建下一个节点。
<a name="QpzzS"></a>
# 三、数据库负载均衡

