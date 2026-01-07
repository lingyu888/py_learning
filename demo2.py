# 类继承练习：人力系统
class Employee:
    def __init__(self, em_name, em_id):
        self.name = em_name
        self.id = em_id

    def print_info(self):
        print(f"employee: {self.name}, id: {self.id}")

class FullTimeEmployee(Employee):
    def __init__(self, em_name, em_id, em_mon_sal):
        super().__init__(em_name, em_id)
        self.monthly_salary = em_mon_sal
    def cal_mon_sal(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, em_name, em_id, em_dai_sal, em_work_days):
        super().__init__(em_name, em_id)
        self.daily_salary = em_dai_sal
        self.work_days = em_work_days

    def cal_mon_sal(self):
        mon_sal = self.daily_salary * self.work_days
        return mon_sal

zhangsan = FullTimeEmployee("张三", "20260107", 3000)
lisi = PartTimeEmployee("李四", "20250106", 200, 18)

zhangsan.print_info()
print(zhangsan.cal_mon_sal())

print(lisi.cal_mon_sal())