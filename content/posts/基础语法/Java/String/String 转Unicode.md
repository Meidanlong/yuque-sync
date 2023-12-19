---
book_id: 28973507
cnblog_id: '17913018'
doc_id: 134113825
tags:
- 基础语法
- Java
- String
title: String 转Unicode
update_time: 2023-07-24 02:00:20
---
<a name="rfvI2"></a>
## 一、String转Unicode
```java
public static String unicodeToString(String unicode) {
    StringBuffer string = new StringBuffer();
    /* 以 \ u切割 */
    String[] hex = unicode.split("\\\\u");
    for (int i = 1; i < hex.length; i++) {
        /* 这里代表将值转为16进制表示，一共有2, 8, 10, 16几种表示 */
        int data = Integer.parseInt(hex[i], 16);
        /* 追加成String */
        string.append((char) data);
    }
    return string.toString();
}
```
<a name="Pf2y4"></a>
## 二、Unicode转String
```java
public static String stringToUnicode(String string) {
    StringBuffer unicode = new StringBuffer();
    for (int i = 0; i < string.length(); i++) {
        /* 取出每一个字符 */
        char c = string.charAt(i);
        /* 转换为unicode Integer.toHexString(); 返回字符的16进制表示 */
        unicode.append("\\u" + Integer.toHexString(c));
    }
    return unicode.toString();
}
```

