# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。

def bubble(arr):
    n = len(arr)
    for i in range(n):
        # 引入一个flag判定是否发生交换
        flag = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        # 如果没有交换，意味着已经有序，退出循环
        if not flag:
            break
    return arr


list = []
for i in range(3):
    x = int(input("请输入整数："))
    list.append(x)
# list.sort()
list = bubble(list)
print(list)

""" reflection """
# 如果直接输入x, y, z，索引的时候很难办，反复 if 很显然不是正解
# sort() 默认用的是冒泡排序，因此回顾一下冒泡排序
