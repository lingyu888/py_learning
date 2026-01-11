# 题目：放松一下，算一道简单的题目。

if __name__ == '__main__':
    for i in range(5):
        n = 0
        if i != 1: n += 1
        if i == 3: n += 1
        if i == 4: n += 1
        if i != 4: n += 1
        # round 1: 1, 4
        # round 2: 4
        # round 3: 2, print
        if n == 3: print(64 + i)