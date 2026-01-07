# 题目：利用条件运算符的嵌套来完成此题：
# 学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

grade = int(input('请输入成绩：'))

if grade >= 90:
    print('A')
elif grade >= 60:
    print('B')
else:
    print('C')