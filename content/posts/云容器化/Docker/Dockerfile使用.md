---
book_id: 28973507
cnblog_id: '17913036'
doc_id: 111467525
tags:
- 云容器化
- Docker
title: Dockerfile使用
---
<a name="hBCcN"></a>
# 一、建立Dockerfile
在项目根目录下建立Dockerfile
```dockerfile
# 如找不到镜像可使用 openjdk:8
FROM java:8-alpine 
MAINTAINER "wtrue"
ADD rical.backend.provider-1.0.0-SNAPSHOT.jar app.jar
EXPOSE 10000
ENTRYPOINT ["java", "-jar", "app.jar"]
```
二、项目打包<br />1、Maven打包
```bash
mvn clean install package -P prod
```
2、上传Dockerfile和jar包<br />2.1、找到对应打包路径
```bash
cd xxx/target
```
三、上传文件<br />1、建立docker卷
```bash
# 建立docker卷
docker volume create backendvolume
# 查询卷地址
docker inspect backendvolume
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1673334351174-5dd8c76e-69c4-4b08-906b-af814796f0fb.png#averageHue=%23181b25&clientId=ua960e5eb-8181-4&from=paste&height=214&id=u3b106241&originHeight=428&originWidth=1294&originalType=binary&ratio=1&rotation=0&showTitle=false&size=63222&status=done&style=none&taskId=u41f9475e-806e-4f1c-b402-f76df726aaa&title=&width=647)<br />2、将Dockerfile和jar包上传到对应路径<br />四、运行容器<br />1、创建镜像<br />Dockerfile目录执行
```bash
# docker stop wtbackend && docker rm wtbackend && docker rmi wtbackendimage

docker build -t wtbackendimage \
/var/lib/docker/volumes/backendvolume/_data/.

```
2、创建容器并执行
```bash
docker run -it \
-p 10000:10000 \
--net wtnet \
--name wtbackend \
--ip 172.18.3.x \ # 未指定子网段不能指定IP --subnet 172.18.0.0/16
wtbackendimage
```

