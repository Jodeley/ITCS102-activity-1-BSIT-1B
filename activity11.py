temp = eval(input("Enter the temperature "))

if temp <= 0 :
	print("The temperature is below freezing")
elif temp >= 1 and temp <= 15 :
	print("The temperature is extremely cold")
elif temp >= 16 and temp <= 30 :
	print("The temperature is cold")
elif temp >= 31 and temp <= 38 :
	print("The temperature is lukewarm")
elif temp >= 39 and temp <= 42 :
	print("The temperature is warm")
elif temp >= 43 and temp <= 50 :
	print("The temperature is hot")
elif temp >= 51 and temp <= 60 :
	print("The temperature is extremely hot")
elif temp >= 61 :
	print("The temperature is burning")

else:
	print("Invalid temperature")