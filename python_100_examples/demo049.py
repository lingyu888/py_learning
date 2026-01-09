# 题目：使用lambda来创建匿名函数。
# 比大小

x = int(input('x = '))
y = int(input('y = '))

max = lambda x, y : (x > y) * x + (x < y) * y
min = lambda x, y : (x < y) * x + (x > y) * y

print(f'max = {max(x, y)}, min = {min(x, y)}')

""" reflection """
# lambda 本质上还是一个函数，因此需要调用