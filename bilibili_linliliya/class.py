class Student:
    def __init__(self, stu_name, stu_id):
        self.name = stu_name
        self.id = stu_id
        self.grades = {"ch": 0, "ma": 0, "en": 0,}
    def set_grades(self, course, grade): 
        if course in self.grades:
            self.grades[course] = grade
    def print_grades(self):
        print(f"student:{self.name}(id:{self.id})'s grades are : " )
        for course in self.grades:
            print(f"{course}:{self.grades[course]}")
chen = Student("chen", "20517")
zeng = Student("zeng", "20618")

print(chen.id)

zeng.set_grades("ma", 95)

print(zeng.grades)

zeng.print_grades()