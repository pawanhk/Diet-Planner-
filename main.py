# imports
from modules import * 


print("DIET PLANNER V2  -- command line version")
print("Welcome to DIET planner, to start agree the following terms and conditions: ")


while True:
# terms and conditions
    print("TERMS AND CONDITION:- ")
    print(" * diet planner is not responsible for your death * ")
    print(" * diet planner is not responsible for your health * ")
    print(" * you should not listen to diet planner * ")
    agree = str(input("do you agree to the following(Y/N): "))
    atc = False

    if agree in ("Y","y"):
        atc = True
        print("success !")
        print(" ")
        break
    elif agree in("N","n"):
        atc = False
        print("<--! you must accept the terms and conditions to continur with the program !--> ")
    else:
        print("<--! please provide a vaild input !--> ")


# Registration  / Login

if atc == True:
    while True:
        checkr = False
        checkl = False
        print("LOGIN AND REGISTRATION:- ")
        print("To proceed you must have an account and if you dont you can create one here:- ")
        lt = str(input("if need an account type R or if you have an account type L(R/L):  "))
        print(" ")

        if lt in ("r","R"):
            print("REGISTRATION:- ")
            k =  registration()
            if k == True:
                checkr = True
                break
        elif lt in ("l","L"):
            print("LOGIN:- ")
            k = login()
            if k == True:
                checkl = True
                break


            

        if checkr == True:
            print("<--! Welcome to Diet Planner !--> ")
            break
        elif checkl == True:
            print("<--! Welcome back to  Diet Planner !--> ")
            break
        else:
            continue
        

# main hub area
            
if atc == True and (checkl or checkr) == True:
    print("WElCOME TO THE MAIN HUB, you'll be provided a series of options to choose from")
    hub()
    
            



























            





    
