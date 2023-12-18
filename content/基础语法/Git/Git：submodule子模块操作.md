---
book_id: 28973507
cnblog_id: '17912491'
doc_id: 147959807
tags:
- 基础语法
- Git
title: Git：submodule子模块操作
update_time: 2023-12-13 01:59:10
---
<a name="bSBfX"></a>
# 一、子模块添加
```bash
git submodule add <url> <path>

git submodule add https://github.com/../.git themes/MeiFixIt
```
<a name="sMN9g"></a>
# 二、子模块更新
```bash
git submodule update --remote --merge
```
<a name="kunHN"></a>
# 三、下载子模块
同父模块一起下载子模块
```bash
git clone --recurse-submodules <repository-url>
```
父模块下载完成，再下载子模块
```bash
git submodule update --init --recursive
```
如果子模块下载不下来或者下载缓慢可以将`.gitmodules`文件中的`url`切换成`SSH`连接<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1701250794193-ae24b5e6-c0fb-4c24-b835-d5210453eaa2.png#averageHue=%23efefef&clientId=u3fa76f58-5a5a-4&from=paste&height=83&id=u01207b0f&originHeight=166&originWidth=780&originalType=binary&ratio=2&rotation=0&showTitle=false&size=31225&status=done&style=none&taskId=u652536e4-1de7-4cc9-9f5f-1b5a38e5294&title=&width=390)
<a name="cENxp"></a>
# 四、删除子模块

1. `rm -rf 子模块目录` 删除子模块目录及源码
2. `vi .gitmodules` 删除项目目录下.gitmodules文件中子模块相关条目
3. `vi .git/config` 删除配置项中子模块相关条目
4. `rm .git/modules/*` 删除模块下的子模块目录，每个子模块对应一个目录，注意只删除对应的子模块目录即可

---

**参考**

- [git中submodule子模块的添加、使用和删除_git add submodule-CSDN博客](https://blog.csdn.net/guotianqing/article/details/82391665)

