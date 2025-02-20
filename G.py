import tkinter as tk

win = tk.Tk()

canvas = tk .Canvas(win ,bg="yellow" ,)
canvas.pack()
win.bind("<KeyPress>", move_by_keys)
win.mainloop()