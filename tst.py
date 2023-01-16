
import tkinter as tk

root= tk.Tk()
root.title("Binoy")

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

header=tk.Label(root, text="MONTHLY CALCULATOR" , fg="green" ).place(x=110, y=0)

# increment y  by 3 for formating
head1 = tk.Label(root, text= "MONTHLY INCOME: ", fg="green").place(x=20,y= 40)
entry1 = tk.Entry(root) 
canvas1.create_window(300, 50, window=entry1)

head1 = tk.Label(root, text= "OTHER INCOME: ", fg="green").place(x=20,y= 70)
entry2 = tk.Entry(root) 
canvas1.create_window(300, 80, window=entry2)

head3 = tk.Label(root, text= "RENT: ", fg="green").place(x=20,y= 100)
entry3 = tk.Entry(root) 
canvas1.create_window(300, 110, window=entry3)

head4 = tk.Label(root, text= "MORTGAGE: ", fg="green").place(x=20,y= 130)
entry4 = tk.Entry(root) 
canvas1.create_window(300, 140, window=entry4)


def open():
    top = tk.Toplevel()
    top.title("Binoy")
    x1 = entry1.get()
    t1 = int(x1)
    
    x2 = entry2.get()
    t2 = int(x2)

    x3 = entry3.get()
    t3 = int(x3)
    
    x4 = entry4.get()
    t4 = int(x4)
    # add and subtract with this variable 
    total = (t1+t2) - (t3+t4)
        
    label1 = tk.Label(top, text=total,font=50).place(x=120,y=40)
    heading1= tk.Label(top, text="TOTAL: " , fg="green",font=50).place(x=40 , y=40)

   

button1 = tk.Button(root, text="GENERATE" ,command=open , fg="green" , bg="white" , width=30)
canvas1.create_window(200, 220, window=button1)


root.mainloop()
