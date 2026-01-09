# 题目：按逗号分隔列表。

""" solution 1 """
print(f'solution 1:')

def insert_comma(list):
    insert_list = [str(list[0])]
    for c in list[1:]:
        insert_list.append(',')
        insert_list.append(str(c))
    # return insert_list
    return ''.join(insert_list)

list = [1, 2, 3, 4, 5]
print(insert_comma(list))

""" reflection """
# 如果直接 return insert_list
# 输出：['1', ',', '2', ',', '3', ',', '4', ',', '5']
# 需要用''.join将列表中的元素连接成字符串

# 'a'.join(b) 可以将任意的字符 a ('', ' ', '-', '\n', etc.) 插入到 列表 b 中


""" solution 2 """
print(f'solution 2:')

list = [1, 2, 3, 4, 5]

insert_list = ','.join(map(str, list))

print(insert_list)

""" reflection """
# list = [1, 2, 3, 4, 5]
# result = map(str, list)
# print(list(result))  # 输出：['1', '2', '3', '4', '5']

# map(function, iterable, ...)
# map() 返回一个迭代器对象(map 对象),
# 通过 list()、tuple() 等函数将其转换为一个具体的列表或元组等类型才能查看内容。

# # 示例 1：将每个数字加倍
# numbers = [1, 2, 3, 4, 5]
# result = map(lambda x: x * 2, numbers)
# # 通过 list() 查看结果
# print(list(result))  # 输出：[2, 4, 6, 8, 10]

# # 示例 2：同时遍历两个列表，计算它们的和
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# result = map(lambda x, y: x + y, list1, list2)
# print(list(result))  # 输出：[5, 7, 9]

# # 示例 3：将数字列表转换为字符串列表
# numbers = [1, 2, 3, 4, 5]
# result = map(str, numbers)
# print(list(result))  # 输出：['1', '2', '3', '4', '5']





