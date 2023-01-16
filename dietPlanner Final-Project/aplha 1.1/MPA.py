# variables
TC = 0
# mysql import
import random
import mysql.connector as my
mydb = my.connect(host="localhost", user="root", database="dietplanner", password="Pawan23Krishnan")
c = mydb.cursor()




def calorieAgeFemale(age):
    # activity_level = borderline noting
    if age >= 2 and age <= 3:
        cal = 1000
    elif age >= 4 and age <=8:
        cal = 1200
    elif age >= 9 and age <= 13:
        cal = 1600
    elif age >= 14 and age <= 18:
        cal = 1800
    elif age >= 19 and age <= 30:
        cal = 2000
    elif age >= 31 and age <= 50:
        cal = 1800
    elif age >=51:
        cal = 1600
    else:
        print("enter a valid age")
    return cal
    
def calorieAgeMale(age):
    # activity_level = borderline noting
    if age >= 2 and age <= 3:
        cal = 1200
    elif age >= 4 and age <=8:
        cal = 1400
    elif age >= 9 and age <= 13:
        cal = 1800
    elif age >= 14 and age <= 18:
        cal = 2000
    elif age >= 19 and age <= 30:
        cal = 2200
    elif age >= 31 and age <= 50:
        cal = 2400
    elif age >=51:
        cal = 2000
    else:
        print("enter a valid age")
    return cal


def activityLevelFemale(activity_level):
    # activity bias
    # bias -> lazy, moderate, active
    bias = 0
    if activity_level in ("lazy","Lazy","LAZY","L","l"):
        bias = 0
        return bias
    elif activity_level in("moderate","Moderate","MODERATE","M","m"):
        bias = 200
        return bias
    elif activity_level in("active","Active","ACTIVE","A","a"):
        bias = 400
        return bias

def activityLevelMale(activity_level):
    # activity bias
    # bias -> lazy, moderate, active
    if activity_level in ("lazy","Lazy","LAZY","L","l"):
        bias = 0
        return bias
    elif activity_level in("moderate","Moderate","MODERATE","M","m"):
        bias = 400
        return bias
    elif activity_level in("active","Active","ACTIVE","A","a"):
        bias = 800
        return bias


def calculateTCI(Mcal,Mbias):
    TC = Mcal + Mbias
    return TC


def calorieCounter():
    break_condition = False
    while True:
        if break_condition == True:
            break
        print("Welcome the diet planner module:- ")
        print(" ")
        print("To begin choose a calorie intake of your choice or")
        print("you can let diet planner decide the calorie intake !")
        print(" ")

        print("your choices:- ")
        
        print("Select 1 to enter your own calorie intake or")
        print("Select 2 to enter the diet planner smart calorie mode")
        print("Select 0 to leave this module")
        print(" ")
        choice = int(input("enter your choice: "))
        print(" ")
        if choice == 1:
            pass
        elif choice == 2:
            print("Some information we need:- ")
            print("please enter the information as accuratley as possible !")
            print(" ")
            while True: 
                age = int(input("Enter your age: "))
                activity_level = str(input("How active are you on a scale of lazy,moderate or active: "))
                gender = str(input("whats your gender(there are only 2 M/F): "))
                if gender in ("male","Male","MALE","M","m"):
                    Mcal = calorieAgeMale(age)
                    Mbias = activityLevelMale(activity_level)
                    Ctotal = calculateTCI(Mcal,Mbias)
                    print(" ")
                    print("Based on your information we've set the total calorie intake as: ",Ctotal)
                    print(" ")
                    print("If you're happy with this intake enter 1")
                    print("If you'd like to redo this enter 2")
                    print("If you want to exit this options enter 3")
                    print(" ")
                    c = int(input("enter your choice: "))
                    print(" ")
                    if c == 1:
                        break_condition = True
                        return Ctotal
                        break
                    elif c == 2:
                        continue
                    elif c == 3:
                        print("Goodby3....")
                        print(" ")
                        break 
                    else:
                        print("enter a valid output")
                        print(" ")
                        continue
                elif gender in ("female","FEMALE","Female","F","f"):
                    Fcal = calorieAgeFemale(age)
                    Fbias = activityLevelFemale(activity_level)
                    Ctotal = calculateTCI(Fcal,Fbias)
                    print(" ")
                    print("Based on your information we've set the total calorie intake as: ",Ctotal)
                    print(" ")
                    print("If you're happy with this intake enter 1")
                    print("If you'd like to redo this enter 2")
                    print("If you want to exit this options enter 3")
                    c = int(input("enter your choice: "))
                    if c == 1:
                        break_condition = True
                        return Ctotal
                        print(" ")
                        break
                    elif c == 2:
                        print(" ")
                        continue
                    elif c == 3:
                        print("Goodby3....")
                        print(" ")
                        break 
                    else:
                        print("enter a valid output")
                        continue
                else:
                    print("<--! enter a valid gender !--> ")
                    print(" ")
                    continue               
        elif choice == 0:
            break
        else:
            print("to procceed you must select an option !")
            continue
        

    


# meal choice

def GUICHOICE():    
    #breakfast
    b = []
    c.execute("select distinct btype from breakfast")
    g = c.fetchall()
    for i in g:
        f = list(i)
        if f not in b:
            b += f
    return b

def LUICHOICE():
    # lunch
    l = []
    c.execute("select distinct ltype from lunch")
    g = c.fetchall()
    for i in g:
        f = list(i)
        if f not in l:
            l += f
    return l


"""
def BreakfastChoiceGUI():
     gb = []
     t = (b_choice,)
     c.execute("select id,bname,bcal,brate from breakfast where bpref = 'VEG' and btype = (%s) ", t)
     g = c.fetchall()
     for i in g:
        gb += [list(i)]
"""

def BreakfastChoice():
    print(" ")
    print("Select a preffered cusine, we offer different cusine styles for different meals:- ")
    print(" ")
    
    #breakfast
    b = []
    c.execute("select distinct btype from breakfast")
    g = c.fetchall()
    print("We offer the following cusines for breakfast:- ")
    for i in g:
        f = list(i)
        if f not in b:
            b += f
    for j in b:
        print(j)
    while True: 
        choice = str(input("enter prefered cusine: "))
        t = (choice,)
        c.execute("Select count(*) from breakfast where btype = (%s)",(t))
        g = c.fetchone()
        mk = 0
        for i in g:
            mk += i
        print(choice, " is selected !")
        print(mk,"dishes available in ",choice, " cusine " ," !")
        if choice in b:
            return choice
            c.close()
            break
        else:
            print("selected option is not available try again")
            continue



def LunchChoice():
    #Lunch
    l = []
    c.execute("select distinct ltype from lunch")
    g = c.fetchall()
    print("We offer the following cusines for lunch:- ")
    for i in g:
        f = list(i)
        if f not in l:
            l += f
    for j in l:
        print(j)
    while True: 
        choice = str(input("enter prefered cusine: "))
        if choice in l:
            print(choice, " is selected !")
            return choice
            c.close()
            break
        else:
            print("selected option is not available try again")
            continue

# meal get

def getBMeal(mealc):
    # get breafast cal
    gb = []
    #k = BreakfastChoice() # disable this aight
    t = (mealc,)
    c.execute("select id,bname,bcal,brate from breakfast where bpref = 'VEG' and btype = (%s) ", t)
    g = c.fetchall()
    for i in g:
        gb += [list(i)]
    return gb


# final breakfast

def getFinalB(k1,totalC):
    L = k1
    sumi = totalC
    total = int((15*sumi)/100)
    ct = 0
    length = len(L)

    combine = []
    while ct <= total:
        k = random.randint(0,(length-1))
        if L[k] not in combine:
            combine.insert(-1,L[k])
            ct += L[k][2]


    if ct > total:
        combine.pop(-1)
        ct -= combine[-1][2]

    m = total - ct

    if ct < total:
        for i in range(len(L)):
            if L[i][2] <= m and L[i] not in combine:
                combine.insert(-1,L[i])
                ct += L[i][2]

    stuff = [combine,ct,m]
    return stuff

def getFinalL(lb,totalC):
    L = lb
    sumi = totalC
    print(totalC)
    total = int((40 * sumi)/100) - 80
    print(total)
    ct = 0
    length = len(L)
    qwert = length
    combine = []
    while ct <= total:
        k = random.randint(0,qwert)
        try:
            if L[k] not in combine:
                combine.insert(-1, L[k])
                ct += L[k][2]
                print(ct)
        except IndexError:
            continue

    if ct > total:
        combine.pop(-1)
        ct -= combine[-1][2]

    m = total - ct

    if ct < total:
        for i in range(len(L)):
            if L[i][2] <= m and L[i] not in combine:
                combine.insert(-1, L[i])
                ct += L[i][2]
                print("i",ct)

    stuff = [combine, ct, m]
    print(stuff)
    return stuff

def getFinalD(db,totalC):
    L = db
    sumi = totalC
    total = int((35 * sumi) / 100) - 100
    ct = 0
    length = len(L)
    qwert = length
    combine = []
    print(totalC)
    print(total)
    while ct <= total:
        k = random.randint(0, qwert)
        try:
            if L[k] not in combine:
                combine.insert(-1, L[k])
                ct += int(L[k][2])
                print(ct)
        except IndexError:
            continue

    if ct > total:
        combine.pop(-1)
        ct -= int(combine[-1][2])

    m = total - ct

    if ct < total:
        for i in range(len(L)):
            if int(L[i][2]) <= m and L[i] not in combine:
                combine.insert(-1, L[i])
                ct += int(L[i][2])

    stuff = [combine, ct, m]
    print("Stuff is ",stuff)
    return stuff



"""
    print("MEAL SET")
    ct = 1
    for i in range(len(combine)):
        print(ct,":- ")
        ct += 1
        print("food name: ",combine[i][1])
        print("calorie(SFP): ",combine[i][2])
        print("rating: ",combine[i][3])
        print(" ")
    print("the total calories for this meal set is: ",c)
    print("the amount over or under is +/-: ",total-c)
    return combine
"""
 


# final stuff
def MealChoice(totalC):
    print("MEAL CHOICE GENERATION:- ")
    print(" ")
    print("To generate a preffered meal plan we need some more information")
    print("Would you like a vegetarian or a non-vegetarian meal plan ")
    print(" ")
    mealc = str(input("enter your meal choice(V/N): "))
    return mealc
    print(" ")
    while True:
        if mealc in ("VEG","veg","v"):
            print("* The following meal plan generated is based on provided information *")
            print("* The meal plan provided may not be suitable for all individuals *")
            print("* All meal proportions follow the SFP schem (to know more about SFP schema go to about) *")
            return mealc
            break
        elif mealc in ("NVEG","nveg","n"):
            print("* The following meal plan generated is based on provided information *")
            print("* The meal plan provided may not be suitable for all individuals *")
            print("* All meal proportions follow the SFP schem (to know more about SFP schema go to about) *")
            return mealc
            break
        else:
            print("Enter a valid choice")
            print(" ")
            continue
            

def returnSelectedBreakfast(sK):
    return sK

def returnB(b):
    return b

def returnL(l):
    return l

def Finish():
    totalC = calorieCounter()
    mealc = MealChoice(totalC)
    b = getBMeal(mealc)
    k1 = returnB(b)
    print(" ")
    while True:
        print("MEAL CHOICE:- ")
        sK = getFinalB(k1,totalC)
        print(" ")
        print("If you are happy with this set press 1")
        print("If you would like to get a different set press 2")
        choice = int(input("enter choice: "))
        if choice == 1:
            print("Meal set selected !")
            end = returnSelectedBreakfast(sK)
            break
        elif choice  == 2:
            continue


    return end

    
#BFINAL = Finish()
#print("final godamm variable: ",BFINAL)




