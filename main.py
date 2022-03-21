import random
import string

#program cretes a randomized string of characters between 1 and 90.


length = int(input("\nEnter the desired length of password: "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all,length)

password = "".join(temp)

print(password)