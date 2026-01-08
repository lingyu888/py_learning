#题目：打印出如下图案（菱形）:
"""
   *
  ***
 *****
*******
 *****
  ***
   *
"""

# range(start, stop, step)
def print_rhombus(num):
    len = num // 2 + 1
    # 上半段
    for i in range(1, len):
        spaces = ' ' * (len - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars + spaces)
    # 中间
    print('*' * num)
    # 下半段
    for i in range(len - 1, 0, -1):
        spaces = ' ' * (len - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars + spaces)

# 测试为奇数
num = 7
print_rhombus(num)