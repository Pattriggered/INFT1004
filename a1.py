ficCount = 0
nonFicCount = 0
sciCount = 0
hisCount = 0

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





fiction, nonFiction, science, history = initial_inventory()
