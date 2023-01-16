import mysql.connector as my
import tkinter
from tkinter import *
from ttkthemes import themed_tk as kt
import tkinter as tk

mydb = my.connect(host="localhost", user="pawan", database="dietplanner", password="Pawan23.Krishnan")
c = mydb.cursor()

root = kt.ThemedTk()
root.title("Diet Planner Upload Module ")
root.resizable(False, False)
root.get_themes()
root.set_theme("radiance")

def getData():
    x1 = int(t1.get())
    x2 = str(t2.get())
    x3 = str(t3.get())
    x4 = str(t4.get()).upper()
    x5 = int(t5.get())
    x6 = int(t6.get())
    x7 = str(t7.get())
    x8 = str(t8.get()).upper()
    L = [x1,x2,x3,x4,x5,x6,x7,x8]
    print(ia.get())
    k = "lunch"
    """
    if (ia.get()) == 100:
        k += "breakfast"
    elif (ia.get()) == 101:
        k += "lunch"
    elif (ia.get()) == 102:
        k += "dinner"
    """
    t = [L,k]
    return t

def uploadData():
    L = getData()
    table  = L[1]
    id = L[0][0]
    name = L[0][1]
    cusine = L[0][2]
    type = L[0][3]
    calorie = L[0][4]
    rating = L[0][5]
    att = L[0][6]
    res = L[0][7]
    query = """insert into breakfast values(%s,%s,%s,%s,%s,%s,%s,%s)"""
    # change database here
    t = (id,name,cusine,type,calorie,rating,att,res)
    c.execute(query,t)
    mydb.commit()



canvas1 = tk.Canvas(root, width = 580, height = 350)
canvas1.pack()

a0 =  tk.Label(root,text="Food Upload:- ",font=20).place(x=10,y=10)

a1 = tk.Label(root,text="enter id of food: ").place(x=10,y=40)
a2 = tk.Label(root,text="enter name of food: ").place(x=10,y=80)
a3 = tk.Label(root,text="enter cusine: ").place(x=10,y=100)
a4 = tk.Label(root,text="enter type(V/N/P/O/Ve/Po/F): ").place(x=10,y=140)
a5 = tk.Label(root,text="enter total calories: ").place(x=10,y=160)
a6 = tk.Label(root,text="enter your rating: ").place(x=10,y=180)
a7 = tk.Label(root,text="enter food attribute(LC,HC,HP,MC,MP,LP): ").place(x=10,y=220)
a8 = tk.Label(root,text="enter allergic specifics(L/G/E/F/S/P/NON): ").place(x=10,y=260)

ia = StringVar(root)
r1 = tk.Radiobutton(root,text="Breakfast",value=1,variable=ia).place(x=10,y=300)
r1 = tk.Radiobutton(root,text="Lunch",value=2,variable=ia).place(x=120,y=300)
r1 = tk.Radiobutton(root,text="Dinner",value=3,variable=ia).place(x=220,y=300)



t1 = tk.Entry(root)
t1.place(x=380,y=40)

t2 = tk.Entry(root)
t2.place(x=380,y=80)
t3 = tk.Entry(root)
t3.place(x=380,y=100)
t4 = tk.Entry(root)
t4.place(x=380,y=140)
t5 = tk.Entry(root)
t5.place(x=380,y=160)
t6 = tk.Entry(root)
t6.place(x=380,y=180)
t7 = tk.Entry(root)
t7.place(x=380,y=220)
t8 = tk.Entry(root)
t8.place(x=380,y=260)

b1 = tk.Button(root,text="Submit",command=uploadData).place(x=380,y=300)








root.mainloop()