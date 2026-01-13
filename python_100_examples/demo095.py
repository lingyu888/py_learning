# 题目：字符串日期转换为易读的日期格式。

from dateutil import parser
dt = parser.parse("Aug 28 2015 8:00AM")
print(dt)
dt = parser.parse("9 28 2015 8:00AM")
print(dt)
dt = parser.parse("28 10 2015 8:00AM")
print(dt)
dt = parser.parse("12 10 2015 8:00AM")
print(dt)


""" reflection """
# dateutil.parser 提供了一个非常强大的 parse() 函数，
# 能够将多种格式的日期字符串解析为 Python datetime 对象。