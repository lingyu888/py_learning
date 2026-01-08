# 题目：利用递归方法求5!。

def fact(num):
    if num == 0:
        return 1
    elif num > 0:
        return num * fact(num - 1)

num = 5
print(f'5! = {fact(num)}')