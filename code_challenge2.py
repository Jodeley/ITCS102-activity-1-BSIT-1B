n1 = int(input("Enter amount to deposit: "))
n2 = [1000, 500, 200, 100, 50, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for value in n2:
    count = n1 // value  # How many of this denomination
    if count > 0:
        print(f"{value} x {count}")
        n1 -= value * count  # Subtract the total of this denomination
