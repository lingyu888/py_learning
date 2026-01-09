# 题目：练习函数调用。
# 程序分析：使用函数，输出三次 RUNOOB 字符串。

# print 内容
def print_string(s):
    print(s)

# print 次数
def print_nums(s, nums):
    for i in range(nums):
        print_string(s)

if __name__ == '__main__':
    s = 'RUNOOB'
    nums = 3
    print_nums(s, nums)