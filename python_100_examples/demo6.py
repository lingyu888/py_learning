# 题目：斐波那契数列。
# 0、1、1、2、3、5、8、13、21、34、……。
# 输出第 n 个裴波那契数

""" solution 1 """
n = int(input("请输入你想要的裴波那契数列序号："))
print(f"solution 1: ")
# 数组序号从 0 开始，一开始就 -1，免得后面混淆
index = n - 1

list = [0, 1]
if index < 2:
    print(f"第 {n} 个裴波那契数为：{list[index]}")
    exit()

for i in range(2, n):
    # list[index] = list[index-1] + list[index-2]
    list.append(list[i-1] + list[i-2])
print(f"第 {n} 个裴波那契数为：{list[index]}")

""" relection """
# "菜鸟100"给的答案不对，第 10 个斐波那契数为 34，他的索引第 1 个是 1，正常应该第 1 个是 0

""" solution 2 """
# 利用递归求解
print(f"solution 2: ")
def fib(n):
    if n == 1:
        return 0
    if n == 2 or n == 3:
        return 1
    return fib(n-1) + fib(n-2)
print(f"第 {n} 个裴波那契数为：{fib(n)}")