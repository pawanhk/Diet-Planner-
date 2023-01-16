import tkinter as tk
from MPA import *
from tkinter import *
from ttkthemes import themed_tk as kt
from tkinter import filedialog
# sql connect
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
    mydb = my.connect(host="localhost", user="root", database="dietplanner", password="Pawan23Krishnan")
    c = mydb.cursor()
    x1 = str(entry1.get())
    x2 = str(entry2.get())
    """
    c.execute("select fname,password from users ")
    g = c.fetchall()
    for i in g:
        if i[0] == x1 and i[1] == x2:
            mainHUB(x1)
        else:
            e3 = tk.Label(root, text="username or password is incorrect !",fg="red").place(x=120,y=220)
    """
    mainHUB("pawan")




def mainHUB(username,*args):
    for ar in args:
        ar.destroy()
    root.withdraw()

    def foodUpload():
        mydb = my.connect(host="localhost", user="root", database="dietplanner", password="Pawan23Krishnan")
        c = mydb.cursor()
        top1 = tk.Tk()
        top1.title("upload Food")
        top1.resizable(False,False)

        def getData():
            x1 = int(t1.get())
            x2 = str(t2.get())
            x3 = str(t3.get())
            x4 = str(t4.get()).upper()
            x5 = int(t5.get())
            x6 = int(t6.get())
            x7 = str(t7.get())
            x8 = str(t8.get()).upper()
            L = [x1, x2, x3, x4, x5, x6, x7, x8]
            if (ia.get()) == 1:
                k = "breakfast"
            elif (ia.get()) == 2:
                k = "lunch"
            elif (ia.get()) == 3:
                k = "dinner"
            else:
                k = "non"
            t = [L, k]
            return t

        def uploadData():
            L = getData()
            table = L[1]
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
            t = (id, name, cusine, type, calorie, rating, att, res)
            c.execute(query, t)
            mydb.commit()
            e3 = tk.Label(canvas11,text="Done.....",fg="green").place(x=380,y=328)



        canvas11 = tk.Canvas(top1,width=580,height=360)
        a0 = tk.Label(canvas11, text="Food Upload:- ", font=20).place(x=10, y=10)
        e3 = tk.Label(canvas11,text="Standby...",fg="red").place(x=380,y=328)

        a1 = tk.Label(canvas11, text="enter id of food: ").place(x=10, y=40)
        a2 = tk.Label(canvas11, text="enter name of food: ").place(x=10, y=80)
        a3 = tk.Label(canvas11, text="enter cusine: ").place(x=10, y=100)
        a4 = tk.Label(canvas11, text="enter type(V/N/P/O/Ve/Po/F): ").place(x=10, y=140)
        a5 = tk.Label(canvas11, text="enter total calories: ").place(x=10, y=160)
        a6 = tk.Label(canvas11, text="enter your rating: ").place(x=10, y=180)
        a7 = tk.Label(canvas11, text="enter food attribute(LC,HC,HP,MC,MP,LP): ").place(x=10, y=220)
        a8 = tk.Label(canvas11, text="enter allergic specifics(L/G/E/F/S/P/NON): ").place(x=10, y=260)

        ia = StringVar(canvas11)
        r1 = tk.Radiobutton(canvas11, text="Breakfast", value=1, variable=ia).place(x=10, y=300)
        r2 = tk.Radiobutton(canvas11, text="Lunch", value=2, variable=ia).place(x=120, y=300)
        r3 = tk.Radiobutton(canvas11, text="Dinner", value=3, variable=ia).place(x=220, y=300)

        t1 = tk.Entry(canvas11)
        t1.place(x=380, y=40)

        t2 = tk.Entry(canvas11)
        t2.place(x=380, y=80)
        t3 = tk.Entry(canvas11)
        t3.place(x=380, y=100)
        t4 = tk.Entry(canvas11)
        t4.place(x=380, y=140)
        t5 = tk.Entry(canvas11)
        t5.place(x=380, y=160)
        t6 = tk.Entry(canvas11)
        t6.place(x=380, y=180)
        t7 = tk.Entry(canvas11)
        t7.place(x=380, y=220)
        t8 = tk.Entry(canvas11)
        t8.place(x=380, y=260)

        b1 = tk.Button(canvas11, text="Submit", command=uploadData).place(x=380, y=300)
        canvas11.pack()


    def planDiet():
        def getAllSelection():
            gender = getGender()
            pref = getPref()
            info = getInfo()
            allergies = getAllergies()
            conditions = getConditions()
            cusine = getCusine()
            superList = [gender, pref, info, allergies, conditions, cusine]
            return superList


        header = tk.Label(canvas3, text="Diet Planner:- ", font="35").place(x=10, y=20)
        # left side
        # manual entry
        h1 = tk.Label(canvas3, text="Welcome to Diet Planner:- ", font=10).place(x=10, y=70)
        h2 = tk.Label(canvas3,text="->for accurate results enter ").place(x=10,y=120)
        h2 = tk.Label(canvas3, text="->the following accurately as possible").place(x=10, y=150)


        # smart calori mode
        def getiInfo():
            t = []
            x1 = int(entryAge.get())
            if (ia.get()) == 100:
                k = "l"
            elif (ia.get()) == 101:
                k = "m"
            elif (ia.get()) == 102:
                k = "a"
            else:
                k = "m"
            t += [x1, k]
            return t

        def getInfo():
            k = getiInfo()
            return k

        h2 = tk.Label(canvas3, text="Smart Calorie mode:- ", font=15).place(x=10, y=200)
        a1 = tk.Label(canvas3, text="Enter Age(int): ", font=10).place(x=10, y=240)
        entryAge = tk.Entry(canvas3)
        entryAge.place(x=10, y=280)
        ia = IntVar()
        a2 = tk.Label(canvas3, text="Enter Activity level(str): ", font=10).place(x=10, y=320)
        a3 = tk.Radiobutton(canvas3, text="lazy", value=100, variable=ia).place(x=10, y=360)
        a3 = tk.Radiobutton(canvas3, text="moderate", value=101, variable=ia).place(x=10, y=400)
        a3 = tk.Radiobutton(canvas3, text="active", value=102, variable=ia).place(x=10, y=440)

        # right side
        # radio button sections
        def getGender():
            if (ig.get()) == 1:
                k = "Male"
            elif (ig.get()) == 2:
                k = "Female"
            elif (ig.get()) == 0:
                k = "Male"
            return k

        ig = IntVar()
        a3 = tk.Label(canvas3, text="Select Gender:- ", font=15).place(x=400, y=20)
        a4 = tk.Radiobutton(canvas3, text="Male", value=1, variable=ig).place(x=400, y=60)
        a5 = tk.Radiobutton(canvas3, text="Female", value=2, variable=ig).place(x=480, y=60)
        a15 = tk.Radiobutton(canvas3, text="Not say", value=0, variable=ig).place(x=580, y=60)

        # meal choice
        def getPref():
            if (ik.get()) == 3:
                k = "Veg"
            elif (ik.get()) == 4:
                k = "Non-Veg"
            elif (ik.get()) == 5:
                k = "Vegan"
            elif (ik.get()) == 6:
                k = "Omni"
            elif (ik.get()) == 7:
                k = "Pescatarian"
            elif (ik.get()) == 8:
                k = "Pollotarian"
            elif (ik.get()) == 9:
                k = "Flexitarian"
            else:
                k = "blank"
            return k

        ik = IntVar()
        a6 = tk.Label(canvas3, text="Select meal Preference:- ", font=15).place(x=400, y=100)
        a7 = tk.Radiobutton(canvas3, text="Veg", value=3, variable=ik).place(x=400, y=140)
        a8 = tk.Radiobutton(canvas3, text="Non-Veg", value=4, variable=ik).place(x=475, y=140)
        a14 = tk.Radiobutton(canvas3, text="Flexitarian", value=9, variable=ik).place(x=585, y=140)

        a9 = tk.Radiobutton(canvas3, text="Vegan", value=5, variable=ik).place(x=400, y=180)
        a10 = tk.Radiobutton(canvas3, text="Omni", value=6, variable=ik).place(x=490, y=180)
        a11 = tk.Radiobutton(canvas3, text="Pescatarian", value=7, variable=ik).place(x=576, y=180)

        a12 = tk.Radiobutton(canvas3, text="pollotarian", value=8, variable=ik).place(x=400, y=220)

        # allergies and stugg
        def getAllergies():
            if (im.get()) == "Lactos-Intolarent":
                k = "LI"
            elif (im.get()) == "Gluten-Free":
                k = "GF"
            elif (im.get()) == "Peanut-Free":
                k = "PF"
            elif (im.get()) == "Eggs-Free":
                k = "EF"
            elif (im.get()) == "Fish-Free":
                k = "FF"
            elif (im.get()) == "Soya-Free":
                k = "SF"
            else:
                k = "None"
            return k

        a16 = tk.Label(canvas3, text="Allergies/Restriction (if any)", font=15).place(x=400, y=260)
        im = StringVar(root)
        choices = {"None", "Lactos-Intolarent", "Gluten-Free", "Peanut-Free", "Eggs-Free", "Fish-Free", "Soya-Free"}
        im.set("None")

        dropDown = tk.OptionMenu(canvas3, im, *choices).place(x=400, y=300)

        # prexisitng conditions
        def getConditions():
            if (ij.get()) == "Diabetes":
                k = "D"
            elif (ij.get()) == "Heart-Disease":
                k = "HD"
            elif (ij.get()) == "High-Blood-Pressure":
                k = "HBP"
            elif (ij.get()) == "Gallstone":
                k = "G"
            elif (ij.get()) == "Cancer":
                k = "C"
            elif (ij.get()) == "Eating-Disorders":
                k = "ED"
            else:
                k = "None"
            return k

        a20 = tk.Label(canvas3, text=" Prexisting Conditions (if any)", font=15).place(x=400, y=360)
        ij = StringVar(root)
        choices2 = {"None", "Heart-Disease", "High-Blood-Pressure", "Diabetes", "Gallstone", "Cancer",
                    "Eating-Disorders"}
        ij.set("None")
        dropDown2 = tk.OptionMenu(canvas3, ij, *choices2).place(x=400, y=400)

        # cusine selection
        def getCusine():
            if (ip.get()) == "global":
                k = "global"
            elif (ip.get()) == "italian":
                k = "italian"
            elif (ip.get()) == "indian":
                k = "indian"
            elif (ip.get()) == "columbian":
                k = "columbian"
            else:
                k = "global"
            return k

        a27 = tk.Label(canvas3, text="Cusine Selection:- ", font=15).place(x=820, y=20)
        choice_list = GUICHOICE()
        ip = StringVar(root)
        ip.set("global")
        dropDown3 = tk.OptionMenu(canvas3, ip, *choice_list).place(x=820, y=60)

        ######

        def openDietPlan(shrek, shrek2, shrek3, abh):
            L = shrek  # b
            L2 = shrek2  # l
            L3 = shrek3  # d
            P = abh
            dp = tk.Toplevel()
            dp.title("your personalized diet plan")
            dp.resizable(False, False)
            canvas4 = tk.Canvas(dp, width=1000, height=30)
            # display output
            # L = [[[4, 'idli', 40, 2], [10, 'poori', 101, 4], [5, 'poha', 241, 4]], 351, 150]
            # L = [[[10, 'poori', 101, 4, 'high-carb'], [4, 'idli', 40, 2, 'low-carb']
            # P = ['Male', 'Vegan', ['18', 'm'], 'EF', 'G', 'indian']
            a32 = Label(canvas4, text="Your diet-plan ", font=40).place(x=10, y=0)
            canvas4.pack()
            canvas5 = tk.Canvas(dp, width=1000, height=500, bg="gray")
            a33 = Label(canvas5, text="Diet Information:- ", fg="green").place(x=10, y=20)
            # MEAL TYPE
            meal_type = "-> " + P[1] + " meal"
            a35 = Label(canvas5, text=meal_type).place(x=10, y=50)
            # Cusine TYPE
            meal_cus = "-> " + P[5] + " cusine"
            a35 = Label(canvas5, text=meal_cus).place(x=10, y=80)
            # TOTAL CALORIE
            # meal_cal = "-> " + "total calorie: " + str(L[1])
            meal_cal = "tbd"
            a34 = Label(canvas5, text=meal_cal).place(x=10, y=110)
            # RESTRICTION
            ctype = "NONE"
            if str(P[3]) == "LI":
                ctype = "Lactose free"
            elif str(P[3]) == "GF":
                ctype = "Gluten free"
            elif str(P[3]) == "PF":
                ctype = "Peanut free"
            elif str(P[3]) == "EF":
                ctype = "Egg free"
            elif str(P[3]) == "FF":
                ctype = "Fish free"
            elif str(P[3]) == "SF":
                ctype = "Soya free"
            else:
                ctype = "NONE"

            if ctype != "NONE":
                meal_res = "-> " + "this meal is " + ctype
                a34 = Label(canvas5, text=meal_res).place(x=10, y=140)
            else:
                a34 = Label(canvas5, text="no restrictions").place(x=10, y=140)

            if P[4] != "None":
                a35 = Label(canvas5, text="Prexisting condition warning:  ", fg="red").place(x=10, y=180)
                cond = P[4]
                #######
                condition = P[4]
                if condition == "D":
                    # recommended less calorie intake
                    # more lean protien
                    # high fiber
                    a36 = Label(canvas5, text="*recommended lower calorie intake", fg="green").place(x=10, y=220)
                    a36 = Label(canvas5, text="*recommended higher protiens intake", fg="green").place(x=10, y=260)
                    a36 = Label(canvas5, text="*recommender higher fiber intake", fg="green").place(x=10, y=300)
                else:
                    """
                    Vegetables or salad: Half a plate
                    High-quality protein: Quarter of a plate — this includes meat, poultry, fish, eggs, dairy, tofu, beans and pulses
                    Complex carbs: Quarter of a plate — such as whole grains and starchy vegetables
                    High-fat foods: Half a tablespoon (7 grams) — including cheese, oils and butter"
                    """
                    a35 = Label(canvas5, text="Portion control: ", fg="red").place(x=10, y=180)
                    a36 = Label(canvas5, text="*high-protien: 1/4th of plate", fg="green").place(x=10, y=220)
                    a36 = Label(canvas5, text="*high-carb: 1/4th of plate", fg="green").place(x=10, y=260)
                    a36 = Label(canvas5, text="*vegetables/salads: 1/2 of plate", fg="green").place(x=10, y=300)
            # order online ()
            def callback(url):
                webbrowser.open_new(url)
            ax = Label(canvas5,text="Order Online(coming soon)").place(x=10,y=340)
            z1 = Label(canvas5,text="Zomato: ").place(x=10,y=370)
            link1 = Button(canvas5, text="order", fg="blue", cursor="hand2")
            link1.place(x=120,y=370)
            link1.bind("<Button-1>", lambda e: callback("https://www.zomato.com/dubai"))
            z1 = Label(canvas5, text="Deliveroo: ").place(x=10, y=410)
            link1 = Button(canvas5, text="order", fg="blue", cursor="hand2")
            link1.place(x=120, y=410)
            link1.bind("<Button-1>", lambda e: callback("https://deliveroo.ae/"))
            z1 = Label(canvas5, text="Uber-Eats: ").place(x=10, y=450)
            link1 = Button(canvas5, text="order", fg="blue", cursor="hand2")
            link1.place(x=120, y=450)
            link1.bind("<Button-1>", lambda e: callback("https://www.ubereats.com/"))

            # diet display
            # L = [[[4, 'idli', 40, 2], [10, 'poori', 101, 4], [5, 'poha', 241, 4]], 351, 150]
            a37 = Label(canvas5, text="Meal Choices:- ", fg="green").place(x=370, y=20)
            count = 0
            x1 = 370
            y1 = 100
            n1 = "Name"
            n2 = "Calories"
            n3 = "Rating"
            n4 = "Type"
            an1 = Label(canvas5, text=n1, fg="black").place(x=500, y=60)
            an2 = Label(canvas5, text=n2, fg="black").place(x=600, y=60)
            an3 = Label(canvas5, text=n3, fg="black").place(x=700, y=60)
            an4 = Label(canvas5, text=n4, fg="black").place(x=800, y=60)

            # Breakfast choices

            while count <= (len(L) - 1):
                try:
                    t = L[0][count]
                except IndexError:
                    break
                m = []
                m.append(t[1])
                m.append(t[2])
                m.append(t[3])
                m.append(t[4])
                txt = "breakfast " + str((count + 1)) + ": "
                a38 = Label(canvas5, text=txt, fg="black").place(x=x1, y=y1)

                a38 = Label(canvas5, text=m[0], fg="black").place(x=(x1 + 130), y=y1)
                a38 = Label(canvas5, text=m[1], fg="red").place(x=(x1 + 250), y=y1)
                a38 = Label(canvas5, text=m[2], fg="black").place(x=(x1 + 350), y=y1)
                a38 = Label(canvas5, text=m[3], fg="black").place(x=(x1 + 430), y=y1)
                y1 += 40
                count += 1

            # lunch choices
            count2 = 0
            x2 = 370
            y2 = 230
            while count2 < (len(L2)):
                try:
                    t = L2[0][count2]
                except IndexError:
                    break
                r = []
                r.append(t[1])
                r.append(t[2])
                r.append(t[3])
                r.append(t[4])

                txt = "lunch " + str((count2 + 1)) + ": "
                a38 = Label(canvas5, text=txt, fg="black").place(x=x2, y=y2)
                a38 = Label(canvas5, text=r[0], fg="black").place(x=(x2 + 130), y=y2)
                a38 = Label(canvas5, text=r[1], fg="red").place(x=(x2 + 250), y=y2)
                a38 = Label(canvas5, text=r[2], fg="black").place(x=(x2 + 350), y=y2)
                a38 = Label(canvas5, text=r[3], fg="black").place(x=(x2 + 430), y=y2)
                y2 += 40
                count2 += 1

            # dinner choices
            count3 = 0
            x2 = 370
            y2 = 380
            while count3 < (len(L3)):
                try:
                    t = L3[0][count3]
                except IndexError:
                    break
                z = []
                z.append(t[1])
                z.append(t[2])
                z.append(t[3])
                z.append(t[4])

                txt = "dinner " + str((count3 + 1)) + ": "
                a38 = Label(canvas5, text=txt, fg="black").place(x=x2, y=y2)
                a38 = Label(canvas5, text=z[0], fg="black").place(x=(x2 + 130), y=y2)
                a38 = Label(canvas5, text=z[1], fg="red").place(x=(x2 + 250), y=y2)
                a38 = Label(canvas5, text=z[2], fg="black").place(x=(x2 + 350), y=y2)
                a38 = Label(canvas5, text=z[3], fg="black").place(x=(x2 + 430), y=y2)
                y2 += 40
                count3 += 1

            canvas5.pack()

        def printStuff():
            # get info
            k = getAllSelection()
            activity_level = k[2][1]
            age = int(k[2][0])
            if k[0] == "Male":
                calm = calorieAgeMale(age)
                biasm = activityLevelMale(activity_level)
                totalm = calculateTCI(calm, biasm)
            else:
                calm = calorieAgeFemale(age)
                biasm = activityLevelFemale(activity_level)
                totalm = calculateTCI(calm, biasm)

            mealc = k[1]
            # breakfast
            b_choice = k[5]
            gb = []
            t = (b_choice,)
            mydb = my.connect(host="localhost", user="root", database="dietplanner", password="Pawan23Krishnan")
            c = mydb.cursor()
            c.execute("select id,bname,bcal,brate,batt from breakfast where bpref = 'VEG' and btype = (%s) ", t)
            g = c.fetchall()
            for i in g:
                gb += [list(i)]
            # contains the list of stuff we need

            shrek = getFinalB(gb, totalm)
            confirm = False
            c.close()

            mydb = my.connect(host="localhost", user="root", database="dietplanner", password="Pawan23Krishnan")
            d = mydb.cursor()

            # lunch
            l_choice = k[5]
            lb = []
            t2 = (l_choice,)
            d.execute("select id,lname,lcal,lrate,latt from lunch where lpref='VEG' and ltype = (%s)", t2)
            g2 = d.fetchall()
            for i in g2:
                lb += [list(i)]
            shrek2 = getFinalL(lb, totalm)

            confirm = False

            # dinner
            d_choice = k[5]
            db = []
            t3 = (d_choice,)
            d.execute("select id,dname,dcal,drate,datt from dinner where dpref='VEG' and dtype = (%s)", t3)
            g2 = d.fetchall()
            for i in g2:
                db += [list(i)]
            shrek3 = getFinalD(db, totalm)
            confirm = False

            if len(shrek) != 0 and len(shrek2) != 0 and len(shrek3) != 0:
                confirm = True

            if confirm == True:
                jio = [shrek, shrek2, shrek3, confirm, k]
                return jio

        # status for updating
        a29 = tk.Label(canvas3, text="status: ").place(x=820, y=450)

        def statusCheck(condition_check=0):
            if condition_check == 0:
                a30 = tk.Label(canvas3, text="standby", fg="green").place(x=900, y=450)
            elif condition_check == 1:
                a30 = tk.Label(canvas3, text="request completed", fg="green").place(x=900, y=450)
            canvas3.delete(a30)

        statusCheck()

        def execute():
            try:
                k = printStuff()
            except ValueError:
                a31 = tk.Label(canvas3, text="incomplete", fg="green").place(x=900, y=450)
            except UnboundLocalError:
                a31 = tk.Label(canvas3, text="unaccaptable values", fg="green").place(x=900, y=450)

            if k[3] == True:
                b7 = tk.Button(canvas3, text="view diet plan", command=lambda: openDietPlan(k[0], k[1], k[2], k[4]),
                               fg="green").place(x=820, y=350)
                statusCheck(1)

        def redo():
            execute()

        b3 = tk.Button(canvas3, text="submit", command=execute).place(x=820, y=400)
        b4 = tk.Button(canvas3, text="save").place(x=920, y=400)
        b5 = tk.Button(canvas3, text="privacy", command=printStuff).place(x=1000, y=400)
        b6 = tk.Button(canvas3, text="redo", command=redo).place(x=1100, y=400)

    def exitProgram():
        def closeProgram():
            exit()

        def stayProgram():
            ex.withdraw()

        ex = tk.Toplevel()
        ex.title("close program")
        ex.resizable(False, False)
        canvas6 = tk.Canvas(ex, width="300", height="100")
        et = tk.Label(ex, text="Are you sure you want to exit ? ").place(x=30, y=10)
        e1 = tk.Button(ex, text="yes", font=15, command=closeProgram, fg="red").place(x=50, y=50)
        e2 = tk.Button(ex, text="no", font=15, command=stayProgram, fg="green").place(x=180, y=50)
        canvas6.pack()


    top = tk.Toplevel()
    top.title("Diet Planner")
    top.resizable(False, False)
    canvas2 = tk.Canvas(top, width=1200, height=80)
    # MAIN HUB AREA
    header3 = tk.Label(top, text="Diet Planner[HUB]", font=60).place(x=525, y=0)
    # menu area
    m1 = tk.Button(top, text="Plan Diet", font=15, command=planDiet).place(x=10, y=30)
    m3 = tk.Button(top, text="Upload", font=15, command=foodUpload).place(x=130, y=30)
    m3 = tk.Button(top, text="exit", font=15, command=exitProgram).place(x=230, y=30)
    name = "welcome back " + username
    welcomeName = tk.Label(top,text=name, font=30).place(x=950,y=35)
    tag = tk.Label(canvas2,text="Made By Pawan, Abishek ",fg="blue").place(x=950,y=10)
    # main area
    canvas2.pack()
    canvas3 = tk.Canvas(top, width=1200, height=480, bg="gray")
    canvas3.pack()


def openFileManager(canvas):
    filename = filedialog.askopenfilename(initialdir="/home/pawan/Pictures/",
                                          title="Select a File",
                                          filetypes=(("Image files",
                                                      "*.png*"),
                                                     ("all files",

                                              "*.*")))

    asd1 = tk.Label(canvas,text="File Path:- ").place(x=10,y=310)
    asd = tk.Label(canvas,text=filename).place(x=10,y=340)
    k = str(filename)
    return k


def uploadStuff(a,b,c,d,e):
    x1 = str(a.get())
    x2 = str(b.get())
    x3 = str(c.get())
    x4 = str(d.get())
    x5 = str(e.get())
    tl = [x1,x2,x3,x4,x5]

    return tl


def register():
    # register
    reg = tk.Tk()
    reg.title("diet Planner V2")
    reg.resizable(False, False)
    canvas10 = tk.Canvas(reg, width=500, height=360)
    header = tk.Label(reg, text="Welcome to Diet Planner V2", font=40).place(x=10, y=10)

    z1 = tk.Label(reg, text="First Name: ").place(x=10, y=40)
    z2 = tk.Label(reg, text="Last Name: ").place(x=10, y=80)
    z3 = tk.Label(reg, text="Email: ").place(x=10, y=120)
    z4 = tk.Label(reg, text="Password: ").place(x=10, y=160)
    z5 = tk.Label(reg, text="Confirm Password: ").place(x=10, y=200)
    z5 = tk.Label(reg, text="Choose Profile Photo: ").place(x=10, y=240)
    b23 = tk.Button(reg, text="choose file",command=lambda: uniteTheFallen(reg,canvas10,1)).place(x=250, y=240)


    x1 = tk.Entry(reg)
    x1.place(x=250, y=40)

    x2 = tk.Entry(reg)
    x2.place(x=250, y=80)

    x3 = tk.Entry(reg)
    x3.place(x=250, y=120)

    x4 = tk.Entry(reg)
    x4.place(x=250, y=160)

    x5 = tk.Entry(reg)
    x5.place(x=250, y=200)

    b24 = tk.Button(reg, text="EULA", fg="red").place(x=250, y=300)
    b25 = tk.Button(reg, text="Login",command=reg.destroy).place(x=325, y=300)
    b26 = tk.Button(reg, text="Submit", fg="green",command=lambda: uniteTheFallen(reg,canvas10,2,x1,x2,x3,x4,x5)).place(x=400, y=300)



    canvas10.pack()

def uniteTheFallen(reg,canvas,a,x1=0,x2=0,x3=0,x4=0,x5=0):
    mydb = my.connect(host="localhost", user="root", database="dietplanner", password="Pawan23Krishnan")
    c = mydb.cursor()
    check1 = False
    check2 = False
    e1 = tk.Label(canvas)
    e1.place(x=260, y=340)
    if a == 1:
        m = openFileManager(canvas)
        query = """
        INSERT INTO location (id,loco) VALUES(%s,%s)
        """
        t = (1,m)
        c.execute(query,t)
        mydb.commit()
    elif a == 2:
        ko = uploadStuff(x1,x2,x3,x4,x5)
        if ko[3] != ko[4]:
            e1.config(text="password does not match !", fg="red")
            check1 = False
        else:
            check1 = True

        if check1 == True:
            c.execute("select * from users")
            g = c.fetchall()
            for i in g:
                if i[3] == ko[2]:
                    check2 = False
                    e1.config(text="email is already being  used !", fg="red")
                    break
                else:
                    check2 = True


        if check1 == True and check2 == True and (ko[0],ko[1],ko[2],ko[3],ko[4]) != "":
            fname = ko[0]
            lname  = ko[1]
            email = ko[2]
            password = ko[4]
            bio = "Kush is GAY"
            genereateIMAGID = random.randint(1, 500)
            imageID = fname + str(genereateIMAGID)
            c.execute("select loco from location where id=1")
            g = c.fetchall()
            for i in g:
                file = i
            t = file[0]
            with open(t, "rb") as f:
                data = f.read()
            query = """
             insert into users (fname,lname,email,photo,bio,password,imageID) values(%s,%s,%s,%s,%s,%s,%s)
             """
            t = (fname, lname, email, data, bio, password, imageID)
            c.execute(query, t)
            mydb.commit()
            c.execute("select * from users")
            r = c.fetchall()
            # add image
            for i in r:
                if i[7] == imageID:
                    decypher = i[4]

            with open("pic/userImages/" + imageID + ".jpg", "wb") as f:
                f.write(decypher)
            c.execute("delete from location where id=1")
            mydb.commit()

            c.execute("select fname,lname,email,password from users")
            k = c.fetchall()
            for i in k:
                if i[0] == ko[0] and i[1] == ko[1] and i[2] == ko[2] and i[3] == ko[3]:
                    print("sucess")
                    mainHUB(ko[0],reg)




def exit1():
    exit()



button1 = tk.Button(root, text="Submit", command=Login).place(x=207,y=160)  # change to checkCorrect

button2 = tk.Button(root, text="Sign-UP", command=register).place(x=300,y=160)

button3 = tk.Button(root, text="Exit", command=exit1).place(x=400,y=160)


root.mainloop()
