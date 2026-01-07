# 题目：输出 9*9 乘法口诀表。
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={i*j}", end=' ')
    print()

""" reflection """
# end 正常情况是换行，end='' 可以指定不换行，end=' ' 可以指定空格隔开