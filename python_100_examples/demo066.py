# 题目：输入3个数a,b,c，按大小顺序输出。

if __name__ == '__main__':

    def bubble_sort(list, length):
        for i in range(length):
            for j in range(length - i - 1):
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
        return list

    list = []
    num = 3

    for i in range(num):
        x = int(input('please input a number: '))
        list.append(x)

    sorted_list = bubble_sort(list, num)
    
    print(sorted_list)