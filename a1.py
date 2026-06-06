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
            print("There are now ",fiction, "fiction books available and you have now borrowed",ficCount, "fiction books")
        elif fiction == 0:
            print("No books are available in fiction")
    elif genre == "nonfiction":
        if nonFiction > 0:
            nonFiction -= 1
            nonFicCount += 1
            print("There are now ",nonFiction, "nonFiction books available and you have now borrowed",nonFiction, "nonFiction books")
        elif nonFiction == 0:
            print("No books are available in non-fiction")
    elif genre == "science":
        if science > 0:
            science -= 1
            sciCount += 1
            print("There are now ",science, "science books available and you have now borrowed",science, "science books")
        elif science == 0:
            print("No books are available in science")
    elif genre == "history":
        if history > 0:
            history -= 1
            hisCount += 1
            print("There are now ",history, "history books available and you have now borrowed",hisCount, "history books")
        elif history == 0:
            print("No books are available in history")
    else:
        print("Please choose from one of the available genres")

    return fiction, nonFiction, science, history, ficCount, nonFicCount, sciCount, hisCount

def return_book(fiction, nonFiction, science, history, ficCount, nonFicCount, sciCount, hisCount):
    genre = input("Which genre would you like to return to? fiction/nonfiction/science/history: ").lower()        
    if genre == "fiction":
        if ficCount == 0:
            print("You have not borrowed any books from fiction")
        elif fiction == 30:
            print("The inventory is full for fiction")
        else:
            fiction += 1
            ficCount -= 1
            print("You have successfully returned a fiction book, you have",ficCount,"remaining fiction books")
    if genre == "nonfiction":
        if nonFicCount == 0:
            print("You have not borrowed any books from non-fiction")
        elif nonFiction == 30:
            print("The inventory is full for non-fiction")
        else:
            nonFiction += 1
            nonFicCount -= 1
            print("You have successfully returned a non-fiction book, you have",nonFicCount,"remaining non-fiction books")
    if genre == "science":
        if sciCount == 0:
            print("You have not borrowed any books from science")
        elif science == 30:
            print("The inventory is full for science")
        else:
            science += 1
            sciCount -= 1
            print("You have successfully returned a science book, you have",sciCount,"remaining science books")
    if genre == "history":
        if hisCount == 0:
            print("You have not borrowed any books from history")
        elif history == 30:
            print("The inventory is full for history")
        else:
            history += 1
            hisCount -= 1
            print("You have successfully returned a history book, you have",hisCount,"remaining history books")
        
    return fiction, nonFiction, science, history, ficCount, nonFicCount, sciCount, hisCount

def analysis(fiction, nonFiction, science, history):
    if (fiction/30)*100 >= 75:
        print(f'The inventory status for fiction is "High" {(fiction/30)*100:.2f}%')
    elif 50 <= (fiction/30)*100 < 74:
        print(f'The inventory status for fiction is "Okay" {(fiction/30)*100:.2f}%')
    else:
        print(f'The inventory status for fiction is "Low" {(fiction/30)*100:.2f}%')
    if (nonFiction/20)*100 >= 75:
        print(f'The inventory status for non-fiction is "High" {(nonFiction/20)*100:.2f}%')
    elif 50 <= (nonFiction/20)*100 < 74:
        print(f'The inventory status for non-fiction is "Okay" {(nonFiction/20)*100:.2f}%')
    else:
        print(f'The inventory status for non-fiction is "Low" {(nonFiction/20)*100:.2f}%')
    if (science/15)*100 >= 75:
        print(f'The inventory status for science is "High" {(science/15)*100:.2f}%')
    elif 50 <= (science/15)*100 < 74:
        print(f'The inventory status for science is "Okay" {(science/15)*100:.2f}%')
    else:
        print(f'The inventory status for science is "Low" {(science/15)*100:.2f}%')
    if (history/25)*100 >= 75:
        print(f'The inventory status for history is "High" {(history/25)*100:.2f}%')
    elif 50 <= (history/25)*100 < 74:
        print(f'The inventory status for history is "Okay" {(history/25)*100:.2f}%')
    else:
        print(f'The inventory status for history is "Low" {(history/25)*100:.2f}%')

    return fiction, nonFiction, science, history,


def exit():
    print("Farewell!")
    

#Main function
fiction, nonFiction, science, history = initial_inventory()
valid = False
while not valid:
    choice = menu()
    if choice == "checkout":
        (fiction, nonFiction, science, history, ficCount, nonFicCount, 
        sciCount, hisCount) = checkout(fiction, nonFiction, science, 
        history, ficCount, nonFicCount, sciCount, hisCount)
    elif choice == "return":
        (fiction, nonFiction, science, history, ficCount, nonFicCount, 
        sciCount, hisCount) = return_book(fiction, nonFiction, science, 
        history, ficCount, nonFicCount, sciCount, hisCount)
    elif choice == "analysis":
        (fiction, nonFiction, science, history) = analysis(fiction, 
        nonFiction, science, history)
    else:
        exit()
        valid = True

