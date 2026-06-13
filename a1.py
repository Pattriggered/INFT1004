#Author: <Patrick Triggell>
#Date: 1/6/26
#Task: INFT1004/INFT1006 Assignment 1 Library Book Management System

ficCount = 0
nonFicCount = 0
sciCount = 0
hisCount = 0
#Check that chosen amounts do not exzxceed the maximum per genre
def check_inventory_limit(fiction, nonFiction, science, history):
    if fiction > 30:
        return False
    elif nonFiction > 20:
        return False
    elif science > 15:
        return False
    elif fiction > 25:
        return False
    else:
        return True
#Initial inventory prompts thje user for each genres starting stock
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


def display_menu():
        print("Welcome to the main menu!")
        choice = input("Checkout/Return/Analysis/Restock/Summary/Quit: ").lower()
        return choice

#Checkout a book for a user, they select which genre to take from decreasing the stock level by 1
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

#Return book allows users to return borrowed books of specified genres, if no books are borrowed they cannot return any
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

#Analysis prints the current stock for each genre
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

#Restock shows current inventory and prompts for books to add per genre, if the book exceeds the max
#Display error message and return to main menu
def restock(fiction, nonFiction, science, history, ficCount, nonFicCount, sciCount, hisCount):
    print("The current inventory is: ")
    print("You have",fiction,"fiction books in stock")
    print("You have",nonFiction,"nonFiction books in stock")
    print("You have",science,"science books in stock")
    print("You havefic",history,"history books in stock")
    genre = input("Which genre would you like to restock? fiction/nonfiction/science/history: ").lower()
    if genre == "fiction":
        ficMax = 30-(fiction+ficCount)
        ficAmnt = input(f"How many fiction books would you like to restock? (Max: {ficMax}): " )
        if ficAmnt.isdigit():
            ficAmnt = int(ficAmnt)
            if ficAmnt > ficMax:
                print("Your number exceeds the stock limit")
            else:
                fiction += ficAmnt
                print("Your inventory has been updated you now have",fiction,"fiction books")
        else:
            print("Please enter a positive number")
    if genre == "nonfiction":
        nonFicMax = 20-(nonFiction+nonFicCount)
        nonFicAmnt = input(f"How many non-fiction books would you like to restock? (Max: {nonFicMax}): " )
        if nonFicAmnt.isdigit():
            nonFicAmnt = int(nonFicAmnt)
            if nonFicAmnt > nonFicMax:
                print("Your number exceeds the stock limit")
            if nonFicAmnt < 0:
                print("Please select a positive number")
            else:
                nonFiction += nonFicAmnt
                print("Your inventory has been updated you now have",nonFiction,"non-fiction books")
        else:
            print("Please enter a positive number")
    if genre == "science":
        sciMax = 15-(science+sciCount)
        sciAmnt = input(f"How many science books would you like to restock? (Max: {sciMax}): " )
        if sciAmnt.isdigit():
            sciAmnt = int(sciAmnt)
            if sciAmnt > sciMax:
                print("Your number exceeds the stock limit")
            if sciAmnt < 0:
                print("Please select a positive number")
            else:
                science += sciAmnt
                print("Your inventory has been updated you now have",science,"science books")
        else:
            print("Please enter a positive number")
    if genre == "history":
        hisMax = 25-(history+hisCount)
        hisAmnt = input(f"How many history books would you like to restock? (Max: {hisMax}): " )
        if hisAmnt.isdigit():
            hisAmnt = int(hisAmnt)
            if hisAmnt > hisMax:
                print("Your number exceeds the stock limit")
            if hisAmnt < 0:
                print("Please select a positive number")
            else:
                history += hisAmnt
                print("Your inventory has been updated you now have",history,"history books")
        else:
            print("Please enter a positive number")
    return fiction, nonFiction, science, history, ficCount, nonFicCount, sciCount, hisCount

def summary(ficCount,nonFicCount,sciCount,hisCount):
    print("You have borrowed",ficCount,"fiction books")
    print("You have borrowed",nonFicCount,"non-fiction books")
    print("You have borrowed",sciCount,"science books")
    print("You have borrowed",hisCount,"history books")

    return ficCount,nonFicCount,sciCount,hisCount

#Ends the program
def exit():
    print("Farewell!")
    

#Main function
fiction, nonFiction, science, history = initial_inventory()
valid = False
while not valid:
    choice = display_menu()
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
    elif choice == "restock":
        (fiction, nonFiction, science, history,  ficCount, nonFicCount,
        sciCount, hisCount) = restock(fiction, nonFiction, science,
        history, ficCount, nonFicCount, sciCount, hisCount)
    elif choice == "summary":
        (ficCount,nonFicCount,sciCount,hisCount) = summary(ficCount,
        nonFicCount,sciCount,hisCount)
    else:
        exit()
        valid = True

