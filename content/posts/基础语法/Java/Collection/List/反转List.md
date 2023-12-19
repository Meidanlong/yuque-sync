---
book_id: 28973507
cnblog_id: '17913017'
doc_id: 132169731
tags:
- 基础语法
- Java
- Collection
- List
title: 反转List
---
<a name="kuu9U"></a>
## 一、使用Collections.reverse()方法反转
```java
public void reverseList1(List<String> list) {
    Collections.reverse(list);
}
```
<a name="ApVJV"></a>
## 二、自定义实现
```java
public void reverseList2(List<String> list) {
    List<String> tmpList = new ArrayList<>();
    for (int i = list.size() - 1; i >= 0; i--) {
        tmpList.add(list.get(i));
    }
    list.clear();
    list.addAll(tmpList);
}
```

