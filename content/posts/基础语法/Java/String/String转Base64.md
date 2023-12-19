---
book_id: 28973507
cnblog_id: '17913020'
doc_id: 132186252
tags:
- 基础语法
- Java
- String
title: String转Base64
---
```java
public String decoder(String endcoderStr) throws IOException {
    return Base64.getEncoder().encodeToString(endcoderStr.getBytes("utf-8")).replaceAll("\\+","-").replaceAll("/", "_").replaceAll("=", Strings.EMPTY);
}
```
[什么是 URL 安全的 BASE64 编码？-腾讯云](https://cloud.tencent.com.cn/document/product/460/86595#1b54a43c-d985-441d-9c89-81ac6c4adc39)

