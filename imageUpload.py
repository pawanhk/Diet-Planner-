import mysql.connector as my
import random
mydb = my.connect(host="localhost", user="pawan", database="dietplanner", password="Pawan23.Krishnan")
c = mydb.cursor()

fname = "dis"
lname = "guy"
email = "disguy@gmail.com"
password = "DSsd"
bio = "hello there"

genereateIMAGID = random.randint(1,500)
imageID = fname + str(genereateIMAGID)
print(imageID)


with open("/home/pawan/Desktop/DietPlanner V2/aplha 1.1/pic/tt3.png","rb") as f:
    data = f.read()
query = """
 insert into users (fname,lname,email,photo,bio,password,imageID) values(%s,%s,%s,%s,%s,%s,%s)
 """

t = (fname,lname,email,data,bio,password,imageID)
c.execute(query,t)
mydb.commit()

c.execute("select * from users")
g = c.fetchall()
for i in g:
    if i[7] == imageID:
        decypher = i[4]

with open("pic/"+imageID+".jpg","wb") as f:
    f.write(decypher)




