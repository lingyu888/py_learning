# 题目：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。

def main():
    num =  7    # 读数个数
    for i in range(num):
        cnt = int(input('please input a number: '))
        print('*' * cnt)

if __name__ == '__main__':
    main()