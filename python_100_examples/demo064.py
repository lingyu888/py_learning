# 题目：利用ellipse 和 rectangle 画图。

import tkinter as tk

if __name__ == '__main__':

    root = tk.Tk()

    canvas = tk.Canvas(width=400, height=600, bg='white')
    canvas.pack(expand=True, fill=tk.BOTH)
    
    left = 20
    right = 50
    top = 50
    num = 15
    for i in range(num):
        canvas.create_oval(250 - right,250 - left,250 + right,250 + left)
        canvas.create_oval(250 - 20,250 - top,250 + 20,250 + top)
        canvas.create_rectangle(20 - 2 * i,20 - 2 * i,10 * (i + 2),10 * ( i + 2))
        right += 5
        left += 5
        top += 10

    root.mainloop()

