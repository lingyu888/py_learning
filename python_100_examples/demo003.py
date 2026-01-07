# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

""" solution 1 """
# 假设整数为 x ,即 sqrt(x + 100) = 整数，sqrt(x + 268) = 整数
# 换言之： x = m^2 - 100, x = n^2 - 268
# n^2 - m^2 = 168
# 然后遍历 m 和 n
# try

ans = 0
max = 84
print(f"solution 1: ")
for m in range(1, max + 1):
    for n in range(m, max + 1):
        if (n + m) * (n - m) == 168:
            ans = m**2 - 100
            print(f"x = {ans}")

""" reflection """
# 循环需要有上限，因此需要继续分析
# (n + m)(n - m) = 168
# 那么最极限的情况下也就是 168 * 1
# 此时 n, m 的最大值也就是 168 / 2
# 即等于 84，那么max = 84
# solution 1 是嵌套 for 循环，时间成本过高，可以简化


""" solution 2 """
# solution 1 是直接求解 m 和 n
# 但也可以将 (n + m)(n - m) = 168 转换成 x*y = 168
# 先求解 x 和 y，再求解 m 和 n
# | n + m = i
# | n - m = j
# | m = (i - j) / 2
# | n = (i + j) / 2
# try
import math

ans = 0
max = int(math.sqrt(168))
print(f"solution 2: ")
for i in range(1, max + 1):
    # i 是 168 的因子
    if 168 % i == 0:
        j = 168 / i
        if (i - j) % 2 == 0:
            m = (i - j) / 2
            ans = m**2 - 100
            print(f"x = {ans}")

""" reflection """
# 由于是直接求解，此时的范围是 168 的开方
# 输出里会有小数，意味着 m 和 n 的输出是小数
# 回退回去也就是 (i + j) / 2 和 (i - j) / 2 存在小数
# 用 if 把这些值删掉