# 题目：求一个3*3矩阵主对角线元素之和。

a = [[1, 2, 3], 
     [4, 5, 6],
     [7, 8, 9]]

length_row = len(a)
length_col = len(a[0])
ans = 0

for i in range(length_row):
    ans += a[i][i]

print(ans)