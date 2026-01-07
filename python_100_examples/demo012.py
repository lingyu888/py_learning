# 题目：判断101-200之间有多少个素数，并输出所有素数。
import math

def is_prime(num):
    sqrt_num = int(math.sqrt(num))
    for i in range(2, sqrt_num + 1):
        if num % i == 0:
            return False
    return True

primes = []
for number in range(101, 201):
    if is_prime(number):
        primes.append(number)
print(f"101-200之间共有{len(primes)}个素数，分别是：")
print(primes)