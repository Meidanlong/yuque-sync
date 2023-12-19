---
book_id: 28973507
cnblog_id: '17913123'
doc_id: 88481944
tags:
- 服务框架
- Spring
- 第三方
- Nacos
- FAQ
title: Nacos配置：发布失败，请检查参数是否正确
---
<a name="h9w1R"></a>
## 一、表象：
<a name="EHgyA"></a>
#### 页面1：
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1659579789334-b55a5d09-12d2-4f59-a11f-85632521a3b8.png#averageHue=%23fecec0&clientId=u381807a2-b113-4&from=paste&height=642&id=u26a7aed0&originHeight=1284&originWidth=2544&originalType=binary&ratio=1&rotation=0&showTitle=false&size=314694&status=done&style=none&taskId=u72d5b648-0321-4c00-b790-9070d1521b0&title=&width=1272)
<a name="NKXPw"></a>
#### 报错1：
> caused: PreparedStatementCallback; bad SQL grammar [SELECT id,data_id,group_id,tenant_id,app_name,content,md5,gmt_create,gmt_modified,src_user,src_ip,c_desc,c_use,effect,type,c_schema,encrypted_data_key FROM config_info WHERE data_id=? AND group_id=? AND tenant_id=?]; nested exception is java.sql.SQLSyntaxErrorException: Unknown column 'encrypted_data_key' in 'field list';caused: Unknown column 'encrypted_data_key' in 'field list';

<a name="A9YI3"></a>
#### 页面2:
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1659579898373-9ab1bc16-e5b2-4618-9129-65cf5ecb8084.png#averageHue=%23f87d61&clientId=u381807a2-b113-4&from=paste&height=632&id=uf3ece531&originHeight=1264&originWidth=2534&originalType=binary&ratio=1&rotation=0&showTitle=false&size=293710&status=done&style=none&taskId=u78df2c6a-a9d1-4bef-9960-b4cf9a44438&title=&width=1267)
<a name="pudWi"></a>
#### 报错2:
> caused: PreparedStatementCallback; bad SQL grammar [INSERT INTO his_config_info (id,data_id,group_id,tenant_id,app_name,content,md5,src_ip,src_user,gmt_modified,op_type,encrypted_data_key) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)]; nested exception is java.sql.SQLSyntaxErrorException: Unknown column 'encrypted_data_key' in 'field list';caused: Unknown column 'encrypted_data_key' in 'field list';

<a name="v2oHR"></a>
## 二、分析
<a name="c7tln"></a>
### 1、相关版本
| 服务 | 版本 |
| --- | --- |
| Nacos Server | 2.1.0 |
| Mysql | 8.0.29 |

查询相关文档，建议：
> Nacos Server 1.4.0以下使用的Mysql驱动是8.0以下的，1.4.0以上使用的驱动就是8.0以上的

该报错与版本无关
<a name="KLYaq"></a>
### 2、官方文档
建表SQL语句应查看对应`Nacos Server`的`tag`版本，我用的是`1.4.0`的SQL所以产生问题。`2.1.0`可参考：[nacos-db-2-1-0.sql](https://github.com/alibaba/nacos/blob/2.1.0/config/src/main/resources/META-INF/nacos-db.sql)<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1659663724395-58012b01-7fa6-4f9d-96d0-31bd0d65bb16.png#averageHue=%23b95f48&clientId=u07be0623-fa72-4&from=paste&height=778&id=ue8633bd6&originHeight=1556&originWidth=3506&originalType=binary&ratio=1&rotation=0&showTitle=false&size=438481&status=done&style=none&taskId=u218dc541-78d7-49f2-ba4b-070882a49f1&title=&width=1753)
<a name="La6BA"></a>
## 三、解决
按照官方文档重新建表，或直接补全列：
```sql
-- config_info 表
alter table config_info add encrypted_data_key varchar(255);

-- his_config_info 表
alter table his_config_info add encrypted_data_key varchar(255);
```
<a name="xb8Hv"></a>
## 四、结果
再次重试成功：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1659580407723-394f5a68-9c10-47a0-8e93-f14ae8158555.png#averageHue=%23f7ded8&clientId=udb265c69-5f32-4&from=paste&height=589&id=u1626150a&originHeight=1178&originWidth=2550&originalType=binary&ratio=1&rotation=0&showTitle=false&size=270755&status=done&style=none&taskId=u3e9a7d3f-30e9-4893-a2e6-3200df3d529&title=&width=1275)

