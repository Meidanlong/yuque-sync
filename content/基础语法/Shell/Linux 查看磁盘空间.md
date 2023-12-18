---
book_id: 28973507
cnblog_id: 17912132
doc_id: 147802904
tags:
- 基础语法
- Shell
title: Linux 查看磁盘空间
update_time: 2023-11-23 11:07:07
---
<a name="ZLs9w"></a>
# 一、查看文件系统使用率
```bash
df -h
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1700634944995-10edab13-fe9e-44bd-a956-c429e5d5624b.png#averageHue=%230e0e0e&clientId=u35c999ac-5341-4&from=paste&height=137&id=ua2630c5d&originHeight=274&originWidth=740&originalType=binary&ratio=2&rotation=0&showTitle=false&size=50282&status=done&style=none&taskId=u98ac6333-2781-4997-a1f6-2797f20896b&title=&width=370)
<a name="P8UZE"></a>
# 二、查看目录下文件大小
```bash
du -sh *

# 包含隐藏目录
du -sh .[^.]* * |sort -h
```

