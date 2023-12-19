---
book_id: 28973507
cnblog_id: '17912959'
doc_id: 124368762
tags:
- 基础语法
- Python
title: Python类成员转list
---
<a name="vRDQe"></a>
## 一、举例
```python
class Student:
    id
    name
    birthdate
    gender
    address
    phone
    email
    grade
    vclass
    major
    college
```
<a name="ctocn"></a>
## 二、成员list
<a name="naYdP"></a>
### 1、使用__dir__功能
```python
student = Student()
print(student.__dir__)
print(student.__dir__.keys())
print(student.__dir__.values())
```
<a name="rmh0G"></a>
### 2、使用vars()函数
```python
student = Student()
print(vars(student))
```
<a name="J91lX"></a>
### 3、使用getmembers()函数
```python
import inspect
student = Student()
print(inspect.getmembers(student))
for i in inspect.getmembers(student):
    if not i[0].startswith('_'):
        if not inspect.ismethod(i[1]):
            print(i)
```
<a name="kiFQS"></a>
### 4、列表推导式
```python
import inspect
student = Student()
print([i for i in inspect.getmembers(student) if not i[0].startswith('_') and not inspect.ismethod(i[1])])
```
<a name="GnAKT"></a>
### 5、直接转数组
```python
student = Student()
print([student])
```

