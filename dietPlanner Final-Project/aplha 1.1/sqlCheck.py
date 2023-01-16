import mysql.connector as my
mydb = my.connect(host="localhost", user="pawan", database="dietplanner", password="Pawan23.Krishnan")
c = mydb.cursor()




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
                confirm = True
                break

            except my.Error as error:
                pass


    if confirm == True:
        print("<-- welcome to diet planner --> ")
        break 
            
    

