---
book_id: 28973507
cnblog_id: '17913039'
doc_id: 123725710
tags:
- 云容器化
- Docker
- FAQ
title: 'Docker error: "host" network_mode is incompatible with port_bindings'
---
<a name="F09RF"></a>
## 原因
> 这个错误的原因是在Docker的配置中，使用了"host"网络模式，同时又试图绑定端口（port_bindings）。"host"网络模式意味着容器将直接使用主机的网络，而不是使用Docker创建的虚拟网络。在这种模式下，容器的网络栈不会被隔离，容器可以直接监听主机的网络端口。

因此，当使用"host"网络模式时，Docker不允许再进行端口绑定（port_bindings），因为端口已经直接暴露给容器了，没有必要再进行端口映射。所以，当你尝试同时使用这两个选项时，Docker会报出“"host" network_mode is incompatible with port_bindings”这个错误。

解决方法是，如果你需要使用"host"网络模式，那么就不要在Docker配置中设置端口绑定。如果你需要进行端口绑定，那么就不要使用"host"网络模式，而应该使用默认的桥接模式或者自定义网络。


<a name="Msh3b"></a>
## 解决
方式一：删除该网络模式设定<br />方式二：建立网段，将所需容器指定该网段
<a name="oq9GE"></a>
## 扩展
[Docker网络模式--network_mode](https://www.yuque.com/meidanlong/tzty91/vv3o3gaxmk1y13e2?view=doc_embed)

