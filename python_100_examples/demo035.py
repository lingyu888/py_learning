# 题目：文本颜色设置。

class bcolors:
    HEADER = '\033[95m'        # 紫色
    OKBLUE = '\033[94m'        # 蓝色
    OKGREEN = '\033[92m'       # 绿色
    WARNING = '\033[93m'       # 黄色（通常用于警告）
    FAIL = '\033[91m'          # 红色（通常用于错误）
    ENDC = '\033[0m'           # 结束标记（恢复默认颜色）
    BOLD = '\033[1m'           # 加粗
    UNDERLINE = '\033[4m'      # 下划线

print (bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC)
print(bcolors.OKGREEN + "这是绿色字体!" + bcolors.ENDC)  # 绿色字体
print(bcolors.FAIL + "这是红色字体!" + bcolors.ENDC)     # 红色字体
print(bcolors.BOLD + "这是加粗字体!" + bcolors.ENDC)      # 加粗字体
