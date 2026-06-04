ficCount = 0
nonFicCount = 0
sciCount = 0
hisCount = 0

#Initial inventory
def initial_inventory():
    valid = False
    while not valid:
        fiction = input("Please select how many books you would like in fiction (Max 30): ")
        if fiction.isdigit():
            fiction = int(fiction)
            if 0 <= fiction <= 30:
                print("You have chosen ",fiction, "fiction books")
                valid = True
            else:
                print("Please select a number between 0 and 30")
        else:
            print("Please enter a positive number")

    valid = False
    while not valid:
        nonFiction = input("Please select how many books you would like in non-fiction (Max 20): ")
        if nonFiction.isdigit():
            nonFiction = int(nonFiction)
            if 0 <= nonFiction <= 20:
                print("You have chosen ",nonFiction, "non-fiction books")
                valid = True
            else:
                print("Please select a number between 0 and 20")
        else:
            print("Please enter a positive number")

    valid = False
    while not valid:
        science = input("Please select how many books you would like in science (Max 15): ")
        if science.isdigit():
            science = int(science)
            if 0 <= science <= 15:
                print("You have chosen ",science, "science books")
                valid = True
            else:
                print("Please select a number between 0 and 15")
        else:
            print("Please enter a positive number")

    valid = False
    while not valid:
        history = input("Please select how many books you would like in history (Max 25): ")
        if history.isdigit():
            history = int(history)
            if 0 <= history <= 25:
                print("You have chosen ",history, "history books")
                valid = True
            else:
                print("Please select a number between 0 and 25")
        else:
            print("Please enter a positive number")
    
    return fiction, nonFiction, science, history

def menu():
    print("Welcome to the main menu!")
    choice = input("Checkout/Return/Analysis/Restock/Summary/Quit: ").lower()
    return choice


def checkout(fiction, nonFiction, science, history, ficCount, nonFicCount, sciCount, hisCount):
    genre = input("Which genre would you like to choose from fiction/nonfiction/science/history: ").lower()
    if genre == "fiction":
        if fiction > 0:
            fiction -= 1
            ficCount += 1
            print("There are now ",fiction, "fiction books available and you now have",ficCount, "fiction books")
        elif fiction == 0:
            print("No books are available in fiction")
    elif genre == "nonfiction":
        if nonFiction > 0:
            nonFiction -= 1
            nonFicCount += 1
            print("There are now ",nonFiction, "nonFiction books available and you now have",nonFiction, "nonFiction books")
        elif nonFiction == 0:
            print("No books are available in non-fiction")
    elif genre == "science":
        if science > 0:
            science -= 1
            sciCount += 1
            print("There are now ",science, "science books available and you now have",science, "science books")
        elif science == 0:
            print("No books are available in science")
    elif genre == "history":
        if history > 0:
            history -= 1
            hisCount += 1
            print("There are now ",history, "history books available and you now have",hisCount, "history books")
        elif history == 0:
            print("No books are available in history")
    else:
        print("Please choose from one of the available genres")

    return fiction, nonFiction, science, history, ficCount, nonFicCount, sciCount, hisCount

        




#Main function
fiction, nonFiction, science, history = initial_inventory()
choice = menu()
if choice == "checkout":
    (fiction, nonFiction, science, history, ficCount, nonFicCount, 
    sciCount, hisCount) = checkout(fiction, nonFiction, science, 
    history, ficCount, nonFicCount, sciCount, hisCount)
elif choice == "return":
    



