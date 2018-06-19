#Temperature converter
#Write a program that converts the temperature from Farenheit to Celcius

#get input (raw_input is Python 2, use just input in python 3
far = int(raw_input("Please enter a temperature in farenheight: "))

#compute celcius value
cel = (far - 32) / 1.8

#print value (must cast int to string to concatenate the response)
print(str(far) + " in farenheight is " + str(cel) + " in celcius.")