import sys
from tkinter import *
import random

h = 20
w = 30
#arr[width][height]
arr = [[random.randint(0,1) for x in range(w)] for y in range(h)]

root = Tk()                     #This creates a window, but it won't show up
root.wm_title("Window Title") #Makes the title that will appear in the top left
root.config(background = "#FFFFFF")

def __init__():
    for i in range(h):
        for j in range(w):
            test = Frame(root, width=30, height=30, bg="#FFF")
            test.grid(row=i, column=j, padx=1, pady=1)
            if arr[i][j]==1:
                test.config(background = "#000")

__init__()

root.mainloop()
