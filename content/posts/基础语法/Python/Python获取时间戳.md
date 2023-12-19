---
book_id: 28973507
cnblog_id: '17912954'
doc_id: 124460165
tags:
- 基础语法
- Python
title: Python获取时间戳
---
<a name="bBGvt"></a>
## 一、获取时间戳
```python
import time
import datetime

t = time.time()

print (t)                       #原始时间数据
print (int(t))                  #秒级时间戳
print (int(round(t * 1000)))    #毫秒级时间戳
print (int(round(t * 1000000))) #微秒级时间戳

# 输出
# 1648812012.4263625	#原始时间数据
# 1648812012			#秒级时间戳，10位
# 1648812012426		#毫秒级时间戳，13位
# 1648812012426362	#微秒级时间戳，16位
```
<a name="tB2oY"></a>
## 二、时间戳转日期
```python
dt    = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# 2022-04-01 19:21:19


# 含微秒的日期时间，来源 比特量化
dt_ms = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') 
# 2022-04-01 19:21:19.281936


ts = 1515774430
dt_local = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))
#  2018-01-13 00:27:10
```
<a name="vuGPL"></a>
## 三、日期转时间戳
```python
dt = '2018-01-01 10:40:30'
ts = int(time.mktime(time.strptime(dt, "%Y-%m-%d %H:%M:%S")))

# 1514774430
```
<a name="nZwFm"></a>
## 四、转换时间戳格式
```python
dt = '08/02/2019 01:00'
dt_new = datetime.datetime.strptime(dt, '%m/%d/%Y %H:%M').strftime('%Y-%m-%d %H:%M:%S')

# 2019-08-02 01:00:00
```
<a name="d1EEG"></a>
## 五、转结构体时间`struct_time`
```python
ta_dt = time.strptime("2018-09-06 21:54:46", '%Y-%m-%d %H:%M:%S')  #日期时间转结构体 
# time.struct_time(tm_year=2018, tm_mon=9, tm_mday=6, 
# tm_hour=21, tm_min=54, tm_sec=46, tm_wday=3, tm_yday=249, tm_isdst=-1)


ta_ms = time.localtime(1486188476) #时间戳转结构体，注意时间戳要求为int，来源 比特量化
# time.struct_time(tm_year=2017, tm_mon=2, tm_mday=4, 
# tm_hour=14, tm_min=7, tm_sec=56, tm_wday=5, tm_yday=35, tm_isdst=0)
```

---

**参考**<br />[Python获取秒级时间戳与毫秒级时间戳的方法_python 毫秒时间戳_Python热爱者的博客-CSDN博客](https://blog.csdn.net/qdPython/article/details/123902445)

