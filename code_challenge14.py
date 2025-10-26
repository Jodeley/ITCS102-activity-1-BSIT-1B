anime_list = []
tuloy = True

while tuloy:  # simpler than "while tuloy == True"
    title = input("Enter the title of an anime (or type 'exit' to finish): ").strip()

    # check for exit first (use lower() so user can type Exit, EXIT, etc.)
    if title.lower() == "exit":
        print("You have exited the anime entry program.")
        tuloy = False
        break  # optional, tuloy = False is enough to stop the loop

    # ignore empty input
    if title == "":
        print("No title entered. Please type an anime title or 'exit'.")
        continue

    # add the (cleaned) title to the list and confirm
    anime_list.append(title.title())  # .title() makes nice capitalization
    print(f"'{title.title()}' has been added to your anime list.")

# after loop, show what was collected
if anime_list:
    print("\nYour anime list:")
    for i, a in enumerate(anime_list, start=1):
        print(f"{i}. {a}")
else:
    print("You did not add any anime.")
