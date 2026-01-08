# 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；
# 再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

initial_height = 100    # 初始高度
s = 0   # 路程
num = 10    # 第 n 次反弹
ans = initial_height

for i in range(num):
    ans += initial_height
    initial_height = initial_height / 2

# 先落地，后反弹，在外面 +100 已经落地一次了
ans -= initial_height * 2

print(f"总共经过了{ans}米")
print(f"第{num}次反弹高度为{initial_height}米")