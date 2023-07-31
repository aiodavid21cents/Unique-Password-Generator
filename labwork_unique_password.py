# Build a program that generates 15 unique password characters.

__name__ == "__main__"

import random
import string

print('hello, welcome to your unique password generator!')

length = 15

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lowercase + uppercase + num + symbols

temp = random.sample(all, length)

password = ''.join(temp)

print(password)