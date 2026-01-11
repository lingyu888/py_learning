# 题目：列表排序及连接。

if __name__ == '__main__':
    a = [1, 3, 2]
    b = [3, 4, 5]
    
    a.sort()  # 对列表 a 进行排序
    print(a)  # 在 Python 3 中使用 print() 函数
    
    # 连接列表 a 与 b
    print(a + b)  # 使用 `+` 来连接列表
    
    # 使用 extend() 连接列表 a 与 b
    a.extend(b)  # 将列表 b 的所有元素添加到列表 a 中
    print(a)  # 输出修改后的列表 a