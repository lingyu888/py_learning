# 题目：统计 1 到 100 之和。

ans = 0
for i in range(1, 101):
    ans += i
print(f'1 + 2 + ... + 100 = {ans}')