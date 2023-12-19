---
book_id: 28973507
cnblog_id: '17913043'
doc_id: 133772086
tags:
- 存储/中间件
- ElasticSearch
title: ES读写原理
update_time: 2023-07-20 03:47:51
---
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1689819056218-49b62a8f-b405-4e77-a89c-468c2a013901.png#averageHue=%23e9e9e9&clientId=u1617521e-7fb0-4&from=paste&height=780&id=ue8faa8aa&originHeight=1560&originWidth=2584&originalType=binary&ratio=2&rotation=0&showTitle=false&size=478834&status=done&style=none&taskId=uc884b85d-42ed-49c8-9c40-6f936b8c43a&title=&width=1292)
<a name="aJqEj"></a>
## **一、写数据**
<a name="cujrd"></a>
### segment file(磁盘文件)
存储倒排索引的文件，每个segment本质上就是一个倒排索引，每秒都会生成一个segment文件，当文件过多时es会自动进行segment merge（合并文件），合并时会同时将已经标注删除的文档物理删除
<a name="rIfOY"></a>
### commit point(磁盘文件)
记录当前所有可用的segment，每个commit point都会维护一个.del文件，即每个.del文件都有一个commit point文件（es删除数据本质是不属于物理删除），当es做删改操作时首先会在.del文件中声明某个document已经被删除，文件内记录了在某个segment内某个文档已经被删除，当查询请求过来时在segment中被删除的文件是能够查出来的，但是当返回结果时会根据commit point维护的那个.del文件把已经删除的文档过滤掉
<a name="xxNc2"></a>
### translog日志文件(磁盘文件)
为了防止elasticsearch宕机造成数据丢失保证可靠存储，es会将每次写入数据同时写到translog日志中
<a name="DxK9p"></a>
### os cache
操作系统里面，磁盘文件其实都有一个东西，叫做os cache，操作系统缓存，就是说数据写入磁盘文件之前，会先进入os cache，先进入操作系统级别的一个内存缓存中去
<a name="clp19"></a>
### 写数据的流程
客户端通过路由节点到达指定的shard分片，也就是Lucene的index

1. 数据首先写被入es的jvm内存中，此时数据对外不可见.
2. 默认每隔1s将jvm的数据写入到底层Lucene的**os cache**中，一旦写入到**os cache**中数据即可查询出来.所以es可以做到近实时的搜索.
3. 默认每隔30分钟将数据从**os cache**中flush到磁盘上,成为一个个的**segment file**
4. 为了防止如果节点宕机数据丢失，会写translog，也是先写到**os cache**中的，默认每隔5s中生成**translog**日志持久化到磁盘上,用于节点重启的时候进行数据恢复使用(可以理解成mysql中的binlog)
5. **translog**文件是会不断变大的，当到达一定值的时候就会触发commit操作，生成**commit point**磁盘文件，将**os cache**数据强制刷入磁盘，再清空**translog**文件
6. **主分片**写入成功后会同步到其他的**副本分片**去.
7. 当**主分片**和**副本分片**节点都写完后，协调节点会返回给客户端数据写入成功的响应
8. es会定期进行merge操作，进行**segment file**的合并,当进行segment 合并的时候会将标记删除的文件进行物理删除操作.
<a name="rPjOh"></a>
## **二、读数据**

1. 客户端发送请求到一个协调节点(随意选择的)
2. 协调节点将搜索请求转发到所有的shard对应的**主分片，**或**副本分片**也可以
3. query phase：每个shard将自己的搜索结果（其实就是一些doc id），返回给协调节点，由协调节点进行数据的合并、排序、分页等操作，产出最终结果
4. fetch phase：接着由协调节点，根据doc id去各个节点上拉取实际的document数据，最终返回给客户端。

