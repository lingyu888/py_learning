# 题目：求100之内的素数。

def is_fact(num):
    if num > 1:
        for i in range(2, num // 2 + 1):
            if (num % i) == 0:
                return False
        return True

lower = int(input('请输入区间下限：'))
upper = int(input('请输入区间上限：'))
list = []   # 存放区间内的质数

for num in range(lower, upper + 1):
    if is_fact(num):
        list.append(num)

print(list)