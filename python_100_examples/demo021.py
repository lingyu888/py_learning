# 题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，
# 还不过瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。
# 到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
# y = 1/2 x - 1
# x = 2 (y + 1)

def cal(days, res):
    # 第 n 天还没吃，需要 -1
    for day in range(days - 1):
        res = 2 * (res + 1)
    return res

days = 10   # 第 10 天吃完
res = 1 # 只剩下 1 个桃子

print(f"第一天共摘了{cal(days, res)}个桃子")

""" relection """
# TypeError: 'int' object is not iterable
# days 需要用 range()包起来