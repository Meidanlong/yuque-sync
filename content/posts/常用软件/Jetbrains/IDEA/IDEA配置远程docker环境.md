---
book_id: 28973507
cnblog_id: '17913065'
doc_id: 136050134
tags:
- 常用软件
- Jetbrains
- IDEA
title: IDEA配置远程docker环境
update_time: 2023-11-03 07:54:55
---
[Docker开启远程安全访问-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/1657953)
```shell
mkdir -p /usr/local/ca
cd /usr/local/ca

# 假设docker服务器ip为82.156.216.00
openssl req -subj "/CN=82.156.216.00" -sha256 -new -key server-key.pem -out server.csr

echo subjectAltName = IP:82.156.216.00,IP:0.0.0.0 >> extfile.cnf
```
```shell
sz /usr/local/ca/ca-key.pem /usr/local/ca/ca.pem /usr/local/ca/cert.pem /usr/local/ca/key.pem 
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1691850808625-3a02b17e-5e06-4911-87db-e9c0b62bdf63.png#averageHue=%232d3033&clientId=u99b5b42b-e85d-4&from=paste&height=616&id=ub0b783fa&originHeight=1232&originWidth=1362&originalType=binary&ratio=2&rotation=0&showTitle=false&size=104556&status=done&style=none&taskId=u77d98890-da37-4072-b3f1-0b64b07473b&title=&width=681)

