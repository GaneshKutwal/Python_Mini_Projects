import random
import  string

print("Welcome to password generator ")
length = int(input("Enter the length of Password : "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
pun = string.punctuation
number = string.digits

all = lower + upper + pun + number

temp = random.sample(all, length)
password = "".join(temp)
print(password)