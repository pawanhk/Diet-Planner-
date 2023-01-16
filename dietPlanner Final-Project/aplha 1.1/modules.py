import mysql.connector as my
mydb = my.connect(host="localhost", user="pawan", database="dietplanner", password="Pawan23.Krishnan")
c = mydb.cursor()



def registration():
    while True:
        confirm = False
        username  = str(input("enter your username: "))
        password = str(input("enter a secure password: "))
        cpassword = str(input("confirm password: "))
        email = str(input("enter a valid email: "))

        c.execute("select * from users")
        for i in c:
            if i[0] == username or i[2] == email:
                print("sorry this username is already registerd, please select another username !")
                break
            elif password != cpassword:
                print("the passwords you have entered do not match, please try again !")
                break
            elif len(username) == 0 or len(email) == 0 or len(password) == 0:
                print("some of the forms are not complete, please try again !")
                break
            else:
                try:
                    sql_insert_query = """ INSERT INTO users
                                       (username, password, email) VALUES (%s,%s,%s)"""

                    insert_tuple_1 = (username ,password, email)
                    c.execute(sql_insert_query, insert_tuple_1)
                    mydb.commit()
                    print("Registration successfull !")
                    print(" ")
                    check_again = True
                    confirm = True
                    break

                except my.Error as error:
                    pass

        if confirm == True:
            break

    return check_again





def login():
    while True:
        confirm = False
        username = str(input("enter username: "))
        password = str(input("enter password: "))
        c.execute("select username,password from users")
        g = c.fetchall()
        # conditions
        if len(username) == 0 or len(password) == 0:
            print("some of the forms are not complete, please try again !")
            break
        else:
            for i in g:
                if i[0] == username and i[1] == password:
                    confirm = True
                    break
            else:
                print("the username does not match the password or the username does not exist")
                break

        if confirm == True:
            print("login successfull !")
            print(" ")
            return confirm
    return username
                
                

def hub():
    while True:
        print(" ")
        print("1.) DIET PLANNER ")
        print("2.) HELP FORUM")
        print("3.) PROFILE")
        print("4.) SAVED MEALS")
        print("5.) MEMBER AREA")
        print("6.) ABOUT")
        print("7.) LOGOUT")
        print(" ")
        choice = int(input("enter your choice: "))

        # logout
        if choice == 7:
            ask = str(input("Are you sure you want to log-out ?(y/n): "))
            if ask in ("Y","y"):
                print("loggin out......")
                break
            elif ask in("N","n"):
                continue
            else:
                print("<--! please provide a vaild input !--> ")
        
    



