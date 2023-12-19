---
book_id: 28973507
cnblog_id: '17912968'
doc_id: 149920386
tags:
- 基础语法
- Java
- FAQ
title: 查看mvn版本：cannot execute binary file
update_time: 2023-12-12 03:57:14
---
<a name="fzkFB"></a>
# 一、现象![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1702353371198-c4478fcc-39d2-4ced-9a32-1f736b05478b.png#averageHue=%230e0e0e&clientId=u4d8e05ce-0c25-4&from=paste&height=61&id=u7dc71a04&originHeight=122&originWidth=1888&originalType=binary&ratio=2&rotation=0&showTitle=false&size=27693&status=done&style=none&taskId=u7ecec3d8-9ecd-48d4-a8bd-0d537da9cca&title=&width=944)
<a name="UDeYN"></a>
# 二、原因
网络资料上大部分的原因是因为jdk不是46位导致失败。其实我这边的原因也查不多，目前使用的是Mac M2芯片的电脑但是还安装之前的jdk版本，将其替换为macos arm版本即可。
<a name="yZrli"></a>
# 三、操作
[JDK下载官网](https://www.oracle.com/java/technologies/downloads/#java8)<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1702353258244-d26e0313-b0f7-4129-bfb0-84e182889c60.png#averageHue=%23f9f8f8&clientId=u4d8e05ce-0c25-4&from=paste&height=632&id=u2b147b09&originHeight=1264&originWidth=2176&originalType=binary&ratio=2&rotation=0&showTitle=false&size=274427&status=done&style=none&taskId=u497aef5e-a1fd-4450-a8e1-4cf0b661153&title=&width=1088)<br />下载、解压并更新环境变量<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1702353339963-13a082bb-1143-498a-b170-079e9c30e38c.png#averageHue=%230f0f0f&clientId=u4d8e05ce-0c25-4&from=paste&height=136&id=u918173a6&originHeight=272&originWidth=890&originalType=binary&ratio=2&rotation=0&showTitle=false&size=47195&status=done&style=none&taskId=uc8137e6c-48f1-49d8-91e2-5320bc2a050&title=&width=445)
<a name="fKxwW"></a>
# 四、修复
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1702353427938-14bc133c-55f8-4929-8c66-79a9c2c02f35.png#averageHue=%230d0d0d&clientId=u4d8e05ce-0c25-4&from=paste&height=111&id=u4c2d6ab8&originHeight=222&originWidth=1776&originalType=binary&ratio=2&rotation=0&showTitle=false&size=49992&status=done&style=none&taskId=uef6a8d7e-5a98-4125-a555-738f6aa1b9e&title=&width=888)

