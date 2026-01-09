# 题目：有一个已经排好序的数组。
# 现输入一个数，要求按原来的规律将它插入数组中。

list = [1, 5, 6, 8 ,4, 9, 5, 7, 6, 3]
print(f'list: {list}')

def bubble_sort(list):
    length = len(list)
    for i in range(length):
        for j in range(length - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

sorted_list = bubble_sort(list)

print(f'sorted_list:{sorted_list}')

num = int(input('请输入要插入的数：'))

sorted_list.append(num)
sorted_list = bubble_sort(sorted_list)
print(f'sorted_list:{sorted_list}')