# 题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。

def main():
    num = int(input('please input a odd number: '))
    flag = True # 整除标志位
    cnt = 1     # 9 的个数
    ans = 9     # 被除数

    while flag:
        if ans % num != 0:
            ans = ans * 10 + 9
            cnt += 1
            flag = True
        else:
            flag = False
            print(f'奇数 {num} 需要 {cnt} 个 9 ({ans})才能被整除')

if __name__ == '__main__':
    main()

""" reflection """
""" 
    在 Python 中，像 +=、-=、*=、/= 等运算符都属于 复合赋值运算符，
    它们的运作方式通常是 先计算右侧表达式的结果，再将这个结果与左侧变量进行运算，
    最后将运算后的结果赋值给左侧变量。
 """