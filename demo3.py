# task1: 在一个新的名字为"poem.txt"的文件里，写入以下内容：
# 我欲乘风归去，
# 又恐琼楼玉宇，
# 高处不胜寒，

# task2: 在上面的"poem.txt"文件结果处，添加以下内容：
# 起舞弄清影，
# 何似在人间。

""" 教程示例 """
# 读文件
# r: read, w: write, a: apend, r+: read + write + apend
# 当目录下没有文件时，w, a会自动创建文件
# 默认为 r
# 如果不加encoding="utf-8"，会乱码

# f_data = open("./poetry.txt", "r", encoding="utf-8")
# content = f_data.read()
# print(content)

# f_data.close()

# with open("./poetry.txt", "r", encoding="utf-8") as f_data:
#     content = f_data.read()
#     print(content)

# with open("./poetry.txt", "r", encoding="utf-8") as f_data:
#     print(f_data.readline())
#     print(f_data.readline())

# with open("./poetry.txt", "r", encoding="utf-8") as f_data:
#     lines = f_data.readlines()
#     for line in lines:
#         print(line)

""" 正儿八经 """
# 运行前可以将目录中 poem.txt 删除，程序会自动重建
with open("./poem.txt", "w", encoding="utf-8") as f_poem:
    # f_poem.write("我欲乘风归去，\n又恐琼楼玉宇，\n高处不胜寒，\n")
    f_poem.write("我欲乘风归去，\n")
    f_poem.write("又恐琼楼玉宇，\n")
    f_poem.write("高处不胜寒，\n")

with open("./poem.txt", "a", encoding="utf-8") as f_poem:
    f_poem.write("起舞弄清影，\n")
    f_poem.write("何似在人间。\n")