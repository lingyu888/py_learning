# 题目：八进制转换为十进制

def o2d(num):
    ans = 0
    index = 0
    while num > 0:
        re = num % 10
        ans += re * 8 ** index
        num = num // 10
        index += 1
    return ans

def main():
    num = int(input('please input a number: '))
    print(f'The result of converting the octal number {num} to decimal is: {o2d(num)}')

if __name__ == '__main__':
    main()