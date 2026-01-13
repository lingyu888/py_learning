# 题目：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：
# 每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。


def main():
    num = int(input('please input a number: '))
    ans = []

    for i in range(4):
        res = num % 10
        num = num // 10
        ans.append((res + 5) % 10)
    
    # 在 .append 的时候已经相当于 reverse了，所以下一步无需重复
    # ans.reverse()
    # ans[0], ans[3] = ans[3], ans[0]
    # ans[1], ans[2] = ans[2], ans[1]

    for i in range(4):
        print(ans[i], end = '')

if __name__ == '__main__':
    main()