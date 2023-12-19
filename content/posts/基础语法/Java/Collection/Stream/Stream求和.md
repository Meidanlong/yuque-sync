---
book_id: 28973507
cnblog_id: '17913015'
doc_id: 132168673
tags:
- 基础语法
- Java
- Collection
- Stream
title: Stream求和
---
```java
List numbers = Arrays.asList(1, 2, 3, 4, 5);
int sum = numbers.stream().mapToInt(Integer::intValue).sum();
System.out.println("Sum of numbers: " + sum);
```

