# for i in range(1,6):
#     for j in range(1, i, 1):
#         print(i, end=" ")
#     print(i)

for i in range(1, 6, 1):
    for j in range(7, i, -1):
        print(" ", end=" ")
    for k in range(1, 2 * i, 1):
        print("*", end=" ")
    print()