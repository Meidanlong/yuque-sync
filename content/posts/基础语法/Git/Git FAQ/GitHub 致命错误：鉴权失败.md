---
book_id: 28973507
cnblog_id: 17912966
doc_id: 131668907
tags:
- 基础语法
- Git
- Git FAQ
title: GitHub 致命错误：鉴权失败
---
<a name="ND12r"></a>
## 一、现象
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1687963067739-97e3ea13-2e04-4589-98b1-239cad138b0e.png#averageHue=%2323262c&clientId=u66223337-9405-4&from=paste&height=120&id=ud5219d0d&originHeight=264&originWidth=3192&originalType=binary&ratio=2.200000047683716&rotation=0&showTitle=false&size=82230&status=done&style=none&taskId=uca5cd8cd-27f1-4f72-839a-fc913607eb5&title=&width=1450.909059461484)
<a name="L9Ef0"></a>
## 二、解决
```powershell
git remote set-url origin https://token@github.com/Meidanlong/all-in-one.git

git push
```

