def cal(num1, num2, calculator, formatter):
    result = calculator(num1, num2)
    formatter(num1, num2, result)

def calculate_power(num1, num2): 
    return num1 ** num2

def calculate_add(num1, num2):
    return num1 + num2

def calculate_sub(num1, num2):
    return num1 - num2

def print_with_vertical_bar(num1, num2, result):
    print(f""" 
    | 数字参数 | {num1}, {num2} |
    | 计算结果 | {result} |""")

cal(5, 6, calculate_power, print_with_vertical_bar)

cal(123, 345, calculate_add, print_with_vertical_bar)

cal(43, 21, calculate_sub, print_with_vertical_bar)