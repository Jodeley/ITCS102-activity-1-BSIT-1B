# for i in range(1, 7, 1):
#     for j in range(6, i, -1):
#         print(" ", end=" ")
#     for k in range(1, i, 1):
#         print("* ", end=" ")
#     print()

col = eval(input("Enter the number of column/s ---> "))

for i in range(1, 11, 1):
    for j in range(1, col + 1, 1):
        print(f"{i}x{j}={i*j}", end="\t\t")
    print()