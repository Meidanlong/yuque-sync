---
book_id: 28973507
cnblog_id: '17913051'
doc_id: 133382004
tags:
- 存储/中间件
- Redis
- Redis Cluster
title: Redis Cluster 架构
---
<a name="ldfWt"></a>
# 一、架构类型
<a name="sUvd3"></a>
## 1、单机架构
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1662268975044-5534df8b-937b-47a2-866b-fa04a5a0f886.png#averageHue=%23fefefe&clientId=ub5828f05-ecf9-4&from=paste&height=393&id=u2c5633f4&originHeight=786&originWidth=1402&originalType=binary&ratio=1&rotation=0&showTitle=false&size=196198&status=done&style=none&taskId=uf3ee87c0-7686-4133-a08b-6f7a2fc5052&title=&width=701)
<a name="qCKrr"></a>
## 2、分布式架构
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1662274911313-9f05425c-d955-4c9b-9059-e0925d9d989e.png#averageHue=%236c9052&clientId=ub5828f05-ecf9-4&from=paste&height=398&id=u851476a0&originHeight=796&originWidth=706&originalType=binary&ratio=1&rotation=0&showTitle=false&size=280292&status=done&style=none&taskId=u2305907c-a0f1-4ca7-ab84-c53b83c08f1&title=&width=353)
<a name="zotWT"></a>
# 二、Redis Cluster 架构

1. 节点
   1. 集群模式：cluster-enable:yes
2. meet
   1. ![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1662275211068-68d3e259-5ba2-4049-b082-8d83d14400a3.png#averageHue=%23fafaf8&clientId=ub5828f05-ecf9-4&from=paste&height=513&id=u468e3b86&originHeight=1026&originWidth=1600&originalType=binary&ratio=1&rotation=0&showTitle=false&size=736354&status=done&style=none&taskId=ubf26b1ea-d32f-4958-b498-24839e90330&title=&width=800)
   2. 所有节点共享消息
3. 指派槽
   1. ![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1662275354257-cc0f87be-2b6c-4ac2-80a1-531ef8017a8f.png#averageHue=%23f5f35a&clientId=ub5828f05-ecf9-4&from=paste&height=462&id=u5750cdce&originHeight=924&originWidth=2004&originalType=binary&ratio=1&rotation=0&showTitle=false&size=656400&status=done&style=none&taskId=uc24cf4c5-4235-4301-acef-405dd624700&title=&width=1002)
4. 复制
<a name="dhiZ2"></a>
## 1、Redis Cluster特性

- 主从复制
- 高可用
- 分片
<a name="rpOcP"></a>
# 三、集群伸缩
<a name="jVir2"></a>
## 1、原理
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1662275816012-a9b71eee-09d9-4398-a39c-6646bdbab983.png#averageHue=%23c6c3bf&clientId=ub5828f05-ecf9-4&from=paste&height=412&id=uf6a36bd1&originHeight=824&originWidth=944&originalType=binary&ratio=1&rotation=0&showTitle=false&size=310838&status=done&style=none&taskId=u0a2a7012-19cc-4846-bab6-e27c5ec142c&title=&width=472)<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1662275831729-97e32289-2997-4370-8415-b5ccca8d389d.png#averageHue=%23f8f8f7&clientId=ub5828f05-ecf9-4&from=paste&height=391&id=u46ab7748&originHeight=782&originWidth=922&originalType=binary&ratio=1&rotation=0&showTitle=false&size=328487&status=done&style=none&taskId=u16c886ee-fc37-4005-8992-c482a0366a7&title=&width=461) <br />集群伸缩实际上是哈希槽和数据移动的过程
<a name="CmwYj"></a>
## 2、扩容
<a name="C45Tx"></a>
### 2.1、准备新节点

1. 开启“集群模式”
2. 配置和其他节点统一
3. 启动后是孤儿节点
4. ![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1662276088092-250923dd-02d2-41a2-ad76-dfc6b0c1c8f5.png#averageHue=%23cccac7&clientId=ub5828f05-ecf9-4&from=paste&height=250&id=u1a022bab&originHeight=500&originWidth=824&originalType=binary&ratio=1&rotation=0&showTitle=false&size=222248&status=done&style=none&taskId=u04c33510-21cc-475c-9166-42ae89a8a84&title=&width=412)
```shell
redis-server conf/redis-6385.conf
redis-server conf/redis-6386.conf
```
<a name="eXc96"></a>
### 2.2、加入集群
```shell
cluster meet ip 6385
cluster meet ip 6386
```

- ![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1662276181355-9139b5b3-bf7d-4a24-b444-941e88930e25.png#averageHue=%23ceccc9&clientId=ub5828f05-ecf9-4&from=paste&height=253&id=uf6357b00&originHeight=506&originWidth=760&originalType=binary&ratio=1&rotation=0&showTitle=false&size=227492&status=done&style=none&taskId=u6d52e9b3-6199-4fb7-b81c-29348d77dec&title=&width=380)
- 观察加入后集群配置：`cluster nodes`
- 扩容目的：
   - 为它迁移槽和数据实现扩容
   - 作为从节点负责故障转移

**其他扩容方式：**<br />官方工具：`redis-trib.rb`，可检测新节点是否为孤立节点。<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1662276374377-ebd350e6-bd62-4dbc-92f5-42c123970401.png#averageHue=%23f2f2f2&clientId=ub5828f05-ecf9-4&from=paste&height=251&id=u2e49689b&originHeight=502&originWidth=1928&originalType=binary&ratio=1&rotation=0&showTitle=false&size=223165&status=done&style=none&taskId=ud3afde7b-f6ae-4c8d-bd6e-9d910ecaa17&title=&width=964)
<a name="cyNg4"></a>
### 2.3、迁移槽和数据
<a name="fgiaF"></a>
#### 2.3.1、迁移槽计划
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1662276690342-5a70cfcd-fd99-4bed-9f9e-5bffb309429f.png#averageHue=%23c1bfbd&clientId=ub5828f05-ecf9-4&from=paste&height=310&id=u0d7ef0b8&originHeight=620&originWidth=978&originalType=binary&ratio=1&rotation=0&showTitle=false&size=293948&status=done&style=none&taskId=ua801096d-bb08-49e6-9e94-48c42028886&title=&width=489)<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1662276699074-80a89989-86bf-4347-9106-e274e1c760dc.png#averageHue=%23bfbdba&clientId=ub5828f05-ecf9-4&from=paste&height=343&id=ubc6ec023&originHeight=686&originWidth=622&originalType=binary&ratio=1&rotation=0&showTitle=false&size=229770&status=done&style=none&taskId=u37dfa501-bf7c-4d79-82f8-a7a749c76e4&title=&width=311)
<a name="aLsQt"></a>
#### 2.3.2、迁移数据
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1662276873067-3cf51e58-d831-4894-9971-1178a74d9130.png#averageHue=%23eeeeee&clientId=ub5828f05-ecf9-4&from=paste&height=353&id=u13d8a200&originHeight=706&originWidth=2062&originalType=binary&ratio=1&rotation=0&showTitle=false&size=469091&status=done&style=none&taskId=u9b421542-678d-4265-9971-28304b265e5&title=&width=1031)<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1662276889284-25afffc3-0e7b-48e6-9bd4-74138eef2294.png#averageHue=%23cfcbc7&clientId=ub5828f05-ecf9-4&from=paste&height=387&id=u7ecd7c4e&originHeight=774&originWidth=1200&originalType=binary&ratio=1&rotation=0&showTitle=false&size=434733&status=done&style=none&taskId=ubb82bd3b-be59-4be6-a587-9a9d2eefc07&title=&width=600)<br />**伪代码：**<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1662276935172-00e78f31-9248-461f-9e89-c91a0a138a62.png#averageHue=%23f3f3f3&clientId=ub5828f05-ecf9-4&from=paste&height=456&id=u812571ee&originHeight=912&originWidth=1468&originalType=binary&ratio=1&rotation=0&showTitle=false&size=512323&status=done&style=none&taskId=u87a56fc5-8b50-4dae-ae58-955e68d2e37&title=&width=734)
<a name="ym24u"></a>
#### 2.3.3、添加从节点

<a name="rsKp9"></a>
## 3、缩容
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1662277175921-18f5a6b5-d885-4b86-ae7d-eac939e47c55.png#averageHue=%23fbfafa&clientId=ub5828f05-ecf9-4&from=paste&height=464&id=ubd2af5a5&originHeight=928&originWidth=888&originalType=binary&ratio=1&rotation=0&showTitle=false&size=266481&status=done&style=none&taskId=u56a09c28-bcb8-43e6-a440-580a2c7dc10&title=&width=444)
<a name="Tan6S"></a>
### 3.1、下线迁移槽
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1662277248224-6f015acb-81c9-4669-9047-c3260f91a82f.png#averageHue=%23f0f0f0&clientId=ub5828f05-ecf9-4&from=paste&height=381&id=ua663ff59&originHeight=762&originWidth=762&originalType=binary&ratio=1&rotation=0&showTitle=false&size=312627&status=done&style=none&taskId=u4070cbd8-033c-4655-ac05-45174aadc82&title=&width=381)
<a name="VA39C"></a>
### 3.2、忘记节点
```shell
cluster forget {downNodeId}
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1662277321375-59770590-e792-4c42-8f20-bbac060c8abf.png#averageHue=%23f7f6f6&clientId=ub5828f05-ecf9-4&from=paste&height=294&id=uac7d1c4f&originHeight=588&originWidth=1058&originalType=binary&ratio=1&rotation=0&showTitle=false&size=271894&status=done&style=none&taskId=u6c60259a-bf8b-4b59-b4d5-cb268b3e94d&title=&width=529)

- 如果60s后，还有节点没有忘记这个下线节点，那么该节点的信息会再次在集群内传播
- 故，忘记节点要统一在集群内所有节点执行
<a name="KCIK1"></a>
### 3.3、关闭节点
```shell
./redis-trib.rb del-node ip:port nodeid
```
<a name="uMnwu"></a>
## 4、客户端路由
<a name="XyPB9"></a>
### 4.1、moved重定向
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1662513774250-5201a566-a5e6-46e4-b05f-5947e23f6236.png#averageHue=%23fefefd&clientId=ua305c792-21a5-4&from=paste&height=521&id=ucaca19e9&originHeight=1042&originWidth=2122&originalType=binary&ratio=1&rotation=0&showTitle=false&size=492945&status=done&style=none&taskId=uc58c6415-dbad-40bd-bf83-66b8cb11f13&title=&width=1061)
<a name="wn6jl"></a>
#### 4.1.1、槽命中：直接返回
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1662513828781-848c4c9a-37ab-4360-9bea-2d4c5713dab6.png#averageHue=%23f8f8f8&clientId=ua305c792-21a5-4&from=paste&height=412&id=u462603e8&originHeight=824&originWidth=2046&originalType=binary&ratio=1&rotation=0&showTitle=false&size=263814&status=done&style=none&taskId=u382701a6-0651-4ec9-a583-b292b829764&title=&width=1023)
<a name="bmFTX"></a>
#### 4.1.2、槽不命中：moved异常
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1662513873696-1940606c-dc28-4bc4-a77f-459dea60deb1.png#averageHue=%23f7f7f7&clientId=ua305c792-21a5-4&from=paste&height=503&id=uc3f7b07a&originHeight=1006&originWidth=2150&originalType=binary&ratio=1&rotation=0&showTitle=false&size=401231&status=done&style=none&taskId=u3b5a8636-2683-4d8e-94b4-c759405757f&title=&width=1075)
<a name="TWb9w"></a>
#### 4.1.3、redis-cli举例
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1662514016200-6b7a960a-0b24-477f-b2cb-9cadf0d324f6.png#averageHue=%23f5f0f4&clientId=ua305c792-21a5-4&from=paste&height=478&id=u6ae5bce1&originHeight=956&originWidth=1816&originalType=binary&ratio=1&rotation=0&showTitle=false&size=876730&status=done&style=none&taskId=ue32b91b8-f65a-41ec-96c7-77eaea7f476&title=&width=908)
<a name="NDg2I"></a>
### 4.2、ASK重定向

- slot迁移过程中客户端访问
- key已经迁移到新的节点，需要使用ASK重定向解决

![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1662514091640-24738a00-09a0-4031-a713-8aed86c0037b.png#averageHue=%23f7f7f7&clientId=ua305c792-21a5-4&from=paste&height=466&id=u8128c13e&originHeight=932&originWidth=924&originalType=binary&ratio=1&rotation=0&showTitle=false&size=415826&status=done&style=none&taskId=u0b8dfd8d-8bc9-446c-a5f9-d5c1b1d0888&title=&width=462)
<a name="tMyKM"></a>
#### 4.2.1、重定向解决
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1662514217852-18bf4a06-f24a-41e0-814c-a44497cdbe95.png#averageHue=%23fefefd&clientId=ua305c792-21a5-4&from=paste&height=328&id=u3c6e138f&originHeight=656&originWidth=2158&originalType=binary&ratio=1&rotation=0&showTitle=false&size=283488&status=done&style=none&taskId=u1e097979-99da-467d-afa8-9b0ec624f30&title=&width=1079)
<a name="U625W"></a>
#### 4.2.2、moved和ASK的区别

1. 两者都是客户端重定向
2. moved：槽已经确定迁移
3. ASK：槽还在迁移中
<a name="OvxLR"></a>
### 4.3、smart客户端
<a name="ZmjDT"></a>
#### 4.3.1、smart客户端原理
**追求性能（直连，取消代理）**

1. 从集群中选一个可运行的节点，使用cluster slots初始化槽和节点映射
2. 将cluster slots的结果映射到本地，为每个节点创建JedisPool
3. 准备执行命令
<a name="BQof3"></a>
#### 4.3.2、执行命令
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1662514566689-79f12c06-45a0-4f6e-b0ab-0a79a3402a84.png#averageHue=%23fafafa&clientId=ua305c792-21a5-4&from=paste&height=547&id=uc63bfc73&originHeight=1094&originWidth=2126&originalType=binary&ratio=1&rotation=0&showTitle=false&size=466942&status=done&style=none&taskId=u0f19e83c-d280-48c8-84c7-7cddd9e66b5&title=&width=1063)

