# 题目：画图，学用circle画圆形。　

import tkinter as tk
# Tkinter 是 "Tk interface" 的合并简称，表示 Tk 库与 Python 之间的接口。

if __name__ == '__main__':
    # 创建一个 Tkinter 窗口
    root = tk.Tk()
    
    # 创建一个 Canvas 画布
    canvas = tk.Canvas(root, width=800, height=600, bg='yellow')
    canvas.pack(expand=True, fill=tk.BOTH)  # 使用 Tkinter 的新方式
    # expand: 允许画布扩展，但无论时候允许，后续的 BOTH 或 X 都可以让画布在 X 方向上扩展
    # fill: 在生成 GUI 窗口之后，可以利用 .X .Y .BOTH 来允许画布扩展

    # 初始化变量
    k = 1
    j = 1
    
    # 绘制多个圆
    for i in range(0, 26):
        canvas.create_oval(400 - k, 300 - k, 400 + k, 300 + k, outline='black', width=1)
        k += j
        j += 0.3
    
    # 启动事件循环
    root.mainloop()

""" reflection """
# Canvas 是 tkinter 模块中的一个类，它用于在 Tkinter 窗口中创建一个画布，
# 可以在上面绘制各种图形，如线条、矩形、圆形、文本等。
# Canvas 类提供了多种方法，可以帮助你绘制和操作这些图形对象

# Canvas 是一个非常灵活的控件，它可以用来绘制：
# 线条: create_line()
# 矩形: create_rectangle()
# 圆形: create_oval()
# 多边形: create_polygon()
# 文本: create_text()
# 图片: create_image()
# 甚至可以插入复杂的图形和自定义绘制。

# 保持界面：root.mainloop() 会让 Tkinter 窗口保持显示状态，并继续等待用户的交互。
# 没有它，窗口可能会在启动后立刻关闭。