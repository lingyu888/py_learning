# 题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n

def func_even(num):
    ans = 0
    for i in range(2, num + 1, 2):
        ans += 1 / i
    return ans
    
def func_odd(num):
    ans = 0
    for i in range(1, num + 1, 2):
        ans += 1 / i
    return ans

def main():
    num = int(input('please input a number: '))
    if num % 2 == 0: print(f'ans = {func_even(num)}')
    else: print(f'ans = {func_odd(num)}')

if __name__ == '__main__':
    main()