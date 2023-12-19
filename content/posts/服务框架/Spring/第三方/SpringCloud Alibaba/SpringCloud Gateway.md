---
book_id: 28973507
cnblog_id: '17913130'
doc_id: 97830575
tags:
- 服务框架
- Spring
- 第三方
- SpringCloud Alibaba
title: SpringCloud Gateway
---
<a name="noeRK"></a>
# 一、依赖
```java
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-gateway</artifactId>
</dependency>
```
<a name="tpgCp"></a>
# 二、配置
```java
spring:
  cloud:
    gateway:
      routes:
        - id: product
          uri: http://localhost:9000
          predicates:
            - Host=product.muke.com**
        - id: auth
          uri: http://localhost:5000
          predicates:
            - Path=/oauth/token
        - id: skill
          uri: http://localhost:13000
          predicates:
            - Path=/skill
```

