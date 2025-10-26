name = input('Enter your name ---> ')
print("********************\nODD NUMBER SUMMATION\n********************")
tuloy = True
sum = 0
odd = ""

while tuloy == True:
    num = eval(input("Input a random number ---> "))

    if num %2 == 1:
        print("ODD NUMBER DETECTED, code continues")
        sum += num
        odd += str(num) + " "
        continue
    elif num == 0:
        print("Progrram Stops!!!")
        break
    else:
        if num %2 == 0:
            print("EVEN NUMBER DETECTED, continue")
        else:
            print("Invalid Inut")
        continue
print(f"Hi {name}, the sum of all  odd number is {sum}")
print(f"Odd numbers detected included the following {odd}")



