# 题目：输入某年某月某日，判断这一天是这一年的第几天？
try:
    year = int(input("年份："))
    month = int(input("月份："))
    day = int(input("日期："))
except ValueError:
    print("输入为非合法数字，请重新运行程序，并输入正确的数字！")
    exit()
except:
    print("发生了未知错误，请重新运行程序。")
    exit()

months_days = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

ans = day
for i in range(1, month):
    ans += months_days[i]

if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)) and month > 2:
    ans += 1

print(f"{year}年{month}月{day}日是今年的第{ans}天")

""" relection """
# 牢记闰年的判断条件
# 1. 如果年份能被4整除且不能被100整除，则是闰年。
# 2. 如果年份能被100整除，则必须同时能被400整除，才是闰年。