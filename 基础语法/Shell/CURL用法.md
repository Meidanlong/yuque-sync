---
book_id: 28973507
cnblog_id: '17912137'
doc_id: 131615406
tags:
- 基础语法
- Shell
title: CURL用法
---
`curl`是一个常用的命令行工具，用于获取或发送数据，支持多种协议，如HTTP、HTTPS、FTP等。以下是使用`curl`的例子：
<a name="PSgNY"></a>
# 获取网页内容：
```
curl https://www.example.com
```
这个命令会将`https://www.example.com`的HTML源码打印到控制台。
<a name="anHuA"></a>
# 发送POST请求：
```
curl -d "param1=value1&param2=value2" -X POST http://localhost:3000/data
```
这个命令会向`http://localhost:3000/data`发送一个POST请求，数据为`param1=value1&param2=value2`。
<a name="Q5Ui8"></a>
# 下载文件：
```bash
curl -O https://github.com/osmr/deepspeech_features/releases/download/v0.0.1/deepspeech-0_1_0-b90017e8.pb.zip
```
<a name="ydbpq"></a>
# 其他参数
一些重要的`curl`参数包括：

- `-d` 或 `--data`：发送POST请求的数据；
- `-X`：指定HTTP请求的方法；
- `-H` 或 `--header`：添加HTTP请求的头部信息；
- `-o` 或 `--output`：将输出写入到文件中，而不是打印到控制台；
- `-I` 或 `--head`：仅获取HTTP头部信息；
- `-u` 或 `--user`：设置服务器验证用户和密码。

