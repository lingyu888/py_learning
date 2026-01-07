# 题目：暂停一秒输出，并格式化输出当前时间。

""" solution 1 """
print("solution 1:")
import time
import datetime

TIME = datetime.datetime.now()  # 获取当前时间
print(TIME.strftime("%Y.%m.%d %H-%M-%S"))  # 格式化输出时间

time.sleep(1)  # 暂停1秒

TIME = datetime.datetime.now()  # 获取当前时间
print(TIME.strftime("%Y.%m.%d %H-%M-%S"))  # 格式化输出时间



""" solution 2 """
print("solution 2:")
import time

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))  # 获取当前时间并格式化

time.sleep(1)  # 暂停1秒

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))  # 再次输出当前时间



""" reflection """
# | 特性        | 方法 1 (`datetime` 模块)             | 方法 2 (`time` 模块)                  |
# | --------- | -------------------------------- | --------------------------------- |
# | 获取当前时间的方法 | `datetime.datetime.now()`        | `time.localtime(time.time())`     |
# | 获取的时间类型   | `datetime` 对象                    | `struct_time` 对象（包含更多的字段）         |
# | 格式化方法     | `strftime()` 直接使用于 `datetime` 对象 | `strftime()` 使用于 `struct_time` 对象 |
# | 精度        | 获取到的是完整的日期时间（如：年月日时分秒）           | 使用 UNIX 时间戳转换成本地时间，精度取决于系统的时间戳    |
# | 可读性       | 通过 `datetime` 对象直接获取更易理解的信息      | 通过 `struct_time` 对象获取信息，相对更低级一些   |
