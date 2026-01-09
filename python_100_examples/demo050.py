# 题目：使用 random 模块输出一个随机数。

import random

print(random.uniform(10, 20))

""" reflection """
# random.random()：返回一个 [0.0, 1.0) 区间的随机浮点数
# random.randint(a, b)：返回一个随机整数，范围为 [a, b]，即包括 a 和 b。
# random.uniform(a, b)：返回一个随机浮点数，范围为 [a, b]，即包括 a 和 b。
# random.choice(sequence)：从非空序列（如列表、元组或字符串）中随机选择一个元素。
# random.sample(population, k)：从总体中随机选择 k 个独立的元素，并返回一个新列表。population 是序列或集合，k 是需要选择的元素个数。
# random.shuffle(sequence)：打乱一个可变序列（如列表），并在原地修改该序列。
# random.seed(a=None)：初始化随机数生成器的种子。如果你为 seed 提供一个固定值（例如数字或字符串），那么每次运行代码时生成的随机数序列都会相同。否则，它会使用当前时间戳作为种子。
# random.gauss(mu, sigma)：返回一个符合正态分布（高斯分布）的随机浮点数。mu 是均值，sigma 是标准差。
# random.choice([True, False])：随机返回 True 或 False。
