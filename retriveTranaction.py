import urllib.request as ur
import mysql.connector
import os
import json

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="Ammppa@00",
  database="blockchain_network"
)

cursor = mydb.cursor()
cursor.execute("select * from actions;")
result = cursor.fetchall()

Paadhar=[]
file = open("details.txt",'r')
l = file.readlines()
for i in l:
    Paadhar.append(i.replace('\n',""))
file.close()


Phash=[]
file = open("hash.txt",'r')
l = file.readlines()
for i in l:
    Phash.append(i.replace('\n',""))
file.close()



for i in result:
    l = list(i)
    link = "http://localhost:9984/api/v1/transactions?asset_id="+l[2]
    f = ur.urlopen(link)
    myfile = f.read()
    file = open("/home/itsmemuthu/Desktop/SEM_PROJECT/files/transaction.json",'w')
    output = str(myfile)
    file.write(output[3:len(output)-4])

    file = open("/home/itsmemuthu/Desktop/SEM_PROJECT/files/transaction.json",'r')
    l=file.readlines()
    res = json.loads(l[0])
    # print(l['data']['login']['Action'])
    # print()
    try:
        status = res['asset']['data']['Vote']['Status']
        publickey = res['asset']['data']['Vote']['Public key']
        print(status)
        if status == 'Successfully voted' and p[1] == publickey:
            file = open("/home/itsmemuthu/Desktop/SEM_PROJECT/files/status.txt",'w')
            file.write("YES\n")
            #file.write(status+"\n")
            file.write(res['asset']['data']['Vote']['Who Voted']+"\n")
            file.write(res['id']+"\n")
            file.write(res['asset']['data']['Vote']['Time']+"\n")
            file.close()
    except:
        print()
    l1=[]
    try:
        file = open("/home/itsmemuthu/Desktop/SEM_PROJECT/files/status.txt",'r')
        l = file.readlines()
        for i in l:
            l1.append(i.replace('\n',""))
        file.close()
        if l1[0] == "YES":
            break
    except:
        print()