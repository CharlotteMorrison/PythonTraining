pos = ["noun", "noun", "noun", "verb", "verb", "verb", "noun", "noun", "verb", "adjective", "adjective", "noun"]
words = []
count = 0;
print("Mad Lib with Lists")
print("")

for i in pos:
    part = pos[count]
    temp = raw_input("Enter a(n) " + part)
    words.insert(len(words), temp)
    count+=1
print(" ")
print("________________________________________________________________________________________")
print(" ")
print("HOW TO INSTALL A PRINTER")
print(" ")
print("________________________________________________________________________________________")
print(" ")
print("Click the " + words[0] + " button, and then, on the " + words[1] + " menu, click " + words[2] + " and Printers.")
print("Click " + words[3] + " a printer.")
print("In the Add Printer wizard, " + words[4] + " Add a local printer.")
print("On the " + words[5] + " a printer port page, make sure that the Use an existing " + words[6] + " button and then click Next.")
print("On the Install the printer " + words[7] + " page, select the printer manufacturer and model, and then " + words[8] + " Next.")
print("If your printer isn't listed, click Windows Update, and then wait while Windows checks for " + words[9] + " drivers.")
print("If none are available and you have the " + words[10] + " CD, click Have Disk, browse to the " + words[11] + " where the printer driver is located.")
print("Click Finish")