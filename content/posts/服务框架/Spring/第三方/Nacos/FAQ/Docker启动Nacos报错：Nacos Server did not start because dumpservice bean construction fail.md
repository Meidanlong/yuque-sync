---
book_id: 28973507
cnblog_id: '17913126'
doc_id: 105191548
tags:
- 服务框架
- Spring
- 第三方
- Nacos
- FAQ
title: Docker启动Nacos报错：Nacos Server did not start because dumpservice bean construction
  fail
---
<a name="lLGLU"></a>
## 一、表象
1. 重启服务器之后Docker运行Nacos容器，启动成功，但是外网无法访问。
2. 查看了一下Nacos启动日志（docker logs nacos容器名）

![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1667736761968-107cba11-a242-418c-b021-0f82e0651495.png#averageHue=%233f3e3d&clientId=u22d6021b-03f5-4&from=paste&height=377&id=u68e2fb07&originHeight=754&originWidth=1142&originalType=binary&ratio=1&rotation=0&showTitle=false&size=159249&status=done&style=none&taskId=u0fe4d6fe-c811-4509-9db2-b067ef88ab9&title=&width=571)
<a name="obujS"></a>
## 二、分析
很明显是数据库配``置问题。。<br />如果是数据库配置的问题，可以着重检查以下信息<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1667737073721-66f92b40-6d9b-4203-a46c-2eedbfd81c8c.png#averageHue=%23f6eeeb&clientId=uf9565ff4-e17c-4&from=paste&height=107&id=u0971212a&originHeight=214&originWidth=622&originalType=binary&ratio=1&rotation=0&showTitle=false&size=51855&status=done&style=none&taskId=u0f3057bd-c84c-41a6-8bfb-24f122f14a1&title=&width=311)<br />尤其是MySQL内网Host，查询方式见[Docker安装Nacos](https://www.yuque.com/meidanlong/tzty91/wcuih0?view=doc_embed)
<a name="MJ770"></a>
## 三、解决
我已经确认数据库配置和连接都没有问题，但为什么启动时找不到数据源？后来找到解决办法：<br />**用其他客户端连接mysql唤醒它，重启Nacos容器即可**<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1667737357926-8609b242-4c38-4dad-a628-249156f00ece.png#averageHue=%233d3d3d&clientId=uf9565ff4-e17c-4&from=paste&height=417&id=ud8e026f3&originHeight=834&originWidth=1126&originalType=binary&ratio=1&rotation=0&showTitle=false&size=176975&status=done&style=none&taskId=u315a96ae-d45e-43f4-b1d0-a1fee2199be&title=&width=563)<br />容器启动成功！

