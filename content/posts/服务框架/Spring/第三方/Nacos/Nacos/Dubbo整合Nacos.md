---
book_id: 28973507
cnblog_id: '17913118'
doc_id: 88385059
tags:
- 服务框架
- Spring
- 第三方
- Nacos
- Nacos
title: Dubbo整合Nacos
---
<a name="pfrCs"></a>
# 一、Dubbo整体架构
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1659499041235-208dbb63-05a1-4ec0-a553-758318f0d257.png#clientId=u7b9446cc-9e72-4&from=paste&height=366&id=u095d5356&originHeight=424&originWidth=500&originalType=binary&ratio=1&rotation=0&showTitle=false&size=80649&status=done&style=none&taskId=ud58aa6f5-03ac-4623-ba45-0ab73d4e779&title=&width=432)
<a name="COLpR"></a>
# 二、Dubbo环境搭建
<a name="LaVh1"></a>
## 1、集成三板斧
<a name="f1EeT"></a>
### 1.1、依赖
```xml
<dependency>
   <groupId>com.alibaba.cloud</groupId>
   <artifactId>spring-cloud-starter-dubbo</artifactId>
</dependency>
```
<a name="jeRow"></a>
### 1.2、配置
无配置
<a name="NrsmG"></a>
### 1.3、注解
<a name="HgXCl"></a>
#### 1.3.1、启动注解
```java
@EnableDubbo
```
<a name="PYjng"></a>
#### 1.3.2、服务注解
```java
// 服务提供者
@DubboService(version = "1.0-SNAPSHOT", group = "user")

// 服务消费者
@DubboReference(version = "1.0-SNAPSHOT", group = "user")
```

