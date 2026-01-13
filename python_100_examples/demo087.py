# 题目：回答结果（结构体变量传递）。

class Student:
    x = 0
    c = 0
    def func(self):
        self.x = 20
        self.c = 'c'

def main():
    a = Student()
    a.x = 3
    a.c = 'a'
    print(a.x, a.c)
    
    a.func()
    print(a.x, a.c)

if __name__ == '__main__':
    main()