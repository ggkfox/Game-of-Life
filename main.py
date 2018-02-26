#---Game of Life---
#By: <Joshua Holland>

import sys
from tkinter import *
import time
import random

#-------GLOBAL VARIABLES-------
#number of viles vertically and horizonatally
h = 35
w = 85
#size of a single side of each tile.
size = 20
#arr[width][height]
arr = [[1 if random.randint(0,7)==2 else 0 for x in range(w)] for y in range(h)]
temp = [[0 for x in range(w)] for y in range(h)]

#-------Functions-------
def initializeValues():
    print("initializing array Values....")

def updateValues():
    global arr #apparently makes globals editable.
    global temp
    print("updating array values....")
    for i in range(h):
        for j in range(w):
            count = 0
            if arr[(i-1+h)%h][(j-1+w)%w] == 1: count += 1
            if arr[(i-1+h)%h][j]         == 1: count += 1
            if arr[(i-1+h)%h][(j+1+w)%w] == 1: count += 1
            if arr[i][(j-1+w)%w]         == 1: count += 1
            if arr[i][(j+1+w)%w]         == 1: count += 1
            if arr[(i+1+h)%h][(j-1+w)%w] == 1: count += 1
            if arr[(i+1+h)%h][j]         == 1: count += 1
            if arr[(i+1+h)%h][(j+1+w)%w] == 1: count += 1
            if arr[i][j] == 0 and count == 3: temp[i][j] = 1
            elif arr[i][j] == 1 and (count < 2 or count > 3): temp[i][j] = 0
            else: temp[i][j] = arr[i][j]
    arr = [[temp[i][j] for j in range(w)] for i in range(h)] #match arr to temp_array
    updateBoard()

def updateBoard():
    canvas.delete("all")
    for i in range(h):
        for j in range(w):
            xpos = j*size
            ypos = i*size
            rect = canvas.create_rectangle(xpos, ypos, xpos+size, ypos+size, fill='#FFF')
            if arr[i][j]==1:
                canvas.itemconfig(rect, fill='#99ccff')
            else: canvas.itemconfig(rect, fill='white')
    canvas.after(1, updateValues)


#-------Build Window-------
root = Tk()                     #This creates a window, but it won't show up
root.wm_title("Conway's Game of Life       by: Joshua Holland") #Makes the title that will appear in the top left
root.geometry("%dx%d+%d+%d" % (w*size, h*size+100, 130, 100))
canvas = Canvas(root, width=w*size, height=h*size, background='black')
canvas.pack()
play = Button(root, text="Play", command=updateBoard) #this command starts recursive algorithm.
play.pack()
root.mainloop()
