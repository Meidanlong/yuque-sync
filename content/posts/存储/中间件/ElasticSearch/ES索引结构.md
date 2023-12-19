---
book_id: 28973507
cnblog_id: '17913044'
doc_id: 133753871
tags:
- 存储/中间件
- ElasticSearch
title: ES索引结构
update_time: 2023-07-20 03:48:02
---
<a name="D2GEl"></a>
# 一、术语介绍
| **术语** | **描述** | **用法** | **数据库对比概念** |
| --- | --- | --- | --- |
| 字段(Field) | 用于表述每一个列的名字，字段是文档的组成单元，包含字段名称、字段属性和字段内容 | 例如电影名称，电影评分就分别是一个字段 | 列 |
| 字段属性(Attributes) | 描述字段的属性，例如城市名的属性是一个字符串类型，不需要分词等 | 用来描述字段的，包括是否建倒排、正排、分词、值的类型(数字类型、字符串类型等) | 类似字段的Varchar(16),int(20),是否index，primary_index等 |
| 文档(document) | 文档是可搜索的结构化数据单元，用于描述一整条记录，由多个字段组成 | 例如[评分为9.7，名称为战狼2，上映时间为2017-7-27]的电影 | 记录行 |
| 索引(index) | 用于描述多个行记录的集合 | 例如把所有的电影放在一个索引里 | 表 |
| 正排 | 从文档角度看其中的词组，表示每个文档都含有哪些词组，以及每个词组出现了多少次（词频） 及其出现位置<br />id->value | 例如对于电影索引<br />doc1->id,name,pub_time… | 行记录 |
| 倒排 | 从词组角度看文档，标识每个词组分别在那些文档中出现(文档ID)，以及在各自的文档中每个单词分别出现了<br />多少次（词频）及其出现位置.<br />ES中为所有字段默认都建了倒排索引<br />value->id | 例如电影索引，评分9.7的电影有[doc1,doc2,doc3,doc4,doc5] | 类似B+树索引<br />Mysql不设置索引还是可以进行查询，但是ES不设置，查询结果为空 |
| 召回 | 通过用户查询的关键词进行分词，将分词后的词组通过查找倒排链表快速定位到文档，这个过程称为召回。 | 

 | 查询过程 |
| 召回量 | 召回得到的文档数为召回量，即totalhits | 

 | 查询返回的结果数 |
| 分片(Shard) | 一个索引由多个分片组成，这些分片是索引里面的一部分，每一个分片都具备索引相同的数据结构<br />一个分片就对应了一个lucene的索引 | 一个索引分成N个shard，每一个Shard的内容就是这个完整索内容的1/N | 在数据库里没有类似的概念 |
| 段(Segment) | 分片的组成单元，即多个段构成一个分片，段是检索的基本单元，所有的查询/更新都是基于段来查询的， | 

 | 

 |
| 段合并 | Lucene的删除是标记删除，更新是先删后增，随着数据不断的更新，一个分片中会累积很多段(这些段里存在很多已经删掉的文档)，段太多会导致查询性能变慢，因此我们需要一个段合并的过程，将那些没有用的数据清除，减少段的个数 | 

 | 

 |

<a name="Mm0N5"></a>
# 二、索引结构
<a name="WYBt5"></a>
## 1、ES索引
我们知道，每个index由若干个shard组成，以此来达到分布式可扩展的能力。比如下图是一个由10个shard组成的index。<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1689819006856-7e6e251f-e331-4a6b-ab10-c3603fc2eddd.png#averageHue=%23fbfbf8&clientId=u1617521e-7fb0-4&from=paste&height=194&id=u7afd8939&originHeight=387&originWidth=542&originalType=binary&ratio=2&rotation=0&showTitle=false&size=114024&status=done&style=none&taskId=u569aad05-9689-441b-a723-366f26705bc&title=&width=271)<br />shard是Elasticsearch数据存储的最小单位，index的存储容量为所有shard的存储容量之和。Elasticsearch集群的存储容量则为所有index存储容量之和。<br />一个es中的shard就对应了一个Lucene的索引，所以Elasticsearch索引使用的存储内容主要取决于Lucene中的数据存储。
<a name="JMDaS"></a>
## 2、Lucene索引
<a name="JyF2X"></a>
### 2.1、文件结构
Lucene的索引由许多个文件组成，这些文件放在同一个目录下<br />一个Lucene的索引由多个段(Segment)组成，段与段之间是独立的。添加新的文档时可以生成新的段，达到阈值（段的个数，段中包含的文件数等）时，不同的段可以合并<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1689819013134-b18f4b5a-952e-4a1d-bddc-5c3e702b4edc.png#averageHue=%23faf9f9&clientId=u1617521e-7fb0-4&from=paste&height=375&id=u7d42a50f&originHeight=750&originWidth=966&originalType=binary&ratio=2&rotation=0&showTitle=false&size=70430&status=done&style=none&taskId=u5a929c19-c185-4326-b9e3-fb9a1583777&title=&width=483)
<a name="qDinm"></a>
### 2.2、存储规则
Lucene为了使的信息的存储占用的**空间更小**，访问**速度更快**，采取了一些特殊的技巧<br />**postings list**<br />文档列表，作为文档的唯一标识的，ES 会对这些存入的文档进行处理，转化成一个唯一的整型 id，每个文档被分配一个唯一的 id<br />**Term Dictionary**<br />词 (Term)是索引的最小单位，是经过词法分词和语言处理后的字符串，<br />为了能快速找到某个term，将所有的term排个序，**二分法查找term**，logN的查找效率，就像通过字典查找一样，这就是**Term Dictionary（**这是第一步的加速）。和传统数据库通过B+树的方式比较类似<br />**Term Index **<br />B+树通过减少磁盘寻道次数来提高查询性能，Lucene也是采用同样的思路，直接通过内存查找term，不读磁盘，但是如果term太多，**Term Dictionary**也会很大，放内存不现实，于是有了**Term Index（**这是第二步的加速），就像字典里的索引页一样，A开头的有哪些term，分别在哪页，可以理解term index是一棵**字典树**。<br />这棵树不会包含所有的term，它包含的是term的一些**前缀**。通过term index可以快速地定位到term dictionary的某个offset，然后从这个位置再往后顺序查找。如下图：<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1689819019814-92205175-9881-4a20-b160-ebc6ff0360ca.png#averageHue=%23fbfaf7&clientId=u1617521e-7fb0-4&from=paste&height=516&id=u1cd5a3f8&originHeight=1032&originWidth=1574&originalType=binary&ratio=2&rotation=0&showTitle=false&size=488548&status=done&style=none&taskId=u2cec9313-7a83-481f-af14-22be8d78d13&title=&width=787)<br />举个栗子，比如要存储如下词:
```
term
termagancy
termagant
terminal
```
如果按照正常方式来存储，需要的空间如下：<br />**[s=4]** [t][e][r][m]<br />**[s=10] **[t][e][r][m][a][g][a][n][c][y]<br />**[s=9] **[t][e][r][m][a][g][a][n][t]<br />**[s=8] **[t][e][r][m][i][n][a][l]<br />共需要4+10+9+8+**4**=**35**个字节<br />如果应用**字典树**，需要的空间如下：<br />**[s=4]** [t][e][r][m]<br />**[s=4(offset)][s = 6]** [a][g][a][n][c][y]<br />**[s=8(offset)][s= 1]** [t]<br />**[s=4(offset)][s=4]** [i][n][a][l]<br />共需要4+6+1+4+**7**=**22**个字节。<br />大大缩小了存储空间，尤其是在按字典顺序排序的情况下，前缀的重合率大大提高。

