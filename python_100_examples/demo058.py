# 题目：画图，学用rectangle画方形。

import tkinter as tk

if __name__ == '__main__':

    root = tk.Tk()

    canvas = tk.Canvas(width=400, height=400, bg='green')
    canvas.pack(expand=True, fill=tk.BOTH)

    root.title('方形')
    
    x0 = 263
    y0 = 263
    y1 = 275
    x1 = 275
    for i in range(19):
        canvas.create_rectangle(x0,y0,x1,y1,)
        x0 -= 5
        y0 -= 5
        x1 += 5
        y1 += 5
         
    root.mainloop()
