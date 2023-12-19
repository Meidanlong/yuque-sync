---
book_id: 28973507
cnblog_id: 17912960
doc_id: 124064913
tags:
- 基础语法
- Python
title: Python获取服务器IP地址
---
<a name="O0xRN"></a>
## 一、依赖
```python
import socket
```
<a name="rAHwC"></a>
## 二、获取
```python
# 获取计算机名称
hostname = socket.gethostname()

# 获取本机IP
ip = socket.gethostbyname(hostname)
```
<a name="gcIsP"></a>
## 三、结果
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1683510587777-21a0017c-7e85-44f6-ac62-752f1db0a4cb.png#averageHue=%23f4f4f4&clientId=u171f1d48-2891-4&from=paste&height=52&id=ud77c93e7&originHeight=104&originWidth=812&originalType=binary&ratio=2&rotation=0&showTitle=false&size=10703&status=done&style=none&taskId=u8052012c-f848-45f8-848f-6b9d196e422&title=&width=406)

