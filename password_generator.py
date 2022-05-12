

import string 
import random
print("\nMinimum = 1, Maximum = 94")
def generate_password():
    length = int(input('\nEnter the length of password: '))
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    characters = lower + upper + num + symbols
    temp = random.sample(characters,length)
    password = "".join(temp)
    print(password)
generate_password()