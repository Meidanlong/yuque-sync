---
book_id: 28973507
cnblog_id: '17912951'
doc_id: 147814404
tags:
- 基础语法
- Python
title: '***Python语句操作'
update_time: 2023-11-22 08:10:01
---
<a name="QXWeO"></a>
# 一、条件控制
**Python 中有哪些值代表False**

- None
- Flase
- 0
- ""：空字符串
- []：空列表
- {}：空字典
- ()：空元组
<a name="Zs6jq"></a>
## 1、if语句
```python
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
```
**注意：**

- 1、每个条件后面要使用冒号`**:**`，表示接下来是满足条件后要执行的语句块。
- 2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
| 操作符 | 描述 |
| --- | --- |
| < | 小于 |
| <= | 小于或等于 |
| > | 大于 |
| >= | 大于或等于 |
| == | 等于，比较两个值是否相等 |
| != | 不等于 |

<a name="kZolx"></a>
## 2、match...case
```python
match subject:
    case <pattern_1>:
        <action_1>
    case <pattern_2>:
        <action_2>
    case <pattern_3>:
        <action_3>
    case _: # _可匹配一切，类似于java中的default
        <action_wildcard>
```
<a name="JU5Tw"></a>
# 二、循环语句
<a name="D51LJ"></a>
## 1、while循环
```python
while 判断条件(condition)：
    执行语句(statements)……
```
**while 循环使用 else 语句：**<br />如果 while 后面的条件语句为 false 时，则执行 else 的语句块。
```python
while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>
```
<a name="ks0WH"></a>
## 2、for循环
```python
for <variable> in <sequence>:
    <statements>
else:
    <statements>
```
**举例：**
```python
# 数组
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    print(site)

# 字符串
word = 'runoob'
for letter in word:
    print(letter)

#  1 到 5 的所有数字：
for number in range(1, 6):
    print(number)
```
**for 循环使用 else 语句：**<br />用于在循环结束后执行一段代码
```python
for item in iterable:
    # 循环主体
else:
    # 循环结束后执行的代码
```
<a name="BNbJv"></a>
## 3、range()函数
```python
# 成数列
for i in range(5):
	print(i)
# 0
# 1
# 2
# 3
# 4

# 指定区间的值
for i in range(5,9) :
    print(i)
# 5
# 6
# 7
# 8

# 指定数字开始并指定不同的步长
for i in range(0, 10, 3) :
    print(i)
# 0
# 3
# 6
# 9

# 结合len() 函数以遍历一个序列的索引
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
	print(i, a[i])
# 0 Google
# 1 Baidu
# 2 Runoob
# 3 Taobao
# 4 QQ

# 创建一个列表
list(range(5))
# [0, 1, 2, 3, 4]
```
<a name="UwUI4"></a>
## 4、break和continue
while 语句代码执行过程：<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1700639741906-a32bf022-c505-4763-9fef-74dd5c2598fa.png#averageHue=%23fefcfc&clientId=u37f1895d-23a1-4&from=paste&height=457&id=u4440432f&originHeight=914&originWidth=818&originalType=binary&ratio=2&rotation=0&showTitle=false&size=122367&status=done&style=none&taskId=udad6f923-6f22-47a7-8d34-67fe1a9ce3c&title=&width=409)<br />for 语句代码执行过程：<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1700639753280-04d641c8-5b91-48dd-9561-c61be58ee5a1.png#averageHue=%23fbf8f8&clientId=u37f1895d-23a1-4&from=paste&height=279&id=u20608d21&originHeight=558&originWidth=1010&originalType=binary&ratio=2&rotation=0&showTitle=false&size=88242&status=done&style=none&taskId=u809f9063-5064-47e9-aa06-72c1d89eb49&title=&width=505)<br />**break** 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。<br />**continue** 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
> 注：循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行，但循环被 break 终止时不执行。

```python
#!/usr/bin/python3
 
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')
```
<a name="Pd1vw"></a>
## 5、pass
pass是空语句，是为了保持程序结构的完整性。<br />pass 不做任何事情，一般用做占位语句，如下实例
```python
class MyEmptyClass:
    pass
```
<a name="y2bvN"></a>
# 三、推导式
Python 推导式是一种独特的数据处理方式，可以从一个数据序列构建另一个**新的数据序列的结构体**。<br />Python 支持各种数据结构的推导式：

- 列表(list)推导式
- 字典(dict)推导式
- 集合(set)推导式
- 元组(tuple)推导式
<a name="IMaxj"></a>
## 1、列表
```python
[表达式 for 变量 in 列表] 
[out_exp_res for out_exp in input_list]

# 或者 

[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]
```

- out_exp_res：列表生成元素表达式，可以是有返回值的函数。
- for out_exp in input_list：迭代 input_list 将 out_exp 传入到 out_exp_res 表达式中。
- if condition：条件语句，可以过滤列表中不符合条件的值。
```python
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)
# [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
```
<a name="Jz1e2"></a>
## 2、字典
```python
{ key_expr: value_expr for value in collection }

# 或

{ key_expr: value_expr for value in collection if condition }
```
```python
dic = {x: x**2 for x in (2, 4, 6)}
dic
# {2: 4, 4: 16, 6: 36}

type(dic)
# <class 'dict'>
```
<a name="R3xW9"></a>
## 3、集合
```python
{ expression for item in Sequence }

# 或

{ expression for item in Sequence if conditional }
```
```python
setnew = {i**2 for i in (1,2,3)}
setnew
# {1, 4, 9}
```
<a name="jSPOj"></a>
## 4、元组（生成器表达式）
元组推导式可以利用 range 区间、元组、列表、字典和集合等数据类型，快速生成一个满足指定需求的元组。
```python
(expression for item in Sequence )

# 或

(expression for item in Sequence if conditional )
```
元组推导式和列表推导式的用法也完全相同，只是元组推导式是用 `**()**`圆括号将各部分括起来，而列表推导式用的是中括号`**[]**`，另外元组推导式返回的结果是一个生成器对象。<br />例如，我们可以使用下面的代码生成一个包含数字 1~9 的元组：
```python
a = (x for x in range(1,10))
a
# <generator object <genexpr> at 0x7faf6ee20a50>  # 返回的是生成器对象

tuple(a)       # 使用 tuple() 函数，可以直接将生成器对象转换成元组
# (1, 2, 3, 4, 5, 6, 7, 8, 9)
```

