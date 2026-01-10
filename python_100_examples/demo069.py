# 题目：有n个人围成一圈，顺序排号。
# 从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。

def main():
    nmax = int(input('please input a numbner: '))   
    nums = []
    for i in range(1, nmax + 1):
        nums.append(i)

    cnt = 0     # 被淘汰的总人数
    flag = 0    # =3 时淘汰（置零）
    index = 0   # 循环数

    while cnt < nmax - 1: 
        # 报数
        if nums[index] != 0: 
            flag += 1
        # 淘汰
        if flag == 3: 
            flag = 0
            nums[index] = 0
            cnt += 1
        # 循环
        index += 1
        # 重新循环
        if index == nmax:
            index = 0

    for i in range(nmax):
        if nums[i] != 0:
            print(f'最后留下的是第 {i + 1} 位')

if __name__ == '__main__':
    main()