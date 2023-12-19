---
book_id: 28973507
cnblog_id: '17913037'
doc_id: 119549494
tags:
- 云容器化
- Docker
title: Docker网络模式--network_mode
---
`docker-compose.yml` 配置文件中的 `network_mode` 是用于设置网络模式的，与 `docker run` 中的 `--network` 选项参数一样的，可配置如下参数：
<a name="bC8cc"></a>
## 一、bridge

- **默认 **的网络模式。如果没有指定网络驱动，默认会创建一个 `bridge` 类型的网络。
- 桥接模式一般是用在应用是独立的情况，容器之间不需要互相通信。
```yaml
network_mode: "bridge"
```
<a name="YfZE5"></a>
## 二、host

- `host` 网络模式，针对的也是应用是独立的情况，在 `host` 网络模式下，移除了宿主机与容器之间的网络隔离，**容器直接使用宿主机的网络**，这样就能在容器中访问宿主机网络
- `host` 网络模式只对 `Docker 17.06` 以及更高版本的 `swarm` 服务可用
```yaml
network_mode: "host"
```
<a name="dwQQ8"></a>
## 三、none

- `none` 表示对于这个 `container` ，禁用所有的网络。
```yaml
network_mode: "none"
```
<a name="TzeOo"></a>
## 四、container

- 指定容器网络。
```yaml
network_mode: "container:[container name/id]"
```
<a name="Gy0tH"></a>
## 五、自定义网络

- 指向自己定义的网段
```powershell
# 创建子网掩码为16位的网段
docker network create --subnet=172.18.0.0/16 mynet

# 查看自定义网段信息
docker network inspect mynet
```
```yaml
network_mode: "mynet"
```


