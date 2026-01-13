# 题目：列表使用实例。

def main():
    # list
    # 新建列表
    testList = [10086, '中国移动', [1, 2, 4, 5]]

    # 访问列表长度
    print(len(testList))

    # 获取列表从索引 1 到结尾的所有元素
    print(testList[1:])

    # 向列表添加元素
    testList.append('i\'m new here!')

    print(len(testList))
    # testList[-1]: 这是一个负索引，表示访问列表的最后一个元素。
    print(testList[-1])

    # 弹出列表的第二个元素，'中国移动'被输出并弹出
    print(testList.pop(1))
    print(len(testList))
    print(testList)

    # list comprehension
    # 后面有介绍，暂时掠过
    matrix = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

    print(matrix)
    print(matrix[1])

    # 获取矩阵的某一列
    col2 = [row[1] for row in matrix]  # 获取矩阵的第二列
    print(col2)

    # 过滤出偶数项
    col2even = [row[1] for row in matrix if row[1] % 2 == 0]  # 过滤掉奇数项
    print(col2even)

if __name__ == '__main__':
    main()