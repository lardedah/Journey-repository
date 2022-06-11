temperatureinput = input ("What is the current temperature, in celsius? ")
temperatureinput = int(temperatureinput)
if temperatureinput > 45:
    print("Nice knowing you!")
elif temperatureinput >= 30:
    print ("what a day!\nnice!")
elif temperatureinput >= 20:
    print ("okay..!")
elif temperatureinput >= 10:
    print ("not bad..")
elif temperatureinput >= 0:
    print ("it is freezing!")
else:
    print ("R.I.P")


