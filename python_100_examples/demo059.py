# 题目：画图，综合例子。　　
# 程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。。

import tkinter as tk
import math

if __name__ == '__main__':
    # 创建主窗口
    root = tk.Tk()
    
    # 创建 Canvas 画布，设置大小和背景色
    canvas = tk.Canvas(root, width=3000, height=3000, bg='green')
    canvas.pack(expand=True, fill=tk.BOTH)  # 使用 True 和 tk.BOTH 替代 YES 和 BOTH
    
    x0 = 1500
    y0 = 800
    
    # 绘制多个圆
    canvas.create_oval(x0 - 100, y0 - 100, x0 + 100, y0 + 100)
    canvas.create_oval(x0 - 200, y0 - 200, x0 + 200, y0 + 200)
    canvas.create_oval(x0 - 500, y0 - 500, x0 + 500, y0 + 500)
    
    B = 0.809  # 这个值控制椭圆的形状
    
    # 绘制16条从中心到边缘的红色线段
    for i in range(16):
        a = 2 * math.pi / 16 * i
        x = int(x0 + 480 * math.cos(a))  # 用 int() 将结果转换为整数
        y = int(y0 + 480 * math.sin(a) * B)
        canvas.create_line(x0, y0, x, y, fill='red')
    
    canvas.create_oval(x0 - 60, y0 - 60, x0 + 60, y0 + 60)
    
    # 绘制螺旋线
    for k in range(501):
        for i in range(17):
            a = (2 * math.pi / 16) * i + (2 * math.pi / 180) * k
            x = int(x0 + 480 * math.cos(a))
            y = int(y0 + 480 * math.sin(a) * B)
            canvas.create_line(x0, y0, x, y, fill='red')
        for j in range(51):
            a = (2 * math.pi / 16) * i + (2 * math.pi / 180) * k - 1
            x = int(x0 + 480 * math.cos(a))
            y = int(y0 + 480 * math.sin(a) * B)
            canvas.create_line(x0, y0, x, y, fill='blue')
    
    # 启动 Tkinter 主事件循环
    root.mainloop()

