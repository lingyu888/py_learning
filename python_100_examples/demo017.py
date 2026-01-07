# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

import string
s = input('请输入一个字符串：')
cnt = 0
space = 0
num = 0
oth = 0
for c in s:
    if c.isalpha():
        cnt += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        num += 1
    else:
        oth += 1
print(f'char = {cnt}, space = {space}, digit = {num}, others = {oth}')

""" reflection """
# 唯一的作用就是 .is---() 判断，无聊