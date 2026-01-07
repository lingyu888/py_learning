# 题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
def is_lili(num):
    flag = num
    ans = 0
    while flag > 0:
        re = flag % 10
        ans += re ** 3
        flag //= 10
    return ans == num

cnt = 0
for num in range(100, 1000):
    if is_lili(num):
        print(num, end = ' ')
        cnt += 1
print(f"\n一共有 {cnt} 个水仙数")

""" reflection """
# '/'：普通除法，结果为浮动小数
# '//'：整数除法，用于进行向下取整除法