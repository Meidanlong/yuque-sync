---
book_id: 28973507
cnblog_id: '17913122'
doc_id: 88486369
tags:
- 服务框架
- Spring
- 第三方
- Nacos
- Nacos
title: Nacos注册中心环境搭建
---
<a name="RrQWh"></a>
# 一、版本
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1659498730509-5aef14cb-87cb-4c10-967f-14fe7fec3160.png#clientId=u195c99de-58c8-4&from=paste&height=44&id=u875f8092&originHeight=88&originWidth=500&originalType=binary&ratio=1&rotation=0&showTitle=false&size=23911&status=done&style=none&taskId=u83281565-a032-4767-945a-5216f187eca&title=&width=250)
<a name="ZxCyH"></a>
# 二、集成三板斧
<a name="Ktj6Z"></a>
## 1、依赖
```xml
<properties>
  <maven.compiler.source>8</maven.compiler.source>
  <maven.compiler.target>8</maven.compiler.target>
  
  <springboot.version>2.3.2.RELEASE</springboot.version>
  <springcloud-alibaba.version>2.2.5.RELEASE</springcloud-alibaba.version>
</properties>

<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-parent</artifactId>
      <version>${springboot.version}</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
    <dependency>
      <groupId>com.alibaba.cloud</groupId>
      <artifactId>spring-cloud-alibaba-dependencies</artifactId>
      <version>${springcloud-alibaba.version}</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>

<dependencies>
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
  </dependency>
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
  </dependency>
  <dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
  </dependency>
</dependencies>
```
<a name="UjBIX"></a>
## 2、配置
```yaml
server:
  port: 8000
spring:
  cloud:
    nacos:
      discovery:
        service: serv
      server-addr: 82.156.216.48:8848
```
<a name="Ge8pd"></a>
## 3、注解
```java
@EnableDiscoveryClient
```
<a name="t6Jb0"></a>
# <br />

