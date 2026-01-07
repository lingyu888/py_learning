# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

cnt = 0   

for i in range(1, 5):
    for j in range(1, 5):
        if j != i:
            for k in range(1, 5):
                if (k != i) and (k != j):
                    ans = i * 100 + j * 10 + k
                    cnt += 1
                    print(ans)


print(f"一可以组成 {cnt} 个无重复数字的三位数")