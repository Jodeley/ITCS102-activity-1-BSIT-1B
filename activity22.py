import random

print("Welcome to the Number Guessing Game")

random_no = random.randint(1, 3)
tries = 0
tuloy = True

while tuloy == True:
    num = int(eval(input("Input an integer number ---> ")))
    tries += 1

    if num == random_no:
        print("CONGRATIOLATIONS, YOU'RE CORRECT")
        print(f"Only took {tries} tries")
        break
    else:
        print("WRONG, PLEASE TRY AGAIN!")
        print("Continue")
        continue