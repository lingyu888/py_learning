# 题目：画椭圆。　

import tkinter as tk

if __name__ == '__main__':

    root = tk.Tk()

    canvas = tk.Canvas(width=800, height=800, bg='white')
    canvas.pack(expand=True, fill=tk.BOTH)
    
    x = 360
    y = 160
    top = y - 30
    bottom = y - 30

    for i in range(20):
        canvas.create_oval(250 - top,250 - bottom,250 + top,250 + bottom)
        top -= 5
        bottom += 5
        
    root.mainloop()