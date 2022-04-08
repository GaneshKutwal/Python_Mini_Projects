import os
import math
import random
import smtplib


digits = "0123456789"
otp = ""

for i in range(6):
    otp += digits[math.floor(random.random()*10)]

msg = otp + " is your OTP"

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

#Enter Mail Id And App Password
s.login("mail id", 'app password')
emailid = input("Enter your email : ")
#Entered Mail Id
s.sendmail('mail id', emailid, msg)
a = input("Enter your otp : ")
if a == otp:
    print("Varified")
else:
    print("Please check your otp again")