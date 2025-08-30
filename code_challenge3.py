name = input("What is your name? ---> ")
fare = eval(input("Fare fee ---> "))
isStudent = input("Are you currently a student? (yes/no) ") 

if isStudent == 'yes'or isStudent == 'YES' :
	discount = fare * 0.2
	#fare -= discount
	new_fare = fare - discount
	print("Hi ",name, "your discount is ",discount, "and your new fare is",new_fare)

else:
	print("Sorry ",name, "your not eligible for a student discount") 