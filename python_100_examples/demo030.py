# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

""" solution 1 """
print('solution 1:')
# 利用 demo030 的思路，生成一个新的倒置的数，与原来的数进行比较

def invert(num):
    cnt = 0     # 记录位数
    rel = 0     # 记录余数
    x = num     # 用于后续修改 num
    y = 0   # 倒置后的数
    while x > 0:
        rel = x % 10
        y = y * 10 + rel
        x = x // 10
        cnt += 1
    return y

def is_palindrome(num):
    if num == invert(num):
        return True

num = int(input('请输入一个正整数：'))

if is_palindrome(num):
    print(f'数 {num} 是回文数')
else:
    print(f'数 {num} 不是是回文数')



""" solution 2 """
print('solution 2:')
# 将 int 转换成 str

def is_palindrome2(num):
    s = str(num)
    length = len(s)
    for i in range(length // 2 + 1):
        if not s[i] == s[length - i - 1]:
            return False
    return True

num = int(input('请输入一个正整数：'))
if is_palindrome2(num):
    print(f'数 {num} 是回文数')
else:
    print(f'数 {num} 不是是回文数')