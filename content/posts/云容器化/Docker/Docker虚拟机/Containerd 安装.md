---
book_id: 28973507
cnblog_id: '17913028'
doc_id: 134045104
tags:
- 云容器化
- Docker
- Docker虚拟机
title: Containerd 安装
update_time: 2023-07-23 06:18:25
---
`Containerd`是一个开源的容器运行时工具，用于管理和运行容器。它为容器提供了高效，安全的执行环境，支持各种容器格式和镜像，极简化的容器生命周期管理，使得构建和部署应用程序更加方便和可靠。<br />[官方文档](https://github.com/containerd/containerd/blob/main/docs/getting-started.md)
<a name="lMlI0"></a>
## 一、下载/安装
```powershell
# 下载
curl -LO https://github.com/containerd/containerd/releases/download/v1.6.6/containerd-1.6.6-linux-amd64.tar.gz

# 解压
tar Cxzvf /usr/local containerd-1.6.6-linux-amd64.tar.gz

# 查看版本
ctr -v 
ctr version
```
<a name="ZpATL"></a>
## 二、配置systemd任务
```powershell
mkdir -p /usr/local/lib/systemd/system/ && \
curl -L https://raw.githubusercontent.com/containerd/containerd/main/containerd.service -o /usr/local/lib/systemd/system/containerd.service && \
systemctl daemon-reload && \
systemctl enable --now containerd
```
<a name="VGwq3"></a>
## 三、安装runc
`runc`实现了容器的`init`，`run`，`create`，`ps`...我们在运行容器所需要的`cmd`
```powershell
curl -LO https://github.com/opencontainers/runc/releases/download/v1.1.1/runc.amd64 && \
install -m 755 runc.amd64 /usr/local/sbin/runc
```
<a name="NYGSU"></a>
## 四、安装cni
CNI(Container Network Interface) 是一套容器网络接口规范，通过插件的形式支持各种各样的网络类型，而标准化的好处就是你只需一套标准json配置就可以为一个容器创建网络接口
```powershell
curl -JLO https://github.com/containernetworking/plugins/releases/download/v1.1.1/cni-plugins-linux-amd64-v1.1.1.tgz
mkdir -p /opt/cni/bin && \
tar Cxzvf /opt/cni/bin cni-plugins-linux-amd64-v1.1.1.tgz
```
<a name="omoDk"></a>
## 五、配置containerd[镜像源](https://so.csdn.net/so/search?q=%E9%95%9C%E5%83%8F%E6%BA%90&spm=1001.2101.3001.7020)
```powershell
mkdir -p /etc/containerd && \
containerd config default > /etc/containerd/config.toml && \
sed -i "s#k8s.gcr.io/pause#registry.aliyuncs.com/google_containers/pause#g"  /etc/containerd/config.toml  && \
sed -i 's#SystemdCgroup = false#SystemdCgroup = true#g' /etc/containerd/config.toml  && \
sed -i '/registry.mirrors]/a\ \ \ \ \ \ \ \ [plugins."io.containerd.grpc.v1.cri".registry.mirrors."docker.io"]' /etc/containerd/config.toml  && \
sed -i '/registry.mirrors."docker.io"]/a\ \ \ \ \ \ \ \ \ \ endpoint = ["http://hub-mirror.c.163.com"]' /etc/containerd/config.toml && \
sed -i '/hub-mirror.c.163.com"]/a\ \ \ \ \ \ \ \ [plugins."io.containerd.grpc.v1.cri".registry.mirrors."k8s.gcr.io"]' /etc/containerd/config.toml  && \
sed -i '/"k8s.gcr.io"]/a\ \ \ \ \ \ \ \ \ \ endpoint = ["http://registry.aliyuncs.com/google_containers"]' /etc/containerd/config.toml && \
echo "===========restart containerd to reload config===========" && \
systemctl restart containerd
```

---

```powershell
#!/bin/bash
echo "===========Installing containerd to /user/local===========" && \
tar Cxzvf /usr/local containerd-1.6.6-linux-amd64.tar.gz && \
mkdir -p /usr/local/lib/systemd/system/ && \
echo "===========start containerd via systemd===========" && \
curl -L https://raw.githubusercontent.com/containerd/containerd/main/containerd.service -o /usr/local/lib/systemd/system/containerd.service && \
systemctl daemon-reload && \
systemctl enable --now containerd
 
echo "===========install runc.amd64 to /usr/local/sbin/runc==========="
curl -LO https://github.com/opencontainers/runc/releases/download/v1.1.4/runc.amd64 && \
install -m 755 runc.amd64 /usr/local/sbin/runc
 
echo "===========install cni==========="
mkdir -p /opt/cni/bin && \
tar Cxzvf /opt/cni/bin cni-plugins-linux-amd64-v1.1.1.tgz
 
echo "===========generate containerd config==========="
mkdir -p /etc/containerd && \
containerd config default > /etc/containerd/config.toml && \
sed -i "s#k8s.gcr.io/pause#registry.aliyuncs.com/google_containers/pause#g"  /etc/containerd/config.toml  && \
sed -i 's#SystemdCgroup = false#SystemdCgroup = true#g' /etc/containerd/config.toml  && \
sed -i '/registry.mirrors]/a\ \ \ \ \ \ \ \ [plugins."io.containerd.grpc.v1.cri".registry.mirrors."docker.io"]' /etc/containerd/config.toml  && \
sed -i '/registry.mirrors."docker.io"]/a\ \ \ \ \ \ \ \ \ \ endpoint = ["http://hub-mirror.c.163.com"]' /etc/containerd/config.toml && \
sed -i '/hub-mirror.c.163.com"]/a\ \ \ \ \ \ \ \ [plugins."io.containerd.grpc.v1.cri".registry.mirrors."k8s.gcr.io"]' /etc/containerd/config.toml  && \
sed -i '/"k8s.gcr.io"]/a\ \ \ \ \ \ \ \ \ \ endpoint = ["http://registry.aliyuncs.com/google_containers"]' /etc/containerd/config.toml && \
echo "===========restart containerd to reload config===========" && \
systemctl restart containerd
```
<a name="qr4oh"></a>
## 六、nerdctl安装及使用
`nerdctl`工具，是`containerd`官方为了让`docker`用户无感切换到`containerd`而开发的命令行工具。也就是`docker`的命令可以直接在`nerdctl`上使用<br />[官方文档](https://github.com/containerd/nerdctl)
```powershell
curl -LO https://github.com/containerd/nerdctl/releases/download/v0.22.2/nerdctl-0.22.2-linux-amd64.tar.gz
tar xzvf nerdctl-0.22.2-linux-amd64.tar.gz
cp nerdctl /usr/local/bin/
rm -rf containerd-rootless* nerdctl
```

