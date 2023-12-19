---
book_id: 28973507
cnblog_id: '17913030'
doc_id: 106035952
tags:
- 云容器化
- Docker
- Docker 安装
title: Docker配置XXL-JOB及其使用
---
<a name="IAOeZ"></a>
# 一、下载XXL-JOB镜像
```shell
# Docker地址：https://hub.docker.com/r/xuxueli/xxl-job-admin/     (建议指定版本号)
docker pull xuxueli/xxl-job-admin
```
<a name="IW8EZ"></a>
# 二、运行容器
```shell
docker run -e PARAMS="--spring.datasource.url=jdbc:mysql://172.17.0.3:3306/xxl_job?useUnicode=true&characterEncoding=UTF-8&autoReconnect=true&serverTimezone=Asia/Shanghai --spring.datasource.username=root --spring.datasource.password=meisql --xxl.job.accessToken=wtjc" -p 19999:8080 -v wtjobcentervolume:/data/applogs --name wtjobcenter -it xuxueli/xxl-job-admin:2.3.1
```
:::warning
⚠️ 注意<br />MySQL的ip为 `docker inpect mymysql` 的`IPAdress`<br />详见[Docker安装Nacos](https://www.yuque.com/meidanlong/tzty91/wcuih0?view=doc_embed)
:::

---

**参考**<br />[分布式开发6大核心专题 掌握企业级分布式项目方案](https://coding.imooc.com/class/453.html)

