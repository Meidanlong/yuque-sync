---
book_id: 28973507
cnblog_id: '17912140'
doc_id: 121660972
tags:
- 基础语法
- Shell
title: wget使用
---
<a name="lNzAu"></a>
## 一、常见用法
```
wget `downloadUrl`
```
<a name="eFauR"></a>
### 1、参数配置
<a name="t31IY"></a>
#### -k, --convert-links 
将绝对链接转换为相对链接。
<a name="IgKSe"></a>
#### -m 
就等价于 递归下载+除非远程文件较新，否则不再取回+最大递归深度无限+不删除“.listing”文件。
<a name="B3H5r"></a>
#### -np, --no-parent 
不搜索上层目录
<a name="IzJBc"></a>
#### -d
只是输出下载信息
<a name="c8es1"></a>
#### -q
“安静”下载
<a name="aB79P"></a>
#### -b
让wget在后台运行
<a name="z6Gzi"></a>
#### -c
断点续传
<a name="bEJRN"></a>
#### -e
代表调用.wgetrc中的代理地址
<a name="adP8o"></a>
## 二、添加代理
<a name="PdOWN"></a>
### 方式一
在用户家目录建立.wgetrc文件
```
http_proxy = http://proxy.server.com:8080/
ftp_proxy = http://proxy.server.com:8080/
--proxy-user=username
--proxy-passwd=mypasswd
```
<a name="wA9I0"></a>
### 方式二
在命令行直接使用代理
```powershell
wget -e "http_proxy=http://<ip>:<port>/" --proxy-user=usrname --proxy-passwd=passwd http://www.***.com

# https
-e "https_proxy=http://127.0.0.1:8087"
```

