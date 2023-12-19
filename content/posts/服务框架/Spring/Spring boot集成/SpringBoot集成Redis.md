---
book_id: 28973507
cnblog_id: '17913107'
doc_id: 84159917
tags:
- 服务框架
- Spring
- Spring boot集成
title: SpringBoot集成Redis
---
<a name="JQlye"></a>
# 一、单体模式
<a name="grggH"></a>
## 1、引入依赖
```xml
<!-- 引入 redis 依赖 -->
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>
```
<a name="LBB0l"></a>
## 2、配置Redis
```yaml
spring:
  redis:
    database: 1
    host: 192.168.1.191
    port: 6379
    password: imooc
```
<a name="rylkm"></a>
## 3、使用
```java
@Autowired
private RedisTemplate redisTemplate;

redisTemplate.opsForValue().set(key, value);

(String)redisTemplate.opsForValue().get(key);

redisTemplate.delete(key);
```
<a name="UjVg4"></a>
# 二、集群模式

---

**参考**<br />[Java架构师-技术专家](https://class.imooc.com/sale/javaarchitect)

