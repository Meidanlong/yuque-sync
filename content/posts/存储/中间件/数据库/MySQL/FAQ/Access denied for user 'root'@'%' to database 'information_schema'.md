---
book_id: 28973507
cnblog_id: '17913059'
doc_id: 123726010
tags:
- 存储/中间件
- 数据库
- MySQL
- FAQ
title: Access denied for user 'root'@'%' to database 'information_schema'
---
<a name="zNAel"></a>
## 原因
`information_schema`是一个虚拟的数据库，里面的表其实都是视图。应切换数据库为“真正的数据库”
<a name="ZPR5X"></a>
## 解决
```plsql
USE `THE-REAL-DATABASE`;
```

---


