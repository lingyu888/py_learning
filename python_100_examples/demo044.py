# 两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
import numpy as np

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

length_row = len(X)
length_rol = len(X[0])

Z = np.zeros((length_row, length_row), dtype = int)

for row in range(length_rol):
    for rol in range(length_rol):
        Z[row][rol] = X[row][rol] + Y[row][rol]

print(Z)