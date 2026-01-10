# 题目：画图，学用line画直线。

import tkinter as tk

if __name__ == '__main__':
    
    root = tk.Tk()

    canvas = tk.Canvas(width=400, height=400, bg='green')
    canvas.pack(expand=True, fill=tk.BOTH)

    x0 = 263
    y0 = 263
    y1 = 275
    for i in range(19):
        canvas.create_line(x0,y0,x0,y1, width=1, fill='red')
        x0 = x0 - 5
        y0 = y0 - 5
        y1 = y1 + 5
 
    x0 = 263
    y1 = 275
    y0 = 263
    for i in range(21):
        canvas.create_line(x0,y0,x0,y1, fill='red')
        x0 += 5
        y0 += 5
        y1 += 5
 
    root.mainloop()