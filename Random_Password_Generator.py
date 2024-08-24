'''---Random Password Generator---'''
import random

import string

pass1=12
rand = string.ascii_letters + string.digits + string.punctuation
password = ""

for i in range(pass1):
    password += random.choice(rand)

print(password)
