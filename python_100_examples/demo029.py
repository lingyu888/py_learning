# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

""" solution 1 """
print('soution 1: ')

def print_i(num):
    cnt = 0     # 记录位数
    rel = 0     # 记录余数
    x = num     # 用于后续修改 num
    while x > 0:
        rel = x % 10
        print(rel, end = ' ')
        x = x // 10
        cnt += 1
    print(f'\n这个数是 {cnt} 位数')

num = int(input('请输入一个正整数'))

print_i(num)

""" solution 2 """
# 暴力拆解出每一位数
# eg: x // 10000, x // 1000, x // 100...