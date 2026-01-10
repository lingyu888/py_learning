# 题目：有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数


""" solution 1 """
print('solution 1: ')

if __name__ == '__main__':
    # 输入整数列表
    list = []
    nums = 7  # 定义列表长度为 7
    for i in range(nums):
        list.append(int(input('please input a number: ')))

    print("Original list:", list)

    cnt = 3  # 需要将前 3 个元素移动到列表的末尾

    # 通过切片操作将列表分为两部分并交换位置
    list = list[-cnt:] + list[:-cnt]

    print("List after moving:", list)


""" solution 2 """
print('solution 2: ')

if __name__ == '__main__':
    # 输入整数列表
    list = []
    nums = 7  # 定义列表长度为 7
    for i in range(nums):
        list.append(int(input('please input a number: ')))

    print("Original list:", list)

    cnt = 3  # 需要将前 3 个元素移动到列表的末尾

    # 模拟循环移位
    for i in range(nums - cnt):
        list.append(list.pop(0))  # 把第一个元素移到末尾

    print("List after moving:", list)


""" solution 3 """
print('solution 3: ')

def move(list, nums, cnt):
    list_end = list[nums - 1]
    for i in range(nums - 1, 0, -1):
        list[i] = list[i - 1]
    list[0] = list_end
    cnt -= 1
    if cnt > 0:
        move(list, nums, cnt)  # 递归调用

if __name__ == '__main__':
    # 输入整数列表
    list = []
    nums = 7  # 定义列表长度为 7
    for i in range(nums):
        list.append(int(input('please input a number: ')))

    print("Original list:", list)

    cnt = 3  # 需要将前 3 个元素移动到列表的末尾
    move(list, nums , cnt)

    print("List after moving:", list)