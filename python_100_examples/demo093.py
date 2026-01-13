# 题目：时间函数举例3。

if __name__ == '__main__':
    import time
    start = time.perf_counter()  # 使用 perf_counter 代替 time.clock
    a = time.time()
    for i in range(3000):
        print(i)
    end = time.perf_counter()  # 同样使用 perf_counter 获取结束时间
    b = time.time()
    print('Difference is %6.3f' % (end - start))  # 输出耗时
    print('Difference is %6.3f' % (b - a))  # 输出耗时
