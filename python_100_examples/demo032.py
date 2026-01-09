# 题目：按相反的顺序输出列表的值。

""" solution 1 """
print('solution 1:')
list = ['one', 'two', 'three']
invert_list = []

for c in list[::-1]:
    invert_list.append(c)
print(f'列表 {list} 倒置后为：{invert_list}')

""" reflection """
# list[start:stop:step]
# list[::-1]: 这里没有指定 start 和 stop，只有 step，其值为 -1
# 表示从列表的最后一个元素开始，以反向顺序访问整个列表，即将列表倒序排列

""" solution 2 """
print('solution 2:')
# 递归

invert_list = []

def invert(list, length):
    global invert_list
    if length == 0:
        return []
    else:
        return [list[length - 1]] + invert(list, length - 1)

list = ['one', 'two', 'three']
length = len(list)

print(f'列表 {list} 倒置后为：{invert(list, length)}')