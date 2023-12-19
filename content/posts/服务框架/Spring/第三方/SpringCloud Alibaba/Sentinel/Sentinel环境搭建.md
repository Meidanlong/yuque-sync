---
book_id: 28973507
cnblog_id: '17913127'
doc_id: 88782405
tags:
- 服务框架
- Spring
- 第三方
- SpringCloud Alibaba
- Sentinel
title: Sentinel环境搭建
---
<a name="MrqKq"></a>
# 一、Sentinel控制台
详见：[Docker安装Sentinel](https://www.yuque.com/meidanlong/tzty91/ukcnfh?view=doc_embed)
<a name="F0PIu"></a>
# 二、SpringBoot集成
<a name="Cpzeq"></a>
## 1、依赖
```xml
<dependency>
  <groupId>com.alibaba.cloud</groupId>
  <artifactId>spring-cloud-starter-alibaba-sentinel</artifactId>
</dependency>
```
<a name="EKtuJ"></a>
## 2、配置
```yaml
management:
  endpoints:
    web:
      exposure:
        include: '*'
spring:
  cloud:
    sentinel:
      transport:
        dashboard: localhost:8858
      filter:
        enabled: false
        url-patterns: /**
server:
  port: 9000
```
<a name="XCG2G"></a>
## 3、注解
无注解
<a name="tB2sz"></a>
# 三、使用Sentinel进行流控


