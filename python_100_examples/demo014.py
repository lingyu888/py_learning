# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
# 从小到大找质数

""" solution 1 """

print(f"solution 1: ")
import math

global_prime = 0

def is_prime(num):
    global global_prime
    sqrt_num = int(math.sqrt(num))
    for i in range(2, sqrt_num + 1):
        if num % i == 0:
            global_prime = i
            return False
    return True

num = int(input("请输入正整数："))
print(f'{num}=', end ='')

# num 后续会被更改
var = num

# 如果 num 是质数直接返回
if is_prime(var):
    print(var)
    exit()

while not is_prime(var):
    print(f'{global_prime}', end = '*' if var // global_prime != 1 else '')
    var //= global_prime

print(var)


""" relection """
# 全部变量在函数中使用需要用 global 声明
# 熟练使用 = a if condition else b

""" solution 2 """

# 可以利用一个列表 factors[] 将所有质因数存储
# print('*'.join(map(str, factors)))
# map(str, factors) 将 factors 列表中的每个元素都 转换成字符串
# factors = [1, 2, 3] -> ['1', '2', '3']
# map(str, [1, 2, 3])  # 输出：['1', '2', '3']
# '*'.join(['1', '2', '3'])  # 输出：'1*2*3'
