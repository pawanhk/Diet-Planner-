import mysql.connector as my
import tkinter as tk
from PIL import ImageTk,Image
import random
from ttkthemes import themed_tk as kt
from tkinter import filedialog
import datetime
root = kt.ThemedTk()
root.title("Diet Planner")
root.resizable(False, False)
root.get_themes()
root.set_theme("radiance")
import webbrowser
canvas1 = tk.Canvas(root, width = 500, height = 250)
canvas1.pack()

header = tk.Label(root, text="Welcome To Diet Planner").place(x=170, y=0)

header1 = tk.Label(root, text="Login:- ").place(x=20, y=40)

head1 = tk.Label(root, text= "Username: ").place(x=20,y= 80)
entry1 = tk.Entry(root)
canvas1.create_window(300, 90, window=entry1)

head1 = tk.Label(root, text= "Password: ").place(x=20,y= 120)
entry2 = tk.Entry(root)
canvas1.create_window(300, 130, window=entry2)
def Login():
    def Login():
        mydb = my.connect(host="localhost", user="pawan", database="dietplanner", password="Pawan23.Krishnan")
        c = mydb.cursor()
        x1 = str(entry1.get())
        x2 = str(entry2.get())
        c.execute("select fname,password from users ")
        g = c.fetchall()
        for i in g:
            if i[0] == x1 and i[1] == x2:
                ProfileRun(x1)
            else:
                e3 = tk.Label(root, text="username or password is incorrect !", fg="red").place(x=120, y=220)
def ProfileRun(x1):
    mydb = my.connect(host="localhost", user="pawan", database="dietplanner", password="Pawan23.Krishnan")
    c = mydb.cursor()
    # root stuff
    root  = tk.Tk()
    root.title("profile")
    root.resizable(False,False)
    fnameI  = "we"
    imageID = "we106"
    emailI = "we"

    def displayPicture(imgID):
        path = "/home/pawan/Desktop/DietPlanner V2/aplha 1.1/pic/userImages/"
        fpath  = path+str(imgID)+".jpg"
        img = Image.open(fpath)
        image = img.resize((100,100), Image.ANTIALIAS)
        image2 = ImageTk.PhotoImage(image)
        return image2

    def exiter():
        exit()
    def signOut():
        pass
    canvas1 = tk.Canvas(root,width=900,height=45,bg="gray")
    a1 = tk.Label(canvas1,text="Profile Page:- ",font=50).place(x=10,y=10)
    b1 = tk.Button(canvas1,text="Exit",command=exiter).place(x=730,y=7)
    b2 = tk.Button(canvas1,text="Log-Out",command=signOut).place(x=800,y=7)
    canvas1.pack()
    canvas2 = tk.Canvas(root,width=900,height=500)
    # get user info
    query = "select * from users where fname=%s and imageID=%s"
    t = (fnameI,imageID)
    c.execute(query,t)
    g = c.fetchall()
    for i in g:
        fnameD  = i[1]
        lnameD  = i[2]
        email  = i[3]
        profile_picture = i[4]
        bio = i[5]
        imgID = i[7]
        image = displayPicture(imgID)


    # mid section

    a = tk.Label(canvas2,text="Profile Info",font=530).place(x=380,y=12)
    a = tk.Label(canvas2, image=image).place(x=380, y=40)
    a1 = tk.Label(canvas2,text="name: ",font=300).place(x=340,y=150)
    a1 = tk.Label(canvas2,text=fnameD,font=300).place(x=440, y=150)
    a1 = tk.Label(canvas2,text=lnameD,font=300).place(x=500, y=150)

    a2 = tk.Label(canvas2,text="email: ",font=300).place(x=340,y=180)
    a2 = tk.Label(canvas2,text=email, font=300).place(x=440,y=180)

    a3 = tk.Label(canvas2,text="bio: ",font=300).place(x=340,y=210)
    a3 = tk.Label(canvas2,text=bio, font=300).place(x=440,y=210)

    a4 = tk.Label(canvas2,text="status: ",font=300).place(x=340,y=240)
    a4 = tk.Label(canvas2,text="user", font=300).place(x=440,y=240)

    # friends
    a1 = tk.Label(canvas2,text="Your Friends",font=500).place(x=10,y=10)
    def makeRelation(e1,e2):
        email1 = e1
        email2 = e2
        req = "yes"
        status = "pending"

        # check if already sent
        query3 = """
        insert into friends (email,femail,req,status) values(%s,%s,%s,%s)
        """
        t4 = (email1,email2,req,status)
        c.execute(query3,t4)
        mydb.commit()

    # search friends
    def makeFriends(canvas):
        a22 = tk.Label(canvas2, text="*user has been located*     ", fg="green").place(x=10, y=300)
        x1 = str(entry1.get())
        proceed = True
        if x1 == email:
            proceed = False

        if proceed == True:
            try:
                que = "select fname,lname,email,imageID from users where email = %s"
                t2 = (x1,)
                c.execute(que,t2)
                q = c.fetchall()
                for i in q:
                    ffname = i[0]
                    fflname = i[1]
                    ffemail = i[2]
                    ffimageID = i[3]
                lt = [ffname,fflname,ffemail,ffimageID]
            except UnboundLocalError:
                a22 = tk.Label(canvas2, text="*user cannot be located*", fg="red").place(x=10, y=300)
                pass

            # check if request is pending
            # check if already friends
            cond = True
            que1 = "select status from friends where email=%s and femail=%s"
            t3 = (email,ffemail)
            c.execute(que1,t3)
            f = c.fetchall()
            for i in f:
                if i[0] == "yes":
                    print("yes")
                    cond = False
                elif i[0] == "pending":
                    print("pending")
                    cond = 23
            # display friend information
            print(lt)
            fileF = r"/home/pawan/Desktop/DietPlanner V2/aplha 1.1/pic/userImages/"
            fileFF = fileF + str(lt[3]) + ".jpg"
            img = Image.open(fileFF)
            image = img.resize((100, 100), Image.ANTIALIAS)
            image2 = ImageTk.PhotoImage(image)
            canvas2.image2 = image2
            a11 = tk.Label(root,image=image2).place(x=10,y=400)
            a12 = tk.Label(canvas2,text="name: ",font=300).place(x=120,y=350)
            a12 = tk.Label(canvas2,text=lt[0],font=300).place(x=200,y=350)
            a12 = tk.Label(canvas2,text=lt[1],font=300).place(x=260,y=350)

            a13 = tk.Label(canvas2,text="email: ",font=300).place(x=120,y=390)
            a13 = tk.Label(canvas2,text=lt[3],font=300).place(x=200,y=390)
            # add friends
            if cond == True:
                b4  = tk.Button(canvas2,text="request follow    ",fg="green",command=lambda: makeRelation(email,ffemail),font=300).place(x=120,y=420)
            elif cond == False:
                b4  = tk.Button(canvas2,text="already friends      ",fg="red",font=300).place(x=120,y=420)
            elif cond == 23:
                b4  = tk.Button(canvas2,text="already requested ",fg="red",font=300).place(x=120,y=420)






    a1 = tk.Label(canvas2,text="Search Friends:- ",font=300).place(x=10,y=280)
    a22 = tk.Label(canvas2,text="*enter their email*",fg="red").place(x=10,y=300)
    entry1 = tk.Entry(canvas2)
    spath = r"/home/pawan/Desktop/DietPlanner V2/aplha 1.1/pic/sear.png"
    sear1 = Image.open(spath)
    sear2 = sear1.resize((20,20),Image.ANTIALIAS)
    sear3 = ImageTk.PhotoImage(sear2)
    b3 = tk.Button(canvas2,image=sear3,command=lambda: makeFriends(canvas2)).place(x=205,y=320)
    entry1.place(x=10,y=323)
    # saved Diets
    rpath = r"/home/pawan/Desktop/DietPlanner V2/aplha 1.1/pic/ref111.png"
    ref1 = Image.open(rpath)
    ref2 = ref1.resize((20,20), Image.ANTIALIAS)
    ref3 = ImageTk.PhotoImage(ref2)
    x = 720
    y = 50
    L = []
    # show requests
    def getreqInfo(lk):
        L = lk
        mk = []
        for i in range(len(L)):
            que7 = "select fname,lname,email,imageID from users where email=%s"
            t6 = (L[i],)
            c.execute(que7,t6)
            r = c.fetchall()
            for i in r:
                rm = [[i[0],i[1],i[2],i[3]]]
                mk += rm
        #[['23', '23', '23', '23268'], ['pawan', 'krishnan', '1233', 'pawan231'], ['zx', 'zx', 'zx', 'zx125']]
        return mk

    def dosomething():
        que1234 = "select distinct femail from friends where status='pending' and email=%s "
        t = (fnameI,)
        c.execute(que1234,t)
        e = c.fetchall()
        lk = []
        for i in e:
            lk += i
        while len(lk) >= 4:
            lk.pop(-1)
        iq = getreqInfo(lk)
        return iq

    iq = dosomething()
    # now we can display
    # cancel
    global req333
    global req33
    pathxi = r"/home/pawan/Desktop/DietPlanner V2/aplha 1.1/pic/cancel.png"
    req111 = Image.open(pathxi)
    req222 = req111.resize((20, 20), Image.ANTIALIAS)
    req333 = ImageTk.PhotoImage(req222)
    # tick
    pathy = r"/home/pawan/Desktop/DietPlanner V2/aplha 1.1/pic/tick.webp"
    req11 = Image.open(pathy)
    req22 = req11.resize((20, 20), Image.ANTIALIAS)
    req33 = ImageTk.PhotoImage(req22)

    def cancelFriend(user,ree2):
        que12 = """
        update friends set status=%s where femail = %s and email = %s
        """
        for i in range(len(ree2)):
            t = ("accepted",ree2[i][0], user)
            c.execute(que12, t)
            mydb.commit()

    def acceptFriend(user,ree2):
        que13 = """
        update friends set status = %s where email = %s and femail = %s 
        """
        t = ('accepted',user,ree2[0][0])
        c.execute(que13,t)
        mydb.commit()
        print(c.rowcount, "record(s) affected")

    def sendReq(m,user,ree2):
        print("d",ree2)
        if m==1:
            cancelFriend(user,ree2)
        else:
            acceptFriend(user,ree2)

    def setImage(k,j,m):
        coo = []
        L = k
        user = m
        ree2 = j
        #print(user)
        #print(ree2)
        for i in range(0,len(L)):
            ax = tk.Label(canvas2,image=L[i][0]).place(x=L[i][1],y=L[i][2])
            coo.insert(-1,[L[i][1],L[i][2],L[i][3]])
        ran = random.randint(0,300)
        # make a unique image id for each button
        for i in range(0,len(coo)):
            button = tk.Button(canvas2, image=req333, command=lambda: sendReq(1,user,ree2)).place(x=coo[i][0] + 140, y=coo[i][1] + 30)
            button1 = tk.Button(canvas2, image=req33, command=lambda: sendReq(2,user,ree2)).place(x=coo[i][0] + 140, y=coo[i][1])

    def requests(x,y,L,iq):
        ree = []
        for i in range(len(iq)):
            f = iq[i][2]
            ree.insert(-1,[f])
        #print(ree)
        #print(fnameI)
        for i in iq:
            # image
            varID = i[3]
            pathx = r"/home/pawan/Desktop/DietPlanner V2/aplha 1.1/pic/userImages/"
            pathx1 = pathx + varID + ".jpg"
            req1 = Image.open(pathx1)
            req2 = req1.resize((50, 50), Image.ANTIALIAS)
            req3 = ImageTk.PhotoImage(req2)
            L.insert(-1,[req3,x,y,varID])
            # info
            rname = i[0]
            ax = tk.Label(canvas2,text=rname).place(x=x+60,y=y)
            remail = i[2]
            ax = tk.Label(canvas2,text=remail).place(x=x+60,y=y+30)
            y += 60
        img = setImage(L,ree,fnameI)


    requests(x,y,L,iq)

    def setImageAgain(k):
        rf = 0
        try:
            while rf <= 2:
                asd1 = Image.open(k[rf][0])
                asd2 = asd1.resize((50, 50), Image.ANTIALIAS)
                asd3 = ImageTk.PhotoImage(asd2)
                asd3.canvas2 = asd3
                axs = tk.Label(canvas2,image=asd3).place(x=k[rf][1]-60,y=k[rf][2]-70)
                rf += 1
        except IndexError:
            pass



    def getFriends():
        friends = []
        fgy = []
        dfg = []
        que1234 = "select distinct femail from friends where status=%s and email=%s"
        t1234 = ("accepted",emailI)
        c.execute(que1234,t1234)
        art = c.fetchall()
        for i in art:
            kr = list(i)
            friends.insert(-1,kr)

        # get friend info
        for i in range(len(friends)):
            query12345 = "select fname,lname,email,bio,imageID from users where email=%s "
            ffname = friends[i][0]
            print(ffname)
            t12345 = (ffname,)
            c.execute(query12345,t12345)
            rf = c.fetchall()
            for i in rf:
                fgy.insert(-1,list(i))
        x = 70
        y = 50
        paths = []
        for i in range(len(fgy)):
            pathA = fgy[i][4]
            pathVar = r"/home/pawan/Desktop/DietPlanner V2/aplha 1.1/pic/userImages/"
            pathF = pathVar + pathA + ".jpg"
            axr = tk.Label(canvas2,text=fgy[i][0]).place(x=x,y=y)
            axr = tk.Label(canvas2,text=fgy[i][1]).place(x=x+30,y=y)
            axr = tk.Label(canvas2,text=fgy[i][2]).place(x=x,y=y+30)
            y += 70
            paths.insert(-1,[pathF,x,y])

        setImageAgain(paths)



    getFriends()
    print("heelo")

    a1 = tk.Label(canvas2,text="Friend Requests ",font=500).place(x=720,y=10)
    # saved diets
    a14 = tk.Label(canvas2,text="Saved Diets:- ",font=300).place(x=730,y=280)




    canvas2.pack()
    root.mainloop()
