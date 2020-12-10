import os
import messaging as mg 

stream = os.popen("df / | grep / | awk '{ print $5}' | sed 's/%//g'")
out = stream.read()
print out
useremails = ['email.com']

if out > 80:
    print useremails
    email = mg.Email(to=useremails, subject="Disk Usage High") 
    email.message('The disk usage is '+str(out)) 
    email.sendPlainText()

