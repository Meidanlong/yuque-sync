---
book_id: 28973507
cnblog_id: '17913022'
doc_id: 133386184
tags:
- 基础语法
- Java
title: Servlet
---
<a name="UCujv"></a>
## 一、简介
1. Java程序 
2. 无法独立运行，需tomcat、jetty等容器载体
3. Servlet第一次载入时候由容器创建（`init()`），然后会一直存在在容器中处理请求（`service()`），直到服务器关闭过web容器被移除(`destory()`)

![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1667112257548-7f15c17c-a80a-4b19-bc8f-447b67a11994.png#averageHue=%23e9e9bf&clientId=u18adf2c0-abe7-4&from=paste&height=297&id=ub6ba7a25&originHeight=594&originWidth=1480&originalType=binary&ratio=1&rotation=0&showTitle=false&size=525346&status=done&style=none&taskId=ud5531099-c3e9-4b6d-af8a-4bd9f814fba&title=&width=740)
<a name="yyFRp"></a>
## 二、目的
`HttpServlet.java` 判断区分GET请求POST请求等，调用`doGet()`/`doPost()`发起请求<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1667112729116-f2614e82-1ac9-4714-81d5-f5b95afe6bf1.png#averageHue=%23f7f6f4&clientId=u18adf2c0-abe7-4&from=paste&height=373&id=u585213b8&originHeight=746&originWidth=1822&originalType=binary&ratio=1&rotation=0&showTitle=false&size=444890&status=done&style=none&taskId=u2ccc6b27-f8dd-4d84-9ec7-b42eb7b315e&title=&width=911)<br />**为了减少Servlet数量**<br />参照Spring MVC，仅通过`DispacherServlet`进行请求派发，`DispacherServlet`做了三件事：

1. 拦截所有的请求
2. 解析请求
3. 派发给对应的Controller里面的方法进行处理

