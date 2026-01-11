# 题目：写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。

def my_len(s):
    cnt = 0
    for c in s:
        cnt += 1
    return cnt

def main():
    s = input('please input a string: ')
    print(f'length of s is {my_len(s)}')

if __name__ == '__main__':
    main()