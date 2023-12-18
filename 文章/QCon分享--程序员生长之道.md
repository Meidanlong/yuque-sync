---
book_id: 28973751
cnblog_id: '17911837'
doc_id: 121371458
tags:
- 文章
title: QCon分享--程序员生长之道
update_time: 2023-07-17 10:38:29
---
<a name="W2OGf"></a>
# ![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1681191220750-7120e1a8-6599-4a2c-bda0-b9a0587b9b11.png#averageHue=%234b5a84&clientId=uba73d064-43f4-4&from=paste&height=426&id=u7ad4a370&originHeight=938&originWidth=1408&originalType=binary&ratio=2.200000047683716&rotation=0&showTitle=false&size=1754083&status=done&style=none&taskId=u1116161c-fa84-48f5-99c8-174e81de435&title=&width=639.9999861283738)
<a name="EQSS7"></a>
# 一、导师介绍
<a name="c8Y9d"></a>
## 杨攀（娓娓道来，热点关注）
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1681191222218-cb612f9c-120f-410c-b62f-00e48cf0678d.png#averageHue=%23616a9a&clientId=uba73d064-43f4-4&from=paste&height=136&id=uc9508f16&originHeight=300&originWidth=197&originalType=binary&ratio=2.200000047683716&rotation=0&showTitle=false&size=107433&status=done&style=none&taskId=ub658b2e0-80b4-47f0-bd6a-42eccc95df9&title=&width=89.54545260460912)

- 涛思数据（TDengine）战略合作与开发者关系副总裁
- TGO 鲲鹏会北京分会会长
- 大规模高并发领域专家，拥有多年大规模即时通讯和社交产品研发、设计、运营经验
- 原 MSN Mobile China、飞信核心团队成员
- 曾联合创立融云并任 CTO，从零到一开创了全球即时通讯云服务产业并带领融云成为行业领导厂商。
<a name="YLmU3"></a>
## Winter（反应快速，角度新颖）
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1681191234219-e728b2be-3a54-4867-a379-3b9d30764ed7.png#averageHue=%23535c8c&clientId=uba73d064-43f4-4&from=paste&height=136&id=uee2ee7fc&originHeight=300&originWidth=200&originalType=binary&ratio=2.200000047683716&rotation=0&showTitle=false&size=110448&status=done&style=none&taskId=u3d1f17e4-6d93-4746-bf7c-08e2d6901ef&title=&width=90.90908893868948)

- 现任开课吧Web教学首席顾问
- 前端社区知名专家
- 前阿里P8高级技术专家
- 前手机淘宝前端leader
- 前淘宝终端架构leader
<a name="clQO2"></a>
## 宗刚（逻辑清晰，思考深刻）
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1681191241927-654edd75-2d4b-4d3d-aa10-407d721aeeaf.png#averageHue=%235c6490&clientId=uba73d064-43f4-4&from=paste&height=136&id=u59b42ad5&originHeight=300&originWidth=195&originalType=binary&ratio=2.200000047683716&rotation=0&showTitle=false&size=102552&status=done&style=none&taskId=u6b9d08cd-76af-4600-b414-75204fd8e38&title=&width=88.63636171522224)

- 动因体育技术副总裁
- 曾任思源高级技术副总裁
- 酒仙网产品技术总监
- 百度资深敏捷教练
- 惠普性能安全技术专家等
- 华为云 MVP
- 两届Qcon大会明星讲师
<a name="UVdWC"></a>
## 郭炜（善于表达，持续开源）
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1681191249566-f3f08d79-1c52-4a5d-a183-68526e8d1bb4.png#averageHue=%238ea0c6&clientId=uba73d064-43f4-4&from=paste&height=136&id=ue82374ea&originHeight=300&originWidth=196&originalType=binary&ratio=2.200000047683716&rotation=0&showTitle=false&size=107230&status=done&style=none&taskId=u578bb214-d094-4a78-80af-9584b2e1be1&title=&width=89.09090715991569)

- Apache 基金会member
- ClickHouse数据库引擎 华人社区发起人
- Hadoop 国内开源社区首批贡献者
- 易观CTO
- 联想集团大数据总监
- IBM高级项目经理
- teradata项目经理
- 万达集团大数据部总经理



四位导师共同特点：**乐观**、**幽默、有亲和力**

<a name="F51VW"></a>
# 二、互联网寒冬背景
<a name="y6Djk"></a>
## 1、疫情原因
截止2022年上半年互联网公司死亡名单<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1681191260213-85216ecd-75be-470d-9510-f1eac1ba06b1.png#averageHue=%23685ca4&clientId=uba73d064-43f4-4&from=paste&height=418&id=u75952a2a&originHeight=920&originWidth=1106&originalType=binary&ratio=2.200000047683716&rotation=0&showTitle=false&size=685771&status=done&style=none&taskId=ubbbd8372-4fac-429b-bae5-67e30aa1e70&title=&width=502.7272618309528)
<a name="VW6I6"></a>
## 2、金融本身周期
康波周期：俄国经济学家康德拉季耶夫，在1926年发现的经济周期性<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1681191267873-b107aa69-8f26-43b6-8fe6-5fcdbdd33174.png#averageHue=%23f9f9f9&clientId=uba73d064-43f4-4&from=paste&height=303&id=u72b890ec&originHeight=666&originWidth=1616&originalType=binary&ratio=2.200000047683716&rotation=0&showTitle=false&size=638359&status=done&style=none&taskId=u16f1fc36-974d-49bc-815b-606518cfdeb&title=&width=734.5454386246109)
<a name="GYNLu"></a>
## 3、公司正常人员储备
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1681191275562-6b7efea5-591e-449e-b47c-3e205fa8e046.png#averageHue=%23fcfcfc&clientId=uba73d064-43f4-4&from=paste&height=318&id=u27be7b10&originHeight=700&originWidth=1242&originalType=binary&ratio=2.200000047683716&rotation=0&showTitle=false&size=71269&status=done&style=none&taskId=u0d689593-8ea1-4d6e-ab86-5b815c97f53&title=&width=564.5454423092616)<br />**Winer：**公司人员的储备率大致是公司业绩的一阶导数

<a name="ZGnrd"></a>
# 三、技术人的困扰是什么
<a name="fumwQ"></a>
## 1、技术更新换代快

1. 专注自己的领域，技术相通
2. 拥抱业务
<a name="XxWly"></a>
## 2、35岁瓶颈，能否持续编程

1. 国内并不乐观，后文阐述“倾斜三角”模型
2. 具备业务思维，适用于技术负责人或转型管理
<a name="Ws7Av"></a>
## 3、提升自己的时间少

1. 不可否认工作中的个人成长是有局限性的，想要提升自己必须是在业余时间
2. 主动承担更具挑战的项目工作
<a name="kwrm7"></a>
## 4、你的核心竞争力是什么

1. 专业上，就是你所做出的一些成绩（结果），可以是公司功能或是能够体现技术能力的，如博客、开源项目等
2. 其他方面，如沟通等其他软实力
> PS：面试应该看重什么？
> **许晓斌：**1. 历史项目、编码能力 2. 个人职业规划是否与公司规划契合 3. 沟通成本是否低，能够明确双方的想法


<a name="FiZ4l"></a>
# 四、管理者的困扰是什么
<a name="HT2dA"></a>
## 1、管理者误区
**许晓斌：**

1. 闷头干模式：延续独立贡献者的工作方法，所有方案自己做，所有代码自己写
2. 路由器模式：上级任务往下转发，任务结果收集汇报
3. 高压模式：对上过度汇报，对下持续增加，辅以不科学的价值宣导
4. 不决策模式：不对任何需求 say no，或者决策全部下放，并让下属承担决策后果
5. 有业务无工程模式：度关注短期业务交付，不管工程质量
<a name="cCKF0"></a>
## 2、员工管理和人员流失
**杨攀：**

1. 对员工有恰当的定位，而不是管着他们
2. 为员工营造好的团队氛围，让员工有归属感和认同感
3. 打造团队文化：PROS：profession 专业，responsibility 责任，open 开放，share 分享。
4. 从关注技术到关注技术人
5. 正确看待人员流失的问题

**乔布斯：**

1. 管理者并不是“管人”，管理者的任务是用简洁的话描述一个有共识的清晰的目标，之后的事情聪明的人会想办法达成目标
<a name="JuL4S"></a>
## 3、降本增效

1. 确定公司核心竞争力
2. 服务降本
3. 创造工具，释放人力成本
4. 提升公司经营效益
<a name="i9Dvr"></a>
## 4、工程师文化
**许晓斌：**<br />软件系统是极高复杂度的系统，复杂度失控，质量失控，会导致系统崩溃。 研发人员是知识工作者，是“手艺人”，良好的工程文化能激发他们的工作热情，反之则会消磨热情。<br />_具体做法：_

1. 要求代码开放，要求 code review，要求 unit test
2. 搭建 CI 看板。 技术领导者每天参与 code review
3. 绩效考核/晋升考核中纳入“技术素养”的要求
4. 定义阶段性技术目标，降低系统复杂度（如：下线服务，架构治理）

**杨攀：**<br />做一些分享、培训，时不时抛出些问题让大家讨论；给工程师留出 20% 的时间，去学习和做研究。这不是对公司生产力的浪费，而是有了这 20% 的储备，才有可能为公司贡献更多

<a name="tehOm"></a>
# 五、技术人如何提升自己
<a name="O1IWx"></a>
## 1、个人成长
**宗刚：**<br />个人成长主要面对两大类问题：规划类和临时面对类<br />规划类问题的解决思路：

1. 以终为始，结果导向，看长远
2. 将宏伟的目标拆解成微习惯
3. [福格行为模型 B=MAP](https://www.jianshu.com/p/1ab4f34f8204)
   1. 行为Behavior在M(动机），A(能力），P(提示）齐全的情况下发生。考虑的次序是提示、能力、动机

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1681191373798-fa4adc73-d79e-40f1-8543-315d6e313eed.png#averageHue=%23e8f0cd&clientId=uba73d064-43f4-4&from=paste&height=136&id=u83a4c633&originHeight=300&originWidth=270&originalType=binary&ratio=2.200000047683716&rotation=0&showTitle=false&size=78155&status=done&style=none&taskId=u41ae9e0a-4231-4183-81e9-733cd603caf&title=&width=122.72727006723079)<br />临时面对类问题的解决思路：

1. 创造环境，刻意练习
2. 方法论：三本书 + 专家 + 实验 + 实战 + 分享
   1. 物理学诺贝尔奖得主诺曼：如果不把一个理论解释到让大一新生都能轻松听懂的程度，那就说明我们没有真正搞懂它（把所学的知识教授他人，并不断填充修正，才能让你印象深刻）
<a name="fUqKQ"></a>
## 2、充实自己、把握机会
**郭炜&杨攀：**

1. 尽早与社区建立联系
2. 多标签：不受局限
3. 打造个人IP（个人品牌影响力）
   1. 开源社区
   2. 个人博客：1. 个人提升：写说相辅相成；2. 被人看到，帮助求知者、与他人建立联系
<a name="ihYHS"></a>
## 3、沟通等软实力
<a name="tEevP"></a>
### 3.1、麦肯锡30秒电梯法则：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1681191383311-b508aac5-3b6a-45f4-b5ad-5425989b20ac.png#averageHue=%23fbf9f2&clientId=uba73d064-43f4-4&from=paste&height=318&id=ufd47c51a&originHeight=700&originWidth=1368&originalType=binary&ratio=2.200000047683716&rotation=0&showTitle=false&size=329322&status=done&style=none&taskId=u9c9eb97f-c599-4955-8abb-ad203eb8fae&title=&width=621.818168340636)

1. 金字塔原理
   1. 先从结论说起，先说中心思想，再说论点、论据，然后再向前推演，状如金字塔
   2. 其要领为：目标明确，结论先行， 以上统下、归类分组， 逻辑递进、关系依赖， 先重后次、先全后细
2. MECE分析法
   1. MECE读作“me-see”，全称是mutually exclusive, collectively exhaustive，意思是“相互独立，完全穷尽”
   2. MECE是用最高的条理化和最大的完善度理清你的思路，做到不重叠、不遗漏，这种高度的条理化使得你的困惑度降到最低
<a name="Wn0a8"></a>
### 3.2、日常工作沟通131框架
1 ：是指结论先行（直奔主题，不用对方猜测你的意图：人的大脑在接收信息时，会不断地猜测后面的内容，如果我们不第一时间给出观点，则对方很可能会根据局部的信息在脑中提前形成与你不一致的结论）<br />3 ：指支持结论的三个理由（用MECE法，保证三个论点相互独立、完全穷尽）<br />1 ：总结（总结陈词，提出反馈）
<a name="TRL8Q"></a>
### 3.3、横向逻辑关系
时间顺序：比如按照事务发展的时间线划分<br />空间顺序：比如按照地点空间来划分<br />程度顺序：比如重要的，不重要的来划分

<a name="J6u68"></a>
## 4、业务思维
**郭炜：**倾斜三角法则<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1681191392892-ace40382-3c28-41a4-b75f-793f8c4a489a.png#averageHue=%23f4f2f1&clientId=uba73d064-43f4-4&from=paste&height=412&id=u17695f81&originHeight=906&originWidth=1266&originalType=binary&ratio=2.200000047683716&rotation=0&showTitle=false&size=458397&status=done&style=none&taskId=u83673f7b-6d87-4219-b953-efbd0c27c7e&title=&width=575.4545329819043)<br />互联网寒冬之前<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1681191417171-f27a8976-e77f-4cee-97bd-63735ac75bb8.png#averageHue=%23f8f6f5&clientId=uba73d064-43f4-4&from=paste&height=472&id=ud11ac51d&originHeight=1038&originWidth=1258&originalType=binary&ratio=2.200000047683716&rotation=0&showTitle=false&size=669827&status=done&style=none&taskId=u372cb0b6-c659-4660-a845-a180e01a208&title=&width=571.8181694243568)<br />互联网寒冬
<a name="zz1Ht"></a>
## 5、向上管理
**Winter：**<br />manage to sth 设法做某事，管理的对象可以下属，也可以是同级甚至领导，也可以是其他。需要具备逆向思维<br />**宗刚：**<br />举例自己与室友的经历，为何在同一家公司任职多年，室友跳槽薪资涨幅是自己的一倍：室友在工作中主动承担更具挑战性的项目或需求，其目的是督促自身成长<br />另外宗刚老师还提出：领导是你的重要人脉
<a name="JcbEq"></a>
## 6、技术眼界
**杨攀：**<br />绝大多数技术人并不是卡在能力上，而是卡在眼界上。技术人不仅仅需要技术，也要有正确的认知，比如有个新工具（开源社区）能让工作效率提升五倍，技术人员是否知道？是否能接受并使用？这就是视野问题、认知问题。对此，杨攀的建议就是技术人需要扩展事业外的眼界，想办法解决根本上的问题，就会达到事半功倍的效果

<a name="SN8yp"></a>
# 六、未来技术方向
**ChatGPT：**<br />未来5年互联网行业的风口可能包括以下几个方面：

1. 人工智能技术的应用：随着人工智能技术的不断发展，它将逐渐渗透到各个领域，包括互联网行业。人工智能技术可以帮助企业提高效率、降低成本，同时也可以提供更好的用户体验。
2. 移动互联网的发展：移动互联网已经成为互联网行业的主要趋势，未来5年，移动互联网的普及率还将继续提高。这将促进移动应用、移动支付、移动广告等业务的发展。
3. 5G技术的普及：5G技术的普及将会大大提高互联网的传输速度和稳定性，同时也将带来更多的应用场景，比如虚拟现实、增强现实等。
4. 电商的发展：电商已经成为互联网行业的重要组成部分，未来5年，电商的发展还将继续加速。电商企业将会更加注重用户体验、物流配送等方面的提升。
5. 区块链技术的应用：区块链技术可以帮助解决互联网行业中的信任问题，未来5年，区块链技术的应用将会逐渐普及。比如，可以应用于数字货币、数字版权等方面。



<a name="FtFHb"></a>
# 七、推荐书单

- 《精益创业》 -- 站在业务角度看待技术问题
- 《系统思考》丹尼斯.舍伍德 -- “很多人只是机械的应对，专注于事件层面的响应，而未触及问题产生的根源”，如果你也有相同困扰不妨读读看
- 《学会提问》尼尔·布朗
- 《纳瓦尔宝典》 -- 不仅是成功学书籍，更新慰藉心里鸡汤。
- 《活出心花怒放的人生》-- 相信人的大脑是可以重塑的，却并非像肉体重塑那么痛苦




