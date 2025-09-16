name = input("What is your name?---> ").title()
print("Hello", name, "Welcome to Factorial Calculator!")
# let the user input number 

fctrl = 1
nmbr = eval(input("\nEnter the number ---> "))
for i in range(nmbr, 0, -1):
    fctrl *= i

print("The factorial number of", nmbr, "is", fctrl)