# 题目：对10个数进行排序。

class bcolors:
    HEADER = '\033[95m'        # 紫色
    OKBLUE = '\033[94m'        # 蓝色
    OKGREEN = '\033[92m'       # 绿色
    WARNING = '\033[93m'       # 黄色（通常用于警告）
    FAIL = '\033[91m'          # 红色（通常用于错误）
    ENDC = '\033[0m'           # 结束标记（恢复默认颜色）
    BOLD = '\033[1m'           # 加粗
    UNDERLINE = '\033[4m'      # 下划线

list = [1, 5, 6, 8 ,4, 9, 5, 7, 6, 3]
length = len(list)
print(f'list: {list}')

""" solution 1 """
print(bcolors.OKBLUE + 'Bubble Sort:' + bcolors.ENDC)
# 冒泡排序

def bubble_sort(list, length):
    for i in range(length):
        for j in range(length - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

sorted_list = bubble_sort(list, length)

print(sorted_list)

""" soluition 2 """