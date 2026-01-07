# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

a = int(input('a = '))
n = int(input('n = '))

ans = 0

for index in range(n):
    ans += (n - index) * a * 10**index

print(f'anser = {ans}')