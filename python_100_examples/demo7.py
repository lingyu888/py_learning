# 题目：将一个列表的数据复制到另一个列表中。
a = [1, 2, 3, 4]
# b = a[:]
b = a.copy()
print(f"b:{b}")

""" reflection """
# b = a 虽然使 print(b) 和 a 一样，但实际上是创建了对 a 列表的引用，修改 b 的同时会修改 a
# a = [1, 2, 3, 4]
# b = a
# print(f"b:{b}")
# b[0] = 2
# print(f"b:{b}")
# print(f"a:{a}")