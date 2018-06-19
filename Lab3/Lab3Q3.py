#Write a program that asks the user the type of conversion that needs to be done.
#Based on the user choice it converts the temperature from Farenheight to Celcius
#or the other way.  The user should enter the Farenheight or Celcius temperature.

flag = raw_input("Enter F to convert to Farenheight, enter C to convert to celcius:")

#added in case the user enters a lower case letter
flag = flag.upper()

if (flag == "F"):
    tempInput = int(raw_input("Please enter a celcius temperature: "))
    farenheight = (tempInput * 1.8) + 32
    print(str(tempInput) + "C, is " + str(farenheight) + "F.")
elif (flag == "C"):
    tempInput = int(raw_input("Please enter a farenheight temperature: "))
    celcius = (tempInput - 32) / 1.8
    print(str(tempInput) + "F, is " + str(celcius) + "C.")
else:
    print("invalid selection")
