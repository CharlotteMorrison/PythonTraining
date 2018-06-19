#Write a program that asks for the height, weight of a person and gives them an ideal weigh.
#Write two programs, one that handles males, one that handles females

#formulas used
#Male:	123.89 lb + 3.11 lb per inch over 5 feet
#Female:	117.07 kg + 3 lb per inch over 5 feet

flag = raw_input("Enter M for male or F for Female: ")

#added in case the user enters a lower case letter
flag = flag.upper()

height = int(raw_input("Enter your height in inches: "))

if (flag == "M"):
    weight =  ((height-60) * 3.11) + 123.89
    print("Your ideal weight is:  " + str(weight))
elif (flag == "F"):
    weight =  ((height-60) * 3) + 117.07
    print("Your ideal weight is:  " + str(weight))
else:
    print("invalid selection")
