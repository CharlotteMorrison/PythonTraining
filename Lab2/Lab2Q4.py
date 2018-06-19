#Write a program that prompts the user to enterhis or her lat name and creates
#a login ID from the first 4 letter of the name in lower case
#and a random 3 digit integer.

import random

name = raw_input("Please enter your last name: ")

#make name lowercase
name = name.lower()

#split the string- only the first 4 letters
name = name[:4]

#choose random numbers (this is not a good solution, omits numbers like 001, 098) better solution
#would be to create 3 random numbers and concatenate them.
num = random.randint(100,999)
print("Your login ID is: " + name + str(num))