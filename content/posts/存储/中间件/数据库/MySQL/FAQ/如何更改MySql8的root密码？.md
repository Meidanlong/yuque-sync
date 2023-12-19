---
book_id: 28973507
cnblog_id: '17913058'
doc_id: 123726207
tags:
- 存储/中间件
- 数据库
- MySQL
- FAQ
title: 如何更改MySql8的root密码？
---
<a name="QDMld"></a>
## 一、登陆MySql
```shell
# 登陆mysql
mysql -u root -p mysql

#如果是通过docker
docker exec -it mymysql mysql -u root -p mysql
```
<a name="xFxlU"></a>
## 二、更换新密码
```bash
# set password for root@localhost = password('xxx');

# mysqladmin -uroot -pxxx password 123456
```
```sql
-- 选择数据库
-- use mysql;
-- 更新密码
alter user 'root'@'localhost' identified with mysql_native_password by 'newPassword';
-- 刷新权限
flush privileges;
```

