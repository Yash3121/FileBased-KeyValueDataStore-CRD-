import threading                    #This is for Python 3.0 or above
from threading import *
import time
import re

d = {}
val = []

# CREATE OPERATION

def create() :
    print("Enter the Key-Value pair : \n")
    key, value = map(str, input().split())
    key = int(key)
    print("\n")
    print("Enter the TimeOut : \n")
    timeout = int(input())
    print("\n")
    timeout = timeout * 60
    spl_char_num = re.compile('[@_!#$%^&*()<>?/\|}{~:0123456789]')
    if key in d :
        print("Error! : This Key already Exists! \n")
    else :
        if len(d) < (1024 * 1020 * 1024) and key <= (16 *1024 * 1024) and spl_char_num.search(value) == None :             #To keep the size of the file storing Data < 1GB, JSON object capped at 16KB AND to elliminate the special characters.
            if timeout == 0 :
                val = [value, timeout]
            else :
                val = [value, time.time() + timeout]
            if len(value) <= 32 :                 #To keep the key always capped at 32-chars
                d[key] = val
                print("Data inside the Text-File : \n",d)
                print("Key-Value pair and TimeOut Created! \n") 
            else:
                print("Error! : Memory-Limit Exceeded! \n")
        else:
            print("Error! : Invalid Key_Name! Key_Name must contain only Alphabets and No Special Characters or Numbers! \n")

# READ OPERATION

def read() :
    print("Enter the Key to Read the Data : \n")
    key = int(input())
    print("\n")
    if key not in d :
        print("Error! : Given Key doesn't match any Data. Please enter a Valid_Key! \n")
    else :
        r = d[key]
        if r[1] != 0 :
            if time.time() < r[1] :                        #To Compare the Present time with the Expiry time.
                result = str(key) + " : " + str(r[0])          #To store the Data in the JSON-Object format (ie) "Key : Value" pair.
                print("The Key-Value pair for the Key",key,"is : \n",result)
            else :
                print("Error! : Time-To-Live of",key,"has Expired! \n")
        else:
            result = str(key) + " : " + str(r[0])               #To store the Data in the JSON-Object format (ie) "Key : Value" pair.
            print("The Key-Value pair for the Key",key,"is : \n",result)

# DELETE OPERATION

def delete() :
    print("Enter the Key to Delete : \n")
    key = int(input())
    print("\n")
    if key not in d :
        print("Error! : Key doesn't Exists! \n")
    else :
        r = d[key]
        if r[1] != 0 :
            if time.time() < r[1] :                        #To Compare the Present time with the Expiry time. 
                del d[key]
                print("Data inside the Text-File after Deletion of",key,"'s Key_value pair : \n",d)
                print("Successfully Deleted! \n")
            else:
                print("Error! : Time-To-Live of",key,"has Expired! \n")
        else:
            del d[key]
            print("Data inside the Text-File after Deletion of",key,"'s Key_value pair : \n",d)
            print("Successfully Deleted! \n")

# STORING DATA IN A TEXT-FILE

def store() :
    file = open("yash.txt", 'w+') 
    strc = str(d)
    file.write(strc)
    file = open("yash.txt", 'r')
    print(file.read())
    file.close()

# MAIN FUNCTION

print("\n")
print("File-Based Key-Value DataStore(CRD)! \n")
i = 1
while(i != 5) :
    print("Select the Operation(1 or 2 or 3 or 4) : \n")
    print("1. Create \n2. Read \n3. Delete \n4. Exit\n")
    option = int(input())
    print("\n")
    if(option == 1) :
        create()
    elif(option == 2) :
        read()
    elif(option == 3) :
        delete()
    elif(option == 4) :
        store()
        exit(0)
    else :
        print("Invalid Option! \n")

# THREADING OPERATION

print("Final Data inside the Text-File after CRD Operations : \n",d)
t1 = threading.Thread(target = (create or read or delete))
t1.start()
time.sleep(1)
t2 = threading.Thread(target = (create or read or delete))
t2.start()
time.sleep(1)