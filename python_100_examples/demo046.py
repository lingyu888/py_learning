# 题目：求输入数字的平方，如果平方运算后小于 50 则退出。

while True:
    num = int(input('请输入一个整数：'))
    if num ** 2 < 50:
        print(f'{num}的平方为：{num**2}')
        print('平方小于50，程序结束！')
        exit()
        # break
        # continue  # 这个不行
    else:
        print(f'{num}的平方为：{num**2}')