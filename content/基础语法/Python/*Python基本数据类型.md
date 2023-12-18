---
book_id: 28973507
cnblog_id: '17912490'
doc_id: 119597839
tags:
- 基础语法
- Python
title: '*Python基本数据类型'
---
[Python教程](https://www.liaoxuefeng.com/wiki/1016959663602400)<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/26501265/1679907230024-5cb75c85-c392-41c1-aac4-a271816ec83d.png#averageHue=%2355636f&clientId=u8161c308-4893-4&from=paste&height=247&id=UPDqL&originHeight=543&originWidth=1773&originalType=binary&ratio=2.200000047683716&rotation=0&showTitle=false&size=345061&status=done&style=none&taskId=u09f4ae6e-be83-4200-883a-d419be45b42&title=&width=805.9090734414822)

- 如果在定义函数时，*代表收集参数，**代表收集关键字参数。
- 如果在调用函数时，*和**都是分配参数用的

在Python中，`**`有两个主要的用途：

1.  作为数学运算符，表示幂运算。例如，`2 ** 3`的结果是8，因为2的3次方等于8。 
2.  在函数调用和定义中，表示关键字参数的字典。例如，你可以使用`**`来将一个字典的键值对作为关键字参数传递给一个函数。 

下面是两个例子：
```python
print(2 ** 3)  # 输出：8
```
```python
def greet(name, greeting):
   print(f"{greeting}, {name}!")

params = {"name": "Alice", "greeting": "Hello"}
greet(**params)  # 输出：Hello, Alice!
```
在这个例子中，`**params`将`params`字典的键值对解包并作为关键字参数传递给`greet`函数。

函数定义
```python
def print_info(**kwargs):
   for key, value in kwargs.items():
       print(f"{key}: {value}")

print_info(name="Alice", age=25)  
# 输出：
# name: Alice
# age: 25
```
在这个例子中，`**kwargs`在函数定义中用于接收任意数量的关键字参数，并将它们保存在一个名为`kwargs`的字典中

在Python中，`*`符号有两个主要的用途：

1.  作为数学运算符，表示乘法。例如，`2 * 3`的结果是6。 
2.  在函数调用和定义中，表示可变数量的位置参数。你可以使用`*`来将一个列表或元组的元素作为位置参数传递给一个函数，或者在函数定义中接收任意数量的位置参数。 

下面是两个例子：
```python
print(2 * 3)  # 输出：6
```
```python
def greet(greeting, name):
   print(f"{greeting}, {name}!")

params = ["Hello", "Alice"]
greet(*params)  # 输出：Hello, Alice!
```
在这个例子中，`*params`将`params`列表的元素解包并作为位置参数传递给`greet`函数。

例子3：函数定义
```python
def print_numbers(*args):
   for number in args:
       print(number)

print_numbers(1, 2, 3, 4, 5)  
# 输出：
# 1
# 2
# 3
# 4
# 5
```
在这个例子中，`*args`在函数定义中用于接收任意数量的位置参数，并将它们保存在一个名为`args`的元组中。

[Python中的*（星号）和**(双星号）完全详解_python中**_zkk9527的博客-CSDN博客](https://blog.csdn.net/zkk9527/article/details/88675129)

