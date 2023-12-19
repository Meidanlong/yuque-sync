---
book_id: 28973507
cnblog_id: '17912952'
doc_id: 147807243
tags:
- 基础语法
- Python
title: Python基础知识
update_time: 2023-11-22 08:18:50
---
<a name="otY2o"></a>
# 一、先置知识
<a name="eeLV0"></a>
## 1、标识符

- 标识符由字母、数字、下划线组成。
- 所有标识符可以包括英文、数字以及下划线(_)，但不能以数字开头。
- 标识符是区分大小写的。
- 以下划线开头的标识符是有特殊意义的。以单下划线开头 **_foo** 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 **from xxx import *** 而导入。
- 以双下划线开头的 **__foo** 代表类的私有成员，以双下划线开头和结尾的 **__foo__** 代表 Python 里特殊方法专用的标识，如 **__init__()** 代表类的构造函数。
<a name="LTcnH"></a>
## 2、保留字符
下面的列表显示了在Python中的保留字。这些保留字不能用作常数或变数，或任何其他标识符名称。<br />所有 Python 的关键字只包含小写字母。

| and | exec | not |
| --- | --- | --- |
| assert | finally | or |
| break | for | pass |
| class | from | print |
| continue | global | raise |
| def | if | return |
| del | import | try |
| elif | in | while |
| else | is | with |
| except | lambda | yield |

<a name="AOQmq"></a>
## 3、行和缩进
Python 的代码块不使用大括号 **{}** 来控制类，函数以及其他逻辑判断。python 最具特色的就是用缩进来写模块。<br />缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。
<a name="DBDs2"></a>
## 4、多行语句
Python语句中一般以新行作为语句的结束符。<br />但是我们可以使用斜杠`\`将一行的语句分为多行显示
<a name="r5cHW"></a>
## 5、引号
Python 可以使用引号( **'** )、双引号( **"** )、三引号( **'''** 或 **"""** ) 来表示字符串，引号的开始与结束必须是相同类型的。<br />其中三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。
```python
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""
```
<a name="payIr"></a>
## 6、注释
单行注释采用 **#** 开头<br />多行注释使用三个单引号 **'''** 或三个双引号 **"""**。
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test.py


'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""
```
<a name="IHJ7l"></a>
## 7、同一行执行多条语句
Python 可以同一行显示多条语句，方法是用分号`;`分开。如：
```python
print ('hello');print ('runoob');
# hello
# runoob
```
<a name="dKWpl"></a>
## 8、print输出
print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号`,`。
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

x="a"
y="b"
# 换行输出
print x
print y

print '---------'
# 不换行输出
print x,
print y,

# 不换行输出
print x,y
```
**end 关键字**<br />end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
```python
print(b, end=',')
```
<a name="UwdyQ"></a>
## 9、多语句代码组
缩进相同的一组语句构成一个代码块，我们称之代码组。<br />像if、while、def和class这样的复合语句，首行以关键字开始，以冒号`:`结束，该行之后的一行或多行代码构成代码组。<br />我们将首行及后面的代码组称为一个子句(clause)。
```python
if expression : 
   suite 
elif expression :  
   suite  
else :  
   suite 
```
<a name="P7N7S"></a>
# 二、变量类型
<a name="Y4lyf"></a>
## 1、简单赋值
```python
counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串

print counter
print miles
print name

# 100
# 1000.0
# John
```
<a name="fK02O"></a>
## 2、多变量赋值
```python
a = b = c = 1

a, b, c = 1, 2, "john"
```
<a name="EjBFx"></a>
## 3、标准数据类型
Python有五个标准的数据类型：

- Numbers（数字）
- String（字符串）
- List（列表）
- Tuple（元组）
- Dictionary（字典）
- Set（集合）
<a name="XmeNR"></a>
### 3.1、数字
Python支持四种不同的数字类型：

- int（有符号整型）
- long（长整型，也可以代表八进制和十六进制）
- float（浮点型）
- complex（复数）

| int | long | float | complex |
| --- | --- | --- | --- |
| 10 | 51924361L | 0.0 | 3.14j |
| 100 | -0x19323L | 15.20 | 45.j |
| -786 | 0122L | -21.9 | 9.322e-36j |
| 080 | 0xDEFABCECBDAECBFBAEl | 32.3e+18 | .876j |
| -0490 | 535633629843L | -90. | -.6545+0J |
| -0x260 | -052318172735L | -32.54e100 | 3e+26J |
| 0x69 | -4721885298529L | 70.2E-12 | 4.53e-7j |

<a name="vmkKu"></a>
### 3.2、字符串
如果你要实现从字符串中获取一段子字符串的话，可以使用 **[头下标:尾下标]** 来截取相应的字符串，其中下标是从 0 开始算起，可以是正数或负数，下标可以为空表示取到头或尾。<br />**[头下标:尾下标]** 获取的子字符串包含头下标的字符，但不包含尾下标的字符。<br />比如:
```python
s = 'abcdef'
s[1:5]
# 'bcde'
```
当使用以冒号分隔的字符串，python 返回一个新的对象，结果包含了以这对偏移标识的连续的内容，左边的开始是包含了下边界。<br />上面的结果包含了 **s[1]** 的值 b，而取到的最大范围不包括**尾下标**，就是 **s[5]** 的值 f。<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1700637534397-56093e97-9043-49cc-8a5a-1f4e51f90eb6.png#averageHue=%23eaecef&clientId=ue99f1770-e60b-4&from=paste&height=151&id=u0b8fd4ce&originHeight=302&originWidth=734&originalType=binary&ratio=2&rotation=0&showTitle=false&size=60974&status=done&style=none&taskId=u576359cd-989a-401a-93c3-2e9905b8345&title=&width=367)<br />加号（+）是字符串连接运算符，星号（*）是重复操作。如下实例：
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
str = 'Hello World!'
 
print str           # 输出完整字符串
print str[0]        # 输出字符串中的第一个字符
print str[2:5]      # 输出字符串中第三个至第六个之间的字符串
print str[2:]       # 输出从第三个字符开始的字符串
print str * 2       # 输出字符串两次
print str + "TEST"  # 输出连接的字符串


# Hello World!
# H
# llo
# llo World!
# Hello World!Hello World!
# Hello World!TEST
```
Python 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串：<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1700637631128-afe5531a-32b8-4dc1-89e4-a4dfaf5f10a4.png#averageHue=%23fefefe&clientId=ue99f1770-e60b-4&from=paste&height=208&id=u984ee5a3&originHeight=416&originWidth=1198&originalType=binary&ratio=2&rotation=0&showTitle=false&size=47682&status=done&style=none&taskId=uefa2a12c-2414-44db-9507-accf9cb70e5&title=&width=599)
<a name="J4Fws"></a>
### 3.3、列表

- 列表用 **[ ]** 标识，是 python 最通用的复合数据类型。
- 列表中值的切割也可以用到变量 **[头下标:尾下标]** ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1700637694275-75ed3275-3d68-42ab-bb11-783962641349.png#averageHue=%23fefefe&clientId=ue99f1770-e60b-4&from=paste&height=352&id=u1409c7d2&originHeight=704&originWidth=1584&originalType=binary&ratio=2&rotation=0&showTitle=false&size=291914&status=done&style=none&taskId=u924f0c50-7561-471a-b1aa-d37f71c640b&title=&width=792)
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
 
print list               # 输出完整列表
print list[0]            # 输出列表的第一个元素
print list[1:3]          # 输出第二个至第三个元素 
print list[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2       # 输出列表两次
print list + tinylist    # 打印组合的列表

# ['runoob', 786, 2.23, 'john', 70.2]
# runoob
# [786, 2.23]
# [2.23, 'john', 70.2]
# [123, 'john', 123, 'john']
# ['runoob', 786, 2.23, 'john', 70.2, 123, 'john']
```
<a name="ocRBy"></a>
### 3.4、元组
元组用 `**()**` 标识。内部元素用逗号隔开。但是**元组不能二次赋值**，相当于只读列表。
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
 
print tuple               # 输出完整元组
print tuple[0]            # 输出元组的第一个元素
print tuple[1:3]          # 输出第二个至第四个（不包含）的元素 
print tuple[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2       # 输出元组两次
print tuple + tinytuple   # 打印组合的元组

# ('runoob', 786, 2.23, 'john', 70.2)
# runoob
# (786, 2.23)
# (2.23, 'john', 70.2)
# (123, 'john', 123, 'john')
# ('runoob', 786, 2.23, 'john', 70.2, 123, 'john')
```
<a name="iM0bp"></a>
### 3.5、字典
列表是有序的对象集合，字典是无序的对象集合<br />字典用`{}`标识。字典由索引(key)和它对应的值value组成。
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
 
tinydict = {'name': 'runoob','code':6734, 'dept': 'sales'}
 
 
print dict['one']          # 输出键为'one' 的值
print dict[2]              # 输出键为 2 的值
print tinydict             # 输出完整的字典
print tinydict.keys()      # 输出所有键
print tinydict.values()    # 输出所有值

# This is one
# This is two
# {'dept': 'sales', 'code': 6734, 'name': 'runoob'}
# ['dept', 'code', 'name']
# ['sales', 6734, 'runoob']
```
<a name="Rmle5"></a>
### 3.6、集合
集合（set）是一个无序的不重复元素序列。<br />集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。<br />可以使用大括号 `**{ }**` 创建集合，元素之间用逗号 `**,**` 分隔， 或者也可以使用 `**set()**` 函数创建集合。
```python
parame = {value01,value02,...}
# 或者
set(value)
```
<a name="o5Opi"></a>
## 4、数据类型转换
| 函数 | 描述 |
| --- | --- |
| [int(x [,base])](https://www.runoob.com/python/python-func-int.html) | 将x转换为一个整数 |
| [long(x [,base] )](https://www.runoob.com/python/python-func-long.html) | 将x转换为一个长整数 |
| [float(x)](https://www.runoob.com/python/python-func-float.html) | 将x转换到一个浮点数 |
| [complex(real [,imag])](https://www.runoob.com/python/python-func-complex.html) | 创建一个复数 |
| [str(x)](https://www.runoob.com/python/python-func-str.html) | 将对象 x 转换为字符串 |
| [repr(x)](https://www.runoob.com/python/python-func-repr.html) | 将对象 x 转换为表达式字符串 |
| [eval(str)](https://www.runoob.com/python/python-func-eval.html) | 用来计算在字符串中的有效Python表达式,并返回一个对象 |
| [tuple(s)](https://www.runoob.com/python/att-tuple-tuple.html) | 将序列 s 转换为一个元组 |
| [list(s)](https://www.runoob.com/python/att-list-list.html) | 将序列 s 转换为一个列表 |
| [set(s)](https://www.runoob.com/python/python-func-set.html) | 转换为可变集合 |
| [dict(d)](https://www.runoob.com/python/python-func-dict.html) | 创建一个字典。d 必须是一个序列 (key,value)元组。 |
| [frozenset(s)](https://www.runoob.com/python/python-func-frozenset.html) | 转换为不可变集合 |
| [chr(x)](https://www.runoob.com/python/python-func-chr.html) | 将一个整数转换为一个字符 |
| [unichr(x)](https://www.runoob.com/python/python-func-unichr.html) | 将一个整数转换为Unicode字符 |
| [ord(x)](https://www.runoob.com/python/python-func-ord.html) | 将一个字符转换为它的整数值 |
| [hex(x)](https://www.runoob.com/python/python-func-hex.html) | 将一个整数转换为一个十六进制字符串 |
| [oct(x)](https://www.runoob.com/python/python-func-oct.html) | 将一个整数转换为一个八进制字符串 |

<a name="JKQuW"></a>
# 三、运算符
<a name="C6be5"></a>
## 1、算术运算符
| 运算符 | 描述 | 实例 |
| --- | --- | --- |
| + | 加 - 两个对象相加 | a + b 输出结果 30 |
| - | 减 - 得到负数或是一个数减去另一个数 | a - b 输出结果 -10 |
| * | 乘 - 两个数相乘或是返回一个被重复若干次的字符串 | a * b 输出结果 200 |
| / | 除 - x除以y | b / a 输出结果 2 |
| % | 取模 - 返回除法的余数 | b % a 输出结果 0 |
| ** | 幂 - 返回x的y次幂 | a**b 为10的20次方， 输出结果 100000000000000000000 |
| // | 取整除 - 返回商的整数部分（**向下取整**） | 9//2 -> 4 <br />-9//2 -> -5 |

> 整数除整数，只能得出整数。如果要得到小数部分，把其中一个数改成浮点数即可。

```python
1/2
# 0
1.0/2
# 0.5
1/float(2)
# 0.5
```
<a name="shs7N"></a>
## 2、比较运算符
| 运算符 | 描述 | 实例 |
| --- | --- | --- |
| == | 等于 - 比较对象是否相等 | (a == b) 返回 False。 |
| != | 不等于 - 比较两个对象是否不相等 | (a != b) 返回 True。 |
| <> | 不等于 - 比较两个对象是否不相等。**python3 已废弃。** | (a <> b) 返回 True。这个运算符类似 != 。 |
| > | 大于 - 返回x是否大于y | (a > b) 返回 False。 |
| < | 小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量 True 和 False 等价。 | (a < b) 返回 True。 |
| >= | 大于等于 - 返回x是否大于等于y。 | (a >= b) 返回 False。 |
| <= | 小于等于 - 返回x是否小于等于y。 | (a <= b) 返回 True。 |

<a name="Op8dR"></a>
## 3、赋值运算符
| 运算符 | 描述 | 实例 |
| --- | --- | --- |
| = | 简单的赋值运算符 | c = a + b 将 a + b 的运算结果赋值为 c |
| += | 加法赋值运算符 | c += a 等效于 c = c + a |
| -= | 减法赋值运算符 | c -= a 等效于 c = c - a |
| *= | 乘法赋值运算符 | c *= a 等效于 c = c * a |
| /= | 除法赋值运算符 | c /= a 等效于 c = c / a |
| %= | 取模赋值运算符 | c %= a 等效于 c = c % a |
| **= | 幂赋值运算符 | c **= a 等效于 c = c ** a |
| //= | 取整除赋值运算符 | c //= a 等效于 c = c // a |

<a name="qa7Jb"></a>
## 4、位运算符
| 运算符 | 描述 | 实例 |
| --- | --- | --- |
| & | 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0 | (a & b) 输出结果 12 ，二进制解释： 0000 1100 |
| &#124; | 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。 | (a &#124; b) 输出结果 61 ，二进制解释： 0011 1101 |
| ^ | 按位异或运算符：当两对应的二进位相异时，结果为1 | (a ^ b) 输出结果 49 ，二进制解释： 0011 0001 |
| ~ | 按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1 。**~x** 类似于 **-x-1** | (~a ) 输出结果 -61 ，二进制解释： 1100 0011，在一个有符号二进制数的补码形式。 |
| << | 左移动运算符：运算数的各二进位全部左移若干位，由 **<<** 右边的数字指定了移动的位数，高位丢弃，低位补0。 | a << 2 输出结果 240 ，二进制解释： 1111 0000 |
| >> | 右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，**>>** 右边的数字指定了移动的位数 | a >> 2 输出结果 15 ，二进制解释： 0000 1111 |

<a name="JsdrE"></a>
## 5、逻辑运算符
| 运算符 | 逻辑表达式 | 描述 | 实例 |
| --- | --- | --- | --- |
| and | x and y | 布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。 | (a and b) 返回 20。 |
| or | x or y | 布尔"或" - 如果 x 是非 0，它返回 x 的计算值，否则它返回 y 的计算值。 | (a or b) 返回 10。 |
| not | not x | 布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。 | not(a and b) 返回 False |

<a name="b62yU"></a>
## 6、成员运算符
| 运算符 | 描述 | 实例 |
| --- | --- | --- |
| in | 如果在指定的序列中找到值返回 True，否则返回 False。 | x 在 y 序列中 , 如果 x 在 y 序列中返回 True。 |
| not in | 如果在指定的序列中没有找到值返回 True，否则返回 False。 | x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。 |

<a name="kbxom"></a>
## 7、身份运算符
| 运算符 | 描述 | 实例 |
| --- | --- | --- |
| is | is 是判断两个标识符是不是引用自一个对象 | **x is y**, 类似 **id(x) == id(y)** , 如果引用的是同一个对象则返回 True，否则返回 False |
| is not | is not 是判断两个标识符是不是引用自不同对象 | **x is not y** ， 类似 **id(a) != id(b)**。如果引用的不是同一个对象则返回结果 True，否则返回 False。 |

<a name="Sdw1c"></a>
### is 和 == 的区别
`==` 最终取决于 `eq()`结果
```python
class Foo(object):
    q : str


if __name__ == "__main__":
    f = Foo()
    print(f is None) # False
    print(f == None) # False
```
```python
class Foo(object):
    q : str
    def __eq__(self, other):
    	return True


if __name__ == "__main__":
    f = Foo()
    print(f is None) # False
    print(f == None) # True
```
`==`比较的是值，`is`比较的是对象（对象id）
```python
list1 = [1,2,3]
list2 = [1,2,3]
print(list1 == list2) # True
print(list1 is list2) # False
print(id(list1) == id(list2)) # False
```
```python
list1 = (1,2,3)
list2 = (1,2,3)
print(list1 == list2) # True
print(list1 is list2) # True
print(id(list1) == id(list2)) # True
```
`元组`为**不可变对象**
<a name="aOo17"></a>
## 8、运算符优先级
| 运算符 | 描述 |
| --- | --- |
| ** | 指数 (最高优先级) |
| ~ + - | 按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@) |
| * / % // | 乘，除，取模和取整除 |
| + - | 加法减法 |
| >> << | 右移，左移运算符 |
| & | 位 'AND' |
| ^ &#124; | 位运算符 |
| <= < > >= | 比较运算符 |
| <> == != | 等于运算符 |
| = %= /= //= -= += *= **= | 赋值运算符 |
| is is not | 身份运算符 |
| in not in | 成员运算符 |
| not and or | 逻辑运算符 |


