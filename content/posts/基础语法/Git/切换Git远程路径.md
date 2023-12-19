---
book_id: 28973507
cnblog_id: 17912967
doc_id: 111568547
tags:
- 基础语法
- Git
title: 切换Git远程路径
---
<a name="mILxA"></a>
# 一、切换仓库地址
<a name="IUyd2"></a>
## 1、直接修改远程路径
```bash
git remote set-url origin URL
```
<a name="ye4Fj"></a>
## 2、先删除再添加
```bash
# 删除现有库
git remote rm origin
# 添加新库
git remote add origin url
```
<a name="FVRIO"></a>
# 二、查看远程仓库地址
```bash
git remote -v
```

