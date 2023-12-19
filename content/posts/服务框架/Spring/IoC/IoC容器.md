---
book_id: 28973507
cnblog_id: '17913114'
doc_id: 105507790
tags:
- 服务框架
- Spring
- IoC
title: IoC容器
---
<a name="HP92n"></a>
# 一、设计
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1667954109923-0f297232-94dc-4b70-b73c-0a3966fb6bca.png#averageHue=%23faeddf&clientId=u1d5917dd-328c-4&from=paste&height=401&id=ubbbec9c4&originHeight=802&originWidth=1648&originalType=binary&ratio=1&rotation=0&showTitle=false&size=538554&status=done&style=none&taskId=u40d7ea6d-558d-434f-a171-baaa47149d0&title=&width=824)<br />**框架最基本功能：**

1. 解析配置
2. 定位与注册对象
3. 注入对象
4. 提供通用工具类
<a name="XAC49"></a>
# 二、IoC容器的实现
**需要实现的点：**

1. 创建注解
2. 提取标记对象
3. 实现容器
4. 依赖注入
<a name="QlLlU"></a>
## 2、提取标记对象

1. 指定范围，获取范围内的所有类
2. 遍历所有类，获取被注解标记的类并加载进容器里

`**extractPacakgeClass**`**里面需要完成的事情：**

1. 获取到类的加载器
2. 通过类加载器获取到加载的资源信息
3. 依据不同的资源类型，采用不容的方式获取资源的集合

**为什么不让用户传入绝对路径：**

1. 不够友好：不同机器之间的路径肯跟不相同
2. 如果打的是war包或者jar包，根本找不到路径
3. 因此通用的做法是通过项目的类加载器来获取
<a name="QYt3M"></a>
### 2.1、类加载器ClassLoader

- 根据一个指定的类的名称，找到获取生成其对应的字节码
- 加载Java应用所需的资源

![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1667955568153-2b9ba00e-621b-4b3c-a052-ff997900ca81.png#averageHue=%23b5e82d&clientId=u1d5917dd-328c-4&from=paste&height=284&id=ub0ffe0d7&originHeight=568&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=200434&status=done&style=none&taskId=uee4fd059-9e42-4a1d-babe-669a45c9b16&title=&width=540)<br />**获取类加载器的方法：**
```java
Thread.currentThread().getContextClassLoader();
```
**统一资源定位符URL：**<br />某个资源的唯一地址

- 通过获取java.net.URL实例获取协议名、资源名、路径等信息

![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1667956085498-d939a46d-4d93-40ee-b560-e84ff711cef7.png#averageHue=%23f5f5f5&clientId=u1d5917dd-328c-4&from=paste&height=238&id=uc931004c&originHeight=476&originWidth=1892&originalType=binary&ratio=1&rotation=0&showTitle=false&size=206628&status=done&style=none&taskId=ue067d115-dff5-4c4a-9f83-0c49faa2f6a&title=&width=946)
<a name="xouPl"></a>
# 三、单例模式 Singleton Pattern
确保一个类只有一个实例，并对外提供统一访问方式

- 饿汉模式：类被加载的时候就立即初始化并创建唯一实例
- 懒汉模式：在被客户端首次调用的时候才会创建唯一实例
   - 加入双重检查锁机制的懒汉模式能够确保线程安全
- 装备了枚举的饿汉模式能够抵御反射与序列化的进攻，满足容器需求
<a name="uEngl"></a>
## 1、枚举保证无视反射和序列化攻击的单例
枚举也是饿汉模式<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1668340916095-dd2923bd-c43e-46af-9a06-b7ed146873cd.png#averageHue=%23f5f5f3&clientId=u41df7ad3-5d66-4&from=paste&height=336&id=u117ec49e&originHeight=672&originWidth=902&originalType=binary&ratio=1&rotation=0&showTitle=false&size=284899&status=done&style=none&taskId=uff0f8779-91f8-4ae8-a88f-5e05cbca49b&title=&width=451)<br />**问题：**<br />**枚举如何抵挡序列化和反序列化攻击？**<br />线索：ObjectInputStream的readObject源码
<a name="K9967"></a>
# 四、容器的载体及容器的加载
<a name="LF1O1"></a>
## 1、获取单例Bean实例
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1668387869539-e916f79a-a542-4781-ada6-1fbac62ded70.png#averageHue=%23f8f7f6&clientId=u21ea494a-fc0a-4&from=paste&height=528&id=u8af7e741&originHeight=1056&originWidth=1036&originalType=binary&ratio=1&rotation=0&showTitle=false&size=379861&status=done&style=none&taskId=ua7cba97e-6447-4f0f-a71a-90c2e79f112&title=&width=518)
<a name="iNi7z"></a>
## 2、实现容器
<a name="e8nPq"></a>
### 2.1、容器的组成部分

- 保存Class对象及其实例的载体
- 容器的加载
- 容器的操作方式
<a name="BvqYw"></a>
### 2.2、实现容器的加载

- 配置的管理与获取
- 获取指定范围内的Class对象
- 依据配置提取Class对象，连同实例一并存入容器
<a name="Unumr"></a>
### 2.3、实现容器的操作方式
涉及到容器的增删改查

- 增加、删除操作
- 根据Class获取对应实例
- 获取所有Class和实例
- 通过注解来获取被注解标注的Class
- 通过超类获取对应的子类Class
- 获取容器载体保存的Class的数量
<a name="XFfNQ"></a>
### 2.4、作用域

- singleton
- prototype
- request
- session
- globalsession
<a name="Bprgr"></a>
## 3、实现容器的依赖注入
目前容器里面管理的Bean实例仍可能是不完备的

- 实例里面某些必须的成员变量还没有创建出来

**实现思路：**

1. 定影相关的注解标签
2. 实现创建被标注的成员变量实例，并将其注入到成员变量里
3. 依赖注入的使用

**doIoc():**

1. 遍历Bean容器中所有的Class对象
2. 遍历Class兑现所有的成员变量
3. 找出被Autowired标记的成员变量
4. 获取这些成员变量类型
5. 获取这些成员变量的类型在容器里对应的实例
6. 通过反射将对应的成员变量实例注入到成员变量所在类的实例里

