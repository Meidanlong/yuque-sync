---
book_id: 28973507
cnblog_id: '17913102'
doc_id: 149927384
tags:
- 服务框架
- Spring
title: spring framework启动问题
update_time: 2023-12-12 06:08:28
---
<a name="JXhJr"></a>
# 正确Gradle版本
查看`gradle/wrapper/gradle-wrapper.properties`<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1702361296646-9d62a2e9-74e8-4e98-86d6-fdf28444698d.png#averageHue=%23fdfdfd&clientId=u5a9ae4a4-dcac-4&from=paste&height=126&id=uf232e2bd&originHeight=252&originWidth=1278&originalType=binary&ratio=2&rotation=0&showTitle=false&size=73057&status=done&style=none&taskId=u9653d72d-309d-439b-8ba2-37aaa6ab4fe&title=&width=639)
<a name="bgkNp"></a>
# A build scan was not published as you have not authenticated with server 'ge.spring.io'.
注释`ge.conventions`
```
plugins {
	id "com.gradle.enterprise" version "3.6.1"
//	id "io.spring.ge.conventions" version "0.0.7"
}
```
<a name="UJrpT"></a>
# 程序包jdk.jfr不存在
该包在`1.8`版本的jdk中不存在，需要升级到jdk`11`<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1702359320129-2612bd1a-8955-4810-8c64-bb3f88c7ba29.png#averageHue=%23f4f5f8&clientId=ubba8e5f7-bce2-4&from=paste&height=700&id=u83aaae56&originHeight=1400&originWidth=1800&originalType=binary&ratio=2&rotation=0&showTitle=false&size=131203&status=done&style=none&taskId=ube77fd4e-d2b9-4628-afb0-38398097b0a&title=&width=900)

