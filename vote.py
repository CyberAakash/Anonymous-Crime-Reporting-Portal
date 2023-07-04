import mysql.connector
import os

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="Ammppa@00",
  database="blockchain_network"
)

l1=[]
file = open("/home/itsmemuthu/Desktop/SEM_PROJECT/files/vote.txt",'r')
l = file.readlines()
for i in l:
  l1.append(i.replace('\n',""))
file.close()

aadhaar = l[0]

cursor = mydb.cursor()
cursor.execute("select * from login;")
result = cursor.fetchall()

for i in result:
  l = list(i)
  if l[0]==aadhaar[:16]:
    file = open("/home/itsmemuthu/Desktop/SEM_PROJECT/files/vote.txt",'w')
    file.write(l[3]+"\n")
    file.write(l[4]+"\n")
    file.write(l[5]+"\n")
    file.close()
    break


os.system('node /home/itsmemuthu/Desktop/SEM_PROJECT/backend/vote.js')
l1=[]
file = open("/home/itsmemuthu/Desktop/SEM_PROJECT/files/vote.txt",'r')
l = file.readlines()
for i in l:
  l1.append(i.replace('\n',""))
file.close()

mycursor = mydb.cursor()
statement = "insert into actions (hash, publickey, transactionid) VALUES (%s, %s, %s)"
val = (l1[0], l1[1], l1[2])
mycursor.execute(statement, val)
mydb.commit()

file = open("/home/itsmemuthu/Desktop/SEM_PROJECT/files/hashforcandidate.txt",'w')
file.write(aadhaar[16:]+"\n")
file.close()

os.system('python3 /home/itsmemuthu/Desktop/SEM_PROJECT/backend/hashforcandidate.py')

hc=[]
file = open("/home/itsmemuthu/Desktop/SEM_PROJECT/files/hashforcandidate.txt",'r')
l = file.readlines()
for i in l:
  hc.append(i.replace('\n',""))
file.close()

mycursor = mydb.cursor()
statement = "insert into candidate (name, hash, transactionid) VALUES (%s, %s, %s)"
val = (aadhaar[16:], hc[0] ,l1[2])
mycursor.execute(statement, val)
mydb.commit()

