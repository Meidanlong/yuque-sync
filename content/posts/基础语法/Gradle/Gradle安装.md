---
book_id: 28973507
cnblog_id: '17912942'
doc_id: 149922420
tags:
- 基础语法
- Gradle
title: Gradle安装
update_time: 2023-12-12 06:07:19
---
[官方安装文档](https://gradle.org/install/)
<a name="R3j75"></a>
# 一、下载
下载地址：[release note](https://gradle.org/releases/)
<a name="OUqA6"></a>
# 二、配置镜像仓库
在`init.d`目录下新建`init.gradle`文件，并配置以下信息
```
allprojects {
    repositories {
        mavenLocal()
        maven { name "Alibaba" ; url "https://maven.aliyun.com/repository/public" }
        maven { name "Bstek" ; url "https://nexus.bsdn.org/content/groups/public/" }
        mavenCentral()
    }
 
    buildscript { 
        repositories { 
            maven { name "Alibaba" ; url 'https://maven.aliyun.com/repository/public' }
            maven { name "Bstek" ; url 'https://nexus.bsdn.org/content/groups/public/' }
            maven { name "M2" ; url 'https://plugins.gradle.org/m2/' }
        }
    }
}
```
<a name="exy4y"></a>
# 三、配置环境变量
```bash
# 配置下载软件根目录
#SOFTWARE_PATH=

# GRADLE
# 指定路径，我将解压后的文件重命名为版本号8.5，以实际路径为准
GRADLE_HOME=$SOFTWARE_PATH/gradle/8.5
PATH=$PATH:$GRADLE_HOME/bin
export GRADLE_HOME PATH
```
```bash
source ./zshrc
```
<a name="bPe2B"></a>
# 四、检查
```bash
gradle -version
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1702354554358-5cd2d210-2a6f-4dba-b12b-6e478f2c1cac.png#averageHue=%23070707&clientId=uf4663789-eaa8-4&from=paste&height=248&id=u69e35dce&originHeight=496&originWidth=1052&originalType=binary&ratio=2&rotation=0&showTitle=false&size=60207&status=done&style=none&taskId=ua87866f6-486a-4498-8418-e71a014102f&title=&width=526)

