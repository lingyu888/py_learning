# 题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

# 找出所有的因数
def found_factor(num):
    list = [1]
    for index in range(2, num//2 + 1):
        if num % index == 0:
            list.append(index)
    list.sort()
    return list

# 检查是否为完数
def is_fin(num):
    list = found_factor(num)
    return sum(list) == num

# 遍历并保存
nums = []
for index in range(2, 1001):
    if is_fin(index):
        nums.append(index)

print(f"1000以内的完数有：{nums}")

""" relefction """
# 在 found_factor(num) 函数中，range 上限需要为 num // 2 + 1
# 以确保当 num 为偶数时，num / 2在其中
