# 题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。

def main():
    # 打开文件用于写入
    with open('test.txt', 'w') as fp:
        # 提示用户输入字符串
        string = input('Please input a string:\n')  # 使用 input() 替代 raw_input()
        # 将字符串转换为大写
        string = string.upper()
        # 将大写字符串写入文件
        fp.write(string)
    
    # 打开文件用于读取
    with open('test.txt', 'r') as fp:
        # 读取并打印文件内容
        print(fp.read())  # 使用 print() 函数打印内容

if __name__ == '__main__':
    main()