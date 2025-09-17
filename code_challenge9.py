print("WELCOME TO THE PARROT SIMULATOR-THE ECHO CHAMBER! 🦜\n")

say = input("What do you want your parrot to say? ")
nmbr = eval(input("How many times should the parrot squawk it? "))
print("\nListen to your parrot:")

for x in range(nmbr):
    print("🦜 Squawk!", say)
