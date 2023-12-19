---
book_id: 28973507
cnblog_id: '17913042'
doc_id: 133754576
tags:
- 存储/中间件
- ElasticSearch
title: ES聚合查询
update_time: 2023-08-01 07:50:45
---
<a name="hHBBw"></a>
## 一、ES聚合查询简介
<a name="OE4mB"></a>
### 1、ES聚合查询是什么？
聚合查询是数据库中重要的功能特性，完成对一个查询的数据集中数据的聚合计算，如：找出某字段（或计算表达式的结果）的最大值、最小值，计算和、平均值等。ES作为搜索引擎兼数据库，同样提供了强大的聚合分析能力。<br />对一个数据集求最大、最小、和、平均值等指标的聚合，在ES中称为**指标聚合**<br />而关系型数据库中除了有聚合函数外，还可以对查询出的数据进行分组group by，再在组上进行指标聚合。在 ES 中group by 称为**分桶**，**桶聚合**
<a name="UAE6w"></a>
### 2、ES聚合查询的写法
在查询请求体中以aggregations节点按如下语法定义聚合查询：
```json
"aggregations" : {
    "<aggregation_name>" : { <!--聚合的名字 -->
        "<aggregation_type>" : { <!--聚合的类型 -->
            <aggregation_body> <!--聚合体：对哪些字段进行聚合 -->
        }
        [,"meta" : {  [<meta_data_body>] } ]? <!--元 -->
        [,"aggregations" : { [<sub_aggregation>]+ } ]? <!--在聚合里面在定义子聚合 -->
    }
    [,"<aggregation_name_2>" : { ... } ]*<!--聚合的名字 -->
}
```
备注：**aggregations 也可简写为 aggs**
> DSL，全称Domain Specific Language，即领域特定语言。
> 这是一种为特定问题领域定制的计算机语言，其设计目的是解决特定领域的问题，比如SQL就是一种用于处理数据库查询的DSL。DSL语句就是用这种领域特定语言编写的代码或指令。

<a name="JZ6mI"></a>
### 3、聚合查询的值来源
聚合计算的值可以取**字段的值**，也可是**脚本计算的结果**。
<a name="an3wL"></a>
## 二、指标聚合
<a name="g5vbp"></a>
### 1、max min sum avg
<a name="ZHj2l"></a>
#### 示例1：查询最大的电影id
```json
{
  "size": 0,
  "aggs": {
    "max_movie_id": {
      "max": {
        "field": "movie_id"
      }
    }
  }
}
```
查询结果1：其中aggregations.max_movie_id.value代表的就是查询结果
```json
{
  "took": 202,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 222,
      "relation": "gte"
    },
    "max_score": null,
    "hits": []
  },
  "aggregations": {
    "max_movie_id": {
      "value": 111
    }
  }
}
```
<a name="R9xfz"></a>
#### 示例2：查询未删除电影的平均评分
```json
{
  "query": {
    "match": {
      "status": 1
    }
  },
  "size": 0,
  "aggs": {
    "avg_score": {
      "avg": {
        "field": "score"
      }
    }
  }
}
```
查询结果2：其中aggregations.avg_score.value代表的就是查询结果，为0.111
```json
{
  "took": 173,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 222,
      "relation": "gte"
    },
    "max_score": null,
    "hits": []
  },
  "aggregations": {
    "avg_score": {
      "value": "0.111"
    }
  }
}
```
<a name="WRW3h"></a>
#### 示例3：脚本计算，查询未删除电影的平均评分，并加上5
```json
{
  "query": {
    "match": {
      "status": 1
    }
  },
  "size": 0,
  "aggs": {
    "avg_score_5": {
      "avg": {
        "script": {
          "source": "doc.score.value+5"
        }
      }
    }
  }
}
```
查询结果3：aggregations.avg_score_5.value=5.111
```json
{
  "took": 335,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 222,
      "relation": "gte"
    },
    "max_score": null,
    "hits": []
  },
  "aggregations": {
    "avg_score_5": {
      "value": "5.111"
    }
  }
}
```
<a name="nQK7m"></a>
### 2、stats 统计 count max min avg sum 5个值
示例：获取电影评分的5个统计值
```json
{
  "aggs": {
    "score_stats": {
      "stats": {
        "field": "score"
      }
    }
  }
}
```
查询结果
```json
{
    "took":65,
    "timed_out":false,
    "_shards":{
        "total":5,
        "successful":5,
        "skipped":0,
        "failed":0
    },
    "hits":Object{...},
    "aggregations":{
        "score_stats":{
            "count":1265878,
            "min":0,
            "max":10,
            "avg":"0.111",
            "sum":"11111.11111"
        }
    }
}
```
<a name="ayeBJ"></a>
### 3、Extended stats 高级统计
高级统计，比stats多4个统计结果： 平方和、方差、标准差、平均值加/减两个标准差的区间
<a name="bjZTz"></a>
#### 示例：获取电影评分的多个统计值
```json
{
  "aggs": {
    "score_stats": {
      "extended_stats": {
        "field": "score"
      }
    }
  }
}
```
查询结果
```json
{
    "took":93,
    "timed_out":false,
    "_shards":{
        "total":5,
        "successful":5,
        "skipped":0,
        "failed":0
    },
    "hits":Object{...},
    "aggregations":{
        "score_stats":{
            "count":1265878,
            "min":0,
            "max":10,
            "avg":"0.8132805067098827",
            "sum":"1029513.901272893",
            "sum_of_squares":"7449929.070082645",
            "variance":"5.223762070903009",
            "std_deviation":"2.285555090323357",
            "std_deviation_bounds":{
                "upper":"5.384390687356596",
                "lower":"-3.757829673936831"
            }
        }
    }
}
```
<a name="iwIYC"></a>
### 4、Percentiles 占比百分位对应的值统计
<a name="wMoDq"></a>
#### 示例：获取占比百分位的电影评分
```json
{
  "aggs": {
    "score_percents": {
      "percentiles": {
        "field": "score",
        "percents" : [95, 99, 99.9]
      }
    }
  }
}
```
查询结果：95%的电影score<=7.400000095367432，99%的电影score<=8.5，99.9的电影score<=9.300000190734863
```json
{
    "took":2597,
    "timed_out":false,
    "_shards":{
        "total":5,
        "successful":5,
        "skipped":0,
        "failed":0
    },
    "hits":Object{...},
    "aggregations":{
        "score_percents":{
            "values":{
                "95.0":"7.400000095367432",
                "99.0":8.5,
                "99.9":"9.300000190734863"
            }
        }
    }
}
```
<a name="WSnfU"></a>
### 5、Percentiles rank 统计值小于等于指定值的文档占比
与2.4反过来的统计方式
<a name="XssT7"></a>
#### 示例：获取电影评分的占比百分位
```json
{
  "aggs": {
    "score_percents_ranks": {
      "percentile_ranks": {
        "field": "score",
        "values": [
          8.0,
          9.0
        ]
      }
    }
  }
}
```
查询结果：score<=8.0的占比97.66178099311308%，score<=9.0的占比99.75368874409698%
```json
{
    "took":2214,
    "timed_out":false,
    "_shards":{
        "total":5,
        "successful":5,
        "skipped":0,
        "failed":0
    },
    "hits":Object{...},
    "aggregations":{
        "score_percents_ranks":{
            "values":{
                "8.0":"97.66178099311308",
                "9.0":"99.75368874409698"
            }
        }
    }
}
```
<a name="yFyOw"></a>
### 6、cardinality  值去重计数
<a name="x6A6M"></a>
#### 示例：统计不重复的电影名称
```json
{
  "aggs": {
    "name_count": {
      "cardinality": {
        "field": "name.name_exactly"
      }
    }
  }
}
```
查询结果
```json
{
    "took":225,
    "timed_out":false,
    "_shards":{
        "total":5,
        "successful":5,
        "skipped":0,
        "failed":0
    },
    "hits":Object{...},
    "aggregations":{
        "name_count":{
            "value":1075191
        }
    }
}
```
<a name="WWpLD"></a>
## 三、桶聚合
<a name="x3f0G"></a>
### 1、terms 根据字段值项分组聚合
<a name="sXszO"></a>
#### 示例1：根据电影名称分组聚合
```json
{
  "aggs": {
    "name_terms": {
      "terms": {
        "field": "name.name_exactly"
      }
    }
  }
}
```
查询结果1:aggregations.name_terms.buckets就是分组结果，其中key表示分组字段(电影名称)，doc_count代表组内数量(电影数量)<br />doc_count_error_upper_bound": 0：文档计数的最大偏差值<br />sum_other_doc_count: 463：未返回的其他项的文档数<br />默认情况下返回按文档计数从高到低的前10个分组
```json
{
    "took":493,
    "timed_out":false,
    "_shards":{
        "total":5,
        "successful":5,
        "skipped":0,
        "failed":0
    },
    "hits":Object{...},
    "aggregations":{
        "name_terms":{
            "doc_count_error_upper_bound":48,
            "sum_other_doc_count":1265035,
            "buckets":[
                {
                    "key":"周六夜现场",
                    "doc_count":343
                },
                {
                    "key":"Home",
                    "doc_count":75
                },
                {
                    "key":"兄弟",
                    "doc_count":65
                },
                {
                    "key":"母亲",
                    "doc_count":63
                },
                {
                    "key":"回家",
                    "doc_count":58
                },
                {
                    "key":"初恋",
                    "doc_count":55
                },
                {
                    "key":"Yukutoshi kurutoshi",
                    "doc_count":53
                },
                {
                    "key":"Broken",
                    "doc_count":52
                },
                {
                    "key":"The Gift",
                    "doc_count":43
                },
                {
                    "key":"罗密欧与朱丽叶",
                    "doc_count":36
                }
            ]
        }
    }
}
```
**使用terms.size字段指定返回的数量**
<a name="vTbLn"></a>
#### 示例2：根据电影名称分组聚合，返回前5个分组
```json
{
  "aggs": {
    "name_terms": {
      "terms": {
        "field": "name.name_exactly",
        "size":5
      }
    }
  }
}
```
查询结果:
```json
{
    "took":239,
    "timed_out":false,
    "_shards":{
        "total":5,
        "successful":5,
        "skipped":0,
        "failed":0
    },
    "hits":Object{...},
    "aggregations":{
        "name_terms":{
            "doc_count_error_upper_bound":53,
            "sum_other_doc_count":1265287,
            "buckets":[
                {
                    "key":"周六夜现场",
                    "doc_count":343
                },
                {
                    "key":"Home",
                    "doc_count":75
                },
                {
                    "key":"母亲",
                    "doc_count":63
                },
                {
                    "key":"兄弟",
                    "doc_count":55
                },
                {
                    "key":"初恋",
                    "doc_count":55
                }
            ]
        }
    }
}
```
**使用terms.order指定分组的排序**
<a name="GDYnP"></a>
#### 示例3：根据电影名称分组聚合，正序返回前5个分组
```json
{
  "aggs": {
    "name_terms": {
      "terms": {
        "field": "name.name_exactly",
        "size": 5,
        "order": {
          "_count": "asc"
        }
      }
    }
  }
}
```
查询结果:
```json
{
    "took":338,
    "timed_out":false,
    "_shards":{
        "total":5,
        "successful":5,
        "skipped":0,
        "failed":0
    },
    "hits":{
        "total":{
            "value":10000,
            "relation":"gte"
        },
        "max_score":1,
        "hits":Array[10]
    },
    "aggregations":{
        "name_terms":{
            "doc_count_error_upper_bound":-1,
            "sum_other_doc_count":1265873,
            "buckets":[
                {
                    "key":"! [ai-ou]",
                    "doc_count":1
                },
                {
                    "key":"!Next?",
                    "doc_count":1
                },
                {
                    "key":"\" The Hollywood Greats\"  Joan Crawford (1978)",
                    "doc_count":1
                },
                {
                    "key":"\"2DTV\"",
                    "doc_count":1
                },
                {
                    "key":"\"30 Days\" Anti-Aging",
                    "doc_count":1
                }
            ]
        }
    }
}
```
**取分组指标排序**
<a name="zzsTv"></a>
#### 示例4：根据电影名称分组聚合，并根据组内的最大评分排序，取前5个
```json
{
  "aggs": {
    "name_terms": {
      "terms": {
        "field": "name.name_exactly",
        "size": 5,
        "order": {
          "max_score": "desc"
        }
      },
      "aggs": {
        "max_score": {
          "max": {
            "field": "score"
          }
        }
      }
    }
  }
}
```
查询结果:
```json
{
    "took":973,
    "timed_out":false,
    "_shards":{
        "total":5,
        "successful":5,
        "skipped":0,
        "failed":0
    },
    "hits":Object{...},
    "aggregations":{
        "name_terms":{
            "doc_count_error_upper_bound":-1,
            "sum_other_doc_count":1265873,
            "buckets":[
                {
                    "key":"2016海贼王剧场版",
                    "doc_count":1,
                    "max_score":{
                        "value":10
                    }
                },
                {
                    "key":"说不出口的秘密",
                    "doc_count":1,
                    "max_score":{
                        "value":10
                    }
                },
                {
                    "key":"吉县麟",
                    "doc_count":1,
                    "max_score":{
                        "value":"9.899999618530273"
                    }
                },
                {
                    "key":"Critico Histerico",
                    "doc_count":1,
                    "max_score":{
                        "value":"9.800000190734863"
                    }
                },
                {
                    "key":"摔跤吧！爸爸",
                    "doc_count":1,
                    "max_score":{
                        "value":"9.800000190734863"
                    }
                }
            ]
        }
    }
}
```
**筛选分组-正则表达式匹配值**
<a name="pTEl4"></a>
#### 示例5：筛选出含有"战狼"的电影，并根据名称进行分组
```json
{
  "aggs": {
    "name_terms": {
      "terms": {
        "field": "name.name_exactly",
        "include" : ".*战狼.*"
      }
    }
  }
}
```
查询结果:
```json
{
    "took":196,
    "timed_out":false,
    "_shards":{
        "total":5,
        "successful":5,
        "skipped":0,
        "failed":0
    },
    "hits":Object{...},
    "aggregations":{
        "name_terms":{
            "doc_count_error_upper_bound":0,
            "sum_other_doc_count":15,
            "buckets":[
                {
                    "key":"战狼",
                    "doc_count":4
                },
                {
                    "key":"白骨夫人大战狼妖",
                    "doc_count":3
                },
                {
                    "key":"战狼.战狼",
                    "doc_count":2
                },
                {
                    "key":"战狼犬",
                    "doc_count":2
                },
                {
                    "key":"脱衣舞娘大战狼人",
                    "doc_count":2
                },
                {
                    "key":"土耳其战狼",
                    "doc_count":1
                },
                {
                    "key":"小小战狼",
                    "doc_count":1
                },
                {
                    "key":"战狼2",
                    "doc_count":1
                },
                {
                    "key":"战狼3",
                    "doc_count":1
                },
                {
                    "key":"战狼三级班",
                    "doc_count":1
                }
            ]
        }
    }
}
```
**根据脚本计算出分组值**
<a name="AYJai"></a>
#### 示例6：根据评分分组，使用脚本值
```json
{
  "aggs": {
    "score_terms": {
      "terms": {
        "script": {
          "source": "doc['score']",
          "lang": "painless"
        }
      }
    }
  }
}
```
查询结果:
```json
{
    "took":340,
    "timed_out":false,
    "_shards":{
        "total":5,
        "successful":5,
        "skipped":0,
        "failed":0
    },
    "hits":Object{...},
    "aggregations":{
        "score_terms":{
            "doc_count_error_upper_bound":2722,
            "sum_other_doc_count":99639,
            "buckets":[
                {
                    "key":"0.0",
                    "doc_count":1118739
                },
                {
                    "key":"7.0",
                    "doc_count":5698
                },
                {
                    "key":"7.599999904632568",
                    "doc_count":5382
                },
                {
                    "key":"7.300000190734863",
                    "doc_count":5363
                },
                {
                    "key":"7.099999904632568",
                    "doc_count":5307
                },
                {
                    "key":"7.5",
                    "doc_count":5300
                },
                {
                    "key":"7.199999809265137",
                    "doc_count":5276
                },
                {
                    "key":"6.900000095367432",
                    "doc_count":5084
                },
                {
                    "key":"7.699999809265137",
                    "doc_count":5072
                },
                {
                    "key":"8.0",
                    "doc_count":5018
                }
            ]
        }
    }
}
```
**使用脚本进行多字段组合聚合**
<a name="rMAPO"></a>
#### 示例7：根据电影名称和导演进行分组
```json
{
  "aggs": {
    "name_director_terms": {
      "terms": {
        "script": {
          "source": "doc['name.name_exactly']+'|'+doc['director']",
          "lang": "painless"
        }
      }
    }
  }
}
```
查询结果:
```json
{
    "took":1344,
    "timed_out":false,
    "_shards":{
        "total":5,
        "successful":5,
        "skipped":0,
        "failed":0
    },
    "hits":Object{...},
    "aggregations":{
        "name_director_terms":{
            "doc_count_error_upper_bound":25,
            "sum_other_doc_count":1265432,
            "buckets":[
                {
                    "key":"[周六夜现场]|[唐·罗伊·金]",
                    "doc_count":73
                },
                {
                    "key":"[周六夜现场]|[]",
                    "doc_count":67
                },
                {
                    "key":"[Yukutoshi kurutoshi]|[]",
                    "doc_count":59
                },
                {
                    "key":"[周六夜现场]|[贝丝·麦卡锡-米勒]",
                    "doc_count":55
                },
                {
                    "key":"[The Gift]|[]",
                    "doc_count":40
                },
                {
                    "key":"[Melodi grand prix]|[]",
                    "doc_count":36
                },
                {
                    "key":"[Nationaal songfestival]|[]",
                    "doc_count":34
                },
                {
                    "key":"[Dronningens nytårstale]|[]",
                    "doc_count":31
                },
                {
                    "key":"[Broken]|[]",
                    "doc_count":26
                },
                {
                    "key":"[回家]|[]",
                    "doc_count":25
                }
            ]
        }
    }
}
```
<a name="s30Ts"></a>
### 2、filter 对满足过滤查询的文档进行聚合计算
在查询命中的文档中选取符合过滤条件的文档进行聚合，先过滤再聚合<br />示例1：对未删除电影的电影名称进行聚合
```json
{
  "aggs": {
    "name_terms": {
      "filter": {
        "match": {
          "status": "1"
        }
      },
      "aggs": {
        "effective_name_terms": {
          "terms": {
            "field": "name.name_exactly"
          }
        }
      }
    }
  }
}
```
查询结果:
```json
{
    "took":502,
    "timed_out":false,
    "_shards":{
        "total":5,
        "successful":5,
        "skipped":0,
        "failed":0
    },
    "hits":Object{...},
    "aggregations":{
        "name_terms":{
            "doc_count":1123676,
            "effective_name_terms":{
                "doc_count_error_upper_bound":41,
                "sum_other_doc_count":1122995,
                "buckets":[
                    {
                        "key":"周六夜现场",
                        "doc_count":276
                    },
                    {
                        "key":"Home",
                        "doc_count":66
                    },
                    {
                        "key":"母亲",
                        "doc_count":66
                    },
                    {
                        "key":"兄弟",
                        "doc_count":48
                    },
                    {
                        "key":"回家",
                        "doc_count":48
                    },
                    {
                        "key":"初恋",
                        "doc_count":46
                    },
                    {
                        "key":"Carmen",
                        "doc_count":40
                    },
                    {
                        "key":"秘密",
                        "doc_count":32
                    },
                    {
                        "key":"Yukutoshi kurutoshi",
                        "doc_count":31
                    },
                    {
                        "key":"Joulukalenteri",
                        "doc_count":28
                    }
                ]
            }
        }
    }
}
```
<a name="fMVqG"></a>
### 3、filters 多个过滤组聚合计算
示例1：筛选出名称为战狼或名称为哪吒的分组，同时为其他电影分组指定为其他电影
```json
{
  "aggs": {
    "name_terms": {
      "filters": {
        "other_bucket_key": "其他电影",
        "filters": {
          "战狼": {
            "match": {
              "name.name_exactly": "战狼"
            }
          },
          "哪吒": {
            "match": {
              "name.name_exactly": "哪吒"
            }
          }
        }
      }
    }
  }
}
```
查询结果:名称为战狼的电影有4个，名称为哪吒的电影有6个，其他电影1265868个
```json
{
    "took":75,
    "timed_out":false,
    "_shards":{
        "total":5,
        "successful":5,
        "skipped":0,
        "failed":0
    },
    "hits":Object{...},
    "aggregations":{
        "name_terms":{
            "buckets":{
                "哪吒":{
                    "doc_count":6
                },
                "战狼":{
                    "doc_count":4
                },
                "其他电影":{
                    "doc_count":1265868
                }
            }
        }
    }
}
```
<a name="F8wLS"></a>
### 4、 range 范围分组聚合+子聚合
示例1：计算出电影评分在8-9分和9-10分两个分组电影的平均时长，并指定分组名称为优秀，很优秀
```json
{
  "aggs": {
    "score_range": {
      "range": {
        "field": "score",
        "ranges": [
          {
            "key":"优秀",
            "from": 8,
            "to": 9
          },
          {
            "key":"很优秀",
            "from": 9
          }
        ]
      },
      "aggs": {
        "avg_duration_in_mins": {
          "avg": {
            "field": "duration_in_mins"
          }
        }
      }
    }
  }
}
```
查询结果:8-9分优秀电影的平均时长为55.28353587481272，9分以上很优秀电影的平均时长为47.992548435171386
```json
{
    "took":45,
    "timed_out":false,
    "_shards":{
        "total":5,
        "successful":5,
        "skipped":0,
        "failed":0
    },
    "hits":Object{...},
    "aggregations":{
        "score_range":{
            "buckets":[
                {
                    "key":"优秀",
                    "from":8,
                    "to":9,
                    "doc_count":30035,
                    "avg_duration_in_mins":{
                        "value":"55.28353587481272"
                    }
                },
                {
                    "key":"很优秀",
                    "from":9,
                    "doc_count":4026,
                    "avg_duration_in_mins":{
                        "value":"47.992548435171386"
                    }
                }
            ]
        }
    }
}
```
<a name="G6dv0"></a>
### 5、missing 缺失值桶聚合
示例1：统计出缺失导演的电影集合
```json
{
  "aggs": {
    "without_director":{
      "missing":{
           "field" : "director"
      }
    }
  }
}
```
查询结果:缺失导演的电影共有x个
```json
{
    "took":85,
    "timed_out":false,
    "_shards":{
        "total":5,
        "successful":5,
        "skipped":0,
        "failed":0
    },
    "hits":Object{...},
    "aggregations":{
        "without_director":{
            "doc_count":x
        }
    }
}
```

