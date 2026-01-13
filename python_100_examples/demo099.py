# 题目：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列),
#  输出到一个新文件C中。

def main():
    # 写入并读取 A.txt
    with open('A.txt', 'w') as fp:
        a = input('Please input a string for A.txt: ')
        fp.write(a)

    # 写入并读取 B.txt
    with open('B.txt', 'w') as fp:
        b = input('Please input a string for B.txt: ')
        fp.write(b)

    # 读取两个文件内容并合并
    with open('A.txt', 'r') as fp:
        a_read = fp.read()

    with open('B.txt', 'r') as fp:
        b_read = fp.read()

    # 合并并按字母顺序排序
    merged = sorted(a_read + b_read)

    # 将合并且排序后的内容写入 C.txt
    with open('C.txt', 'w') as fp:
        fp.write(''.join(merged))  # 将排序后的列表合并为字符串并写入文件

    print("The merged and sorted string has been written to C.txt.")

if __name__ == '__main__':
    main()

""" reflection """
"""
在下述这种写法中，write() 会将内容写入文件，
而在使用 write() 后文件指针会移到文件的末尾，所以下面的 read() 读取不到内容。
with open('A.txt', 'w') as fp: 
    a = input('please input a string: ') 
    fp.write(a) 
    a_read = fp.read() 
    fp.close()

"""