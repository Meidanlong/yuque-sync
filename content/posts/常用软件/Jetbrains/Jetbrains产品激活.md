---
book_id: 28973507
cnblog_id: '17913068'
doc_id: 119281783
tags:
- 常用软件
- Jetbrains
title: Jetbrains产品激活
---
<a name="33564301"></a>
## 方式一：激活码激活
- 对应网址公众号申请：

[IDEA激活码](https://idea.medeming.com/)
<a name="0d293355"></a>
## 方式二：授权服务器激活
<a name="895ecafb"></a>
### 1、登录censys
[Censys Search](https://search.censys.io/)

![56bb582479e68fbaafff3ebde3db436c.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1679623351468-10f1d063-9363-434b-9cbf-0ed750734a6f.png#averageHue=%23f1f3f7&clientId=u5ad93e80-2ae5-4&from=paste&height=410&id=ub365c09f&originHeight=820&originWidth=1554&originalType=binary&ratio=2&rotation=0&showTitle=false&size=103467&status=done&style=none&taskId=u18021ca3-10c2-44f3-ad97-f1bd7efcfaa&title=&width=777)
<a name="49985e08"></a>
### 2、输入命令
搜索框内输入以下命令，并点击“搜索”
```shell
services.http.response.headers.location: account.jetbrains.com/fls-auth
```
![bcd007398788ee96e2db3a88c5e07d43.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1679623394179-82b229b5-d97c-43df-b706-dc194c008ae0.png#averageHue=%23fdfdfd&clientId=u5ad93e80-2ae5-4&from=paste&height=709&id=u14f07303&originHeight=1418&originWidth=2152&originalType=binary&ratio=2&rotation=0&showTitle=false&size=317401&status=done&style=none&taskId=u561ae530-0f02-4771-8b95-c2417d71f6e&title=&width=1076)
<a name="f27a613a"></a>
### 3、查找ip
出现了很多对应跳转到 **jetbrains** 的服务器IP和网址,我们随便点击一个看下状态是不是 **302** 只有 **302** 的才能 **正常使用**<br />![7873112ecf656482825bb2e3b4bc84b8.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1679623412306-0234144b-25d0-4674-a54e-498fb7788742.png#averageHue=%23fcfbfb&clientId=u5ad93e80-2ae5-4&from=paste&height=614&id=u0fbb7cf8&originHeight=1228&originWidth=1788&originalType=binary&ratio=2&rotation=0&showTitle=false&size=189166&status=done&style=none&taskId=u5715ae52-07b6-4d81-8648-a6c51859c40&title=&width=894)
<a name="3580e066"></a>
### 4、复制到 **License server**
![2f0aab0bca1b69de770cd6d9cd098fd6.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1679623421427-d7a26852-3946-4438-b1c3-56331930e437.png#averageHue=%233d4247&clientId=u5ad93e80-2ae5-4&from=paste&height=480&id=ufb61cdc4&originHeight=960&originWidth=1600&originalType=binary&ratio=2&rotation=0&showTitle=false&size=79041&status=done&style=none&taskId=u91c62973-6ace-4db0-a8d7-68c88fe4fa0&title=&width=800)

---

<a name="puoaR"></a>
## 参考
[最新jetbrains全家桶及phpstorm激活方法支持全系列全版本支持更新永久有效 - lmcc-老马吃草的博客](https://www.lmcc.top/articles/485.html#%E6%9C%80%E6%96%B0jetbrains%E5%85%A8%E5%AE%B6%E6%A1%B6%E6%BF%80%E6%B4%BB%E6%96%B9%E6%B3%95)

