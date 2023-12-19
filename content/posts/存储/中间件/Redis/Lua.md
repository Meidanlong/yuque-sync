---
book_id: 28973507
cnblog_id: '17913052'
doc_id: 133380883
tags:
- 存储/中间件
- Redis
title: Lua
---
<a name="y198z"></a>
## 一、Redis中为什么要使用Lua
<a name="nEhmU"></a>
### 1、Redis 运行机制

- 单线程，难保证原子性
- 多客户端请求，进入redis内置队列，执行之后与预期有偏差
   - 可将请求打包，使用redis事务
   - 事务增加代码复杂度
<a name="orra1"></a>
### 2、Lua如何解决该问题

- Lua不是顺序发送单条命令
- 而是将多个命令组合成一个Lua脚本发送，故多个命令是一次性发送到redis服务端的

