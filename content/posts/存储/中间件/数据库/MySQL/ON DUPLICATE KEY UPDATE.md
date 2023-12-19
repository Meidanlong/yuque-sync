---
book_id: 28973507
cnblog_id: '17913057'
doc_id: 131370695
tags:
- 存储/中间件
- 数据库
- MySQL
title: ON DUPLICATE KEY UPDATE
---
```xml
<insert id="batchInsert" parameterType="java.util.List">
    insert into aigc_text (business_id, business_type, scene_index, text_eng, text_chn, text_prompt)
    values
    <foreach collection="records" item="r" index="index" separator=",">
        (
        #{r.businessId,jdbcType=BIGINT},
        #{r.businessType,jdbcType=INTEGER},
        #{r.sceneIndex,jdbcType=INTEGER},
        #{r.textEng,jdbcType=LONGVARCHAR},
        #{r.textChn,jdbcType=LONGVARCHAR},
        #{r.textPrompt,jdbcType=LONGVARCHAR}
        )
    </foreach>
    ON DUPLICATE KEY UPDATE
        business_id = VALUES(business_id),
        business_type = VALUES(business_type),
        scene_index = VALUES(scene_index)
</insert>
```
:::warning

1.  `ON DUPLICATE KEY UPDATE`检查主键或唯一索引字段是否冲突。 
2.  `update`的字段值与现存的字段值相同，则不更新。 
3.  动态更新字段值用`VALUES`(字段名称)。 
:::

