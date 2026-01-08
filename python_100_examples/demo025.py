# 题目：求1+2!+3!+...+20!的和。

# 和 demo024 相似，可以使用历史数据
# 例如 3! = 2! * 3

num = 20    # 前 20 项求和
ans = 0
v = 1   # 第 1 项值

for i in range(1, num + 1):
    v *= i
    ans += v
print(f"前{num}项求和为{ans}")