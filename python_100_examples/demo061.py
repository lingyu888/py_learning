# 题目：打印出杨辉三角形（要求打印出10行如下图）。
# 1 
# 1 1 
# 1 2 1 
# 1 3 3 1 
# 1 4 6 4 1 
# 1 5 10 10 5 1 
# 1 6 15 20 15 6 1 
# 1 7 21 35 35 21 7 1 
# 1 8 28 56 70 56 28 8 1 
# 1 9 36 84 126 126 84 36 9 1
from sys import stdout

if __name__ == '__main__':
    
    num = 10    # 10 行
    list = []
    # list = [[]] * 10  # 有问题

    # 初始化一个二维数组
    for i in range(num):
        list.append([])
        for j in range(num):
            list[i].append([])

    # 先把两端都置1
    for i in range(num):
        list[i][0] = 1
        list[i][i] = 1
    
    # 杨辉三角关系
    for i in range(2, num):
        for j in range(1, i):
            list[i][j] = list[i-1][j-1] + list[i-1][j]
    
    # stdout.write()打印
    for i in range(10):
        for j in range(i + 1):
            stdout.write(str(list[i][j]))
            stdout.write(' ')
        print()
