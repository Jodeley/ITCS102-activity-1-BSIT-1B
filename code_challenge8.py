# looping over a fixed range(1,11)
# Using the loop variable in calculations
# String formatting 

print("Multiplication Table\n")
fctrl = 1
nmbr = eval(input("Enter a number: "))
print("Multiplication Table for", nmbr, ":")
for x in range(1, 11):
  result = nmbr * x
  print(nmbr, "x", x, "=", result)