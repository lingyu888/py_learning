# 题目：将一个数组逆序输出。

""" solution 1 """
print('solution 1:')

list = [1, 5, 6, 8, 10, 15]
invert_list = []

for c in list[::-1]:
    invert_list.append(c)

print(list)
print(invert_list)



""" solution 2 """
print('solution 2:')

list = [1, 5, 6, 8, 10, 15]
length = len(list)
print(list)

for i in range(length // 2):
    list[i], list[length - i - 1] = list[length - i - 1], list[i]

print(invert_list)