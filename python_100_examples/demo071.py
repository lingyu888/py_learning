# 题目：编写input()和output()函数输入，输出5个学生的数据记录。

class Student:
    def __init__(self, stu_name, stu_id):
        self.name = stu_name
        self.id = stu_id

def my_inp(students):
    stu_name = input('Please input the student name: ')
    stu_id = input('Please input the student ID: ')
    student = Student(stu_name, stu_id)
    students.append(student)

    # students[stu_name] = student  # 用字典存储学生对象

def my_outp(students):
    print("\nStudent Records:")
    for student in students:
        print(f"Name: {student.name}, ID: {student.id}")

def main():
    num = 5  # 学生数
    students = []  # 用于存储学生对象

    # students = {}  # 用字典存储学生对象

    for i in range(num):
        print(f"Enter details for student {i+1}:")
        my_inp(students)

    my_outp(students)

if __name__ == '__main__':
    main()

