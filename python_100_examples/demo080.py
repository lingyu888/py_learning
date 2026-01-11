# 题目：海滩上有一堆桃子，五只猴子来分。
# 第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。
# 第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，
# 第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？
# 4 / 5 * ((4 / 5 * (x - 1)) - 1)) ... = 整数

def cal(num):

    j = 1
    cnt = 0 # 确保是整数，迭代找
    ans = 0 # 最后一次分成了 5 份，且拿走 1 份，至少是 4 的倍数，这里随便取，初始化时会 *4
    # 注意 ans 是 4, 8, 12, ... 因此需要引入 j 

    while cnt < 4:
        ans = 4 * j
        for cnt in range(num):
            if (ans % 4 != 0):
                break
            else:
                cnt += 1
            ans = (ans / 4) * 5 + 1
        j += 1
    return ans

def main():
    num = 5
    print(f'最少有 {cal(num)} 个桃子')

if __name__ == '__main__':
    main()

    for cnt in range(5):  # cnt 会从 0 到 4
        print(f'Before incrementing: {cnt}')
        cnt += 2  # 修改 cnt 的值
        print(f'After incrementing: {cnt}')

""" reflection """
# for 循环中的 cnt += 1 会依照迭代器自加，但是不影响迭代器从1 -> 2, 2-> 3

# Before incrementing: 0
# After incrementing: 2
# Before incrementing: 1
# After incrementing: 3
# Before incrementing: 2
# After incrementing: 4
# Before incrementing: 3
# After incrementing: 5
# Before incrementing: 4
# After incrementing: 6