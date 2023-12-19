---
book_id: 28973507
cnblog_id: '17913117'
doc_id: 88486776
tags:
- 服务框架
- Spring
- 第三方
- Nacos
- Nacos
title: Nacos配置中心环境搭建
---
<a name="XYgSC"></a>
# 一、配置中心介绍
原有配置文件问题：

- 配置文件的数量会随着服务的增加池穴递增
- 单个配置文件无法区分多个运行环境
- 配置文件内容无法动态更新，需要重启服务

![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1659574308118-d3374918-3089-4812-b5e8-ccb04aa2636e.png#averageHue=%23ddd3b6&clientId=ud90a57e5-a33f-4&from=paste&height=292&id=ufe3ad5ef&originHeight=584&originWidth=1660&originalType=binary&ratio=1&rotation=0&showTitle=false&size=345336&status=done&style=none&taskId=u38145f14-39f8-40dc-a331-1d3297338ed&title=&width=830)<br />现配置中心：

- 统一的配置文件管理
- 提供统一标准接口，服务根据标准接口自行拉取配置
- 支持动态更新到所有服务

![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1659574398037-6a8359a5-2847-407c-b20e-0d6e86c38de3.png#averageHue=%23c8dbb3&clientId=ud90a57e5-a33f-4&from=paste&height=410&id=uc43894a0&originHeight=820&originWidth=930&originalType=binary&ratio=1&rotation=0&showTitle=false&size=258170&status=done&style=none&taskId=uf1e24cb1-1bfe-4945-815d-6f6289de67f&title=&width=465)
<a name="L4k9z"></a>
# 二、配置中心比较

- Appllo：携程
- Disconf：百度
- SpringCloud Config
- Nacos
<a name="doyt8"></a>
# 三、SpringBoot整合Nacos Config
<a name="AzGWN"></a>
## 1、引入依赖
```xml
<dependencies>
  <dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-nacos-config</artifactId>
  </dependency>
</dependencies>
```
<a name="xkZkP"></a>
## 2、添加配置
<a name="MXuJm"></a>
### 2.1、Nacos后台配置
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1659575423122-1d06f409-b9df-495b-8f02-36b6340121ff.png#averageHue=%23ecedef&clientId=ud90a57e5-a33f-4&from=paste&height=256&id=u5718d5b3&originHeight=512&originWidth=2546&originalType=binary&ratio=1&rotation=0&showTitle=false&size=104221&status=done&style=none&taskId=ua4601ed8-b6b8-432e-80d2-d2e96dc08c2&title=&width=1273)<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1659580635304-15f1f635-ce32-4f6b-ac61-8e626adc42ce.png#averageHue=%23929292&clientId=u56b2ba5f-5f8e-4&from=paste&height=845&id=ubbc33b90&originHeight=1690&originWidth=2200&originalType=binary&ratio=1&rotation=0&showTitle=false&size=140034&status=done&style=none&taskId=u559ee3d1-1ca8-4660-ad32-ebb2908506f&title=&width=1100)<br />**注：**

1. `Data ID`应与`spring.application.name`保持一致
2. `Data ID`+ `Group`应该保持唯一
   1. ![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1659580806220-57ae9eac-5153-4e75-bf1f-2a756dd4c5f3.png#averageHue=%23b2b1b1&clientId=u56b2ba5f-5f8e-4&from=paste&height=58&id=u3feb8dd5&originHeight=116&originWidth=654&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15548&status=done&style=none&taskId=uafc7eb80-40e9-4ec0-8f36-d09ce48a21b&title=&width=327)
<a name="hgfJw"></a>
### 2.2、SpringBoot配置
```yaml
spring:
  application:
    name: springcloud-alibaba-provider
  cloud:
    nacos:
      config:
        server-addr: localhost:8848
        file-extension: yaml
```
<a name="tyt6F"></a>
## 3、添加注解
在对应Bean中添加注解，才能动态刷新配置
```java
@RefreshScope
```

