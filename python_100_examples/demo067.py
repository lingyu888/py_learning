# 题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。

def inp(list, nums):
    for i in range(nums):
        num = int(input('please input a number: '))
        list.append(num)
    return list
    
def find_max_min(list, nums):
    max = 0
    min = 0
    for i in range(nums):
        if list[i] > list[max]:   max = i
        if list[i] < list[min]:   min = i
    return max,min

def exchange(list, nums, max, min):
    list[0], list[max] = list[max], list[min]
    list[nums-1], list[min] = list[min], list[nums-1]

if __name__ == '__main__':
    list = []
    nums = 5
    list  = inp(list, nums)
    
    print(list)

    max, min = find_max_min(list, nums)
    exchange(list, nums, max, min)

    print(list)

""" reflection """
# 在 Python 中，当你把一个列表传递给函数时，实际上是传递该列表的 引用，
# 也就是说，函数内对该列表的任何修改都会影响原始列表。