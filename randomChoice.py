from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from PIL import Image,ImageTk
import os

root = Tk()
canvas1 = tk.Canvas(root,width=400,height=100)
img = Image.open("/home/pawan/Desktop/DietPlanner V2/aplha 1.1/pic/userImages/pawan223.jpg")
image = img.resize((100, 50), Image.ANTIALIAS)
image2 = ImageTk.PhotoImage(image)
a = Label(canvas1, image = image2).place(x=100,y=10)
canvas1.pack()
root.mainloop()