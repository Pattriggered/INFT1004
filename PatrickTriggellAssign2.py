#Author: <Patrick Triggell>
#Date: <17/6/26> – <upload date>
#Task: INFT1004 Assignment 2 – Library Management System – Part 2

import math as m
import pandas as pd
import matplotlib.pyplot as plt

maxAmnt = {} #Seperate dictionary created to store maximum amounts per genre

#Using pandas import csv file and convert to a dictionary
def load_inventory_from_csv():
    try:
        df = pd.read_csv("LibraryInventory.csv",header = None) #load into pandas dataframe
        inventory = {}
        
        for i in range(len(df)):  #processing csv data into a dictionary
            genre = df[0][i]
            amount = int(df[1][i])
            inventory[genre] = amount
        maxAmnt = inventory.copy() #store initial quantites in max dictionary
        print(inventory)
        print(maxAmnt)
        return inventory, maxAmnt

    except FileNotFoundError:
        print("File was not found.")

#Presents all genres and their current book counts neatly formatted
def display_inventory(inventory):
    for genre, amount in inventory.items():
        print("You have",amount,"books in",genre.title())
    
#Takes user input to create a unique genre with a positive integer for the amount, updated inventory is printed
#After successful addition and maximum dictionary is updated with new genre and max amount
def add_new_genre(inventory):
    valid = False
    while not valid:
        genre = input("What new genre would you like to add? ")
        if genre.lower() in [key.lower() for key in inventory]: #Uniqueness check
            print("Genre name must be unique")
        else:
            valid = True
    valid = False
    while not valid:
        amount = int(input("How many books would you like to add? ")) 
        if amount <= 0: #For positive integers assuming the exclusion of 0
            print("Initial count must be a positive integer")
            valid = False
        else:
            valid = True
    inventory[genre.title()] = amount
    print("You successfully created", genre, "and added", amount, "books")
    maxAmnt[genre.title()] = amount #Stores max for this genre in the max dictionary
    print(maxAmnt)
    display_inventory(inventory)
    return inventory, maxAmnt

#Allows the user to either checkout or return books
def checkout_or_return(inventory):
    display_inventory(inventory)
    valid = False
    while not valid:
        prompt = input("Would you like to Checkout (C) or Return (R)").lower()
        if prompt == "checkout" or prompt == "c":
            genre = input("Which genre would you like to checkout from? ")
            
            if genre.lower() in [key.lower() for key in inventory]:
                for key in inventory: #compares the input to the keys in inventory dictionary
                    if key.lower() == genre.lower():
                        genre = key
                        break
                while True:
                    try:
                        amount = int(input("How many books do you want to checkout? "))
                        if amount <= 0:
                            print("Must be a positive integer") 
                        else:
                            if inventory[genre] - amount < 0: #positivity check
                                print("You cannot checkout more books than are available")
                            else:
                                inventory[genre] -= amount #updates inventory
                                print("You have checked out",amount, "books from", genre)
                                return inventory
                    except ValueError:
                        print("Please select a number")
            else:
                print("Error! invalid input. Please choose from one of the genres in your inventory")
                valid = False
        elif prompt == "return" or prompt == "r":
            genre = input("Which genre would you like to return to? ")
            
            if genre.lower() in [key.lower() for key in inventory]:
                for key in inventory: #compares the input to the keys in inventory dictionary
                    if key.lower() == genre.lower():
                        genre = key
                        break
                while True:
                    try:
                        amount = int(input("How many books do you want return? "))
                        if amount <= 0:
                            print("Must be a positive integer") 
                        else:
                            inventory[genre] += amount
                            print("You have returned",amount, "books from", genre)                           
                            return inventory
                    except ValueError:
                            print("Please select a number")
            else:
                    print("Error! invalid input. Please choose from one of the genres in your inventory")
                    valid = False
        else:
                print("Error! invalid input. Please choose from one of the options")
                valid = False

#provides both text and visual report of an inventory analysis for the user
def inventory_analysis_and_visualisation(inventory, maxAmnt):
    #Creating a text report
    table = pd.DataFrame({"Genre":list(inventory.keys()), "Books":list(inventory.values())})
    print("The total number of books in the library is",table["Books"].sum())
    table["Average"] = (table["Books"]/len(table)).apply(m.ceil) #takes the rounded up nearest whole number
    print(table)
    for genre in inventory:
        status = (inventory[genre]/maxAmnt[genre]) * 100
        if status >= 75:
            level = "High"
        elif 50 <= status < 75:
            level = "OK"
        else:
            level = "Low"
        print(f"{genre} stock status is at {status:.2f}% which is {level}")
    
    
    #Creating a bar plot
    plt.bar(table["Genre"], table["Books"])
    plt.title("Library")
    plt.xlabel("Genres")
    plt.ylabel("Current Inventory Count")
    plt.show()

    return inventory, maxAmnt

#Write the updated inventory back to LibraryInventory.csv
def save_inventory_to_csv(inventory):
    try:

        df = pd.DataFrame(list(inventory.items()))
        df.to_csv("LibraryInventory.csv", header = False, index = False)
        print("Saving was successful!")
    
    except PermissionError:
        print("The file could not be written")

    except OSError:
        print("An error occurred whilst attempting to save the file")
    
    return inventory

#Saves the latest inventory and exists the program with a goodbye message
def quit_program(inventory):
    try:

        df = pd.DataFrame(list(inventory.items()))
        df.to_csv("LibraryInventory.csv", header = False, index = False)
        print("File was saved")
    
    except PermissionError:
        print("The file could not be written")

    except OSError:
        print("An error occured whilst attempting to save the file")
    
    print("Farewell!")
    
    return inventory

#Displays menu items
def display_menu():
    print("Welcome to the main menu!")
    choice = input("Please choose from one of these options:"
                "\n(1)Inventory"
                "\n(2)Add New Genre"
                "\n(3)Checkout or Return"
                "\n(4)Analysis"
                " \n(5)Save Changes to CSV"
                " \n(6)Quit\n").lower()
    return choice

#Main program
inventory, maxAmnt = load_inventory_from_csv()
valid = False
while not valid:

    choice = display_menu()
    if choice == "1" or choice == "inventory":
        display_inventory(inventory)
    elif choice == "2" or choice == "add new genre":
        inventory, maxAmnt = add_new_genre(inventory)
    elif choice == "3" or choice == "checkout or return":
        inventory = checkout_or_return(inventory)
    elif choice == "4" or choice == "analysis":
        inventory, maxAmnt = inventory_analysis_and_visualisation(inventory, maxAmnt)
    elif choice == "5" or choice == "save changes to csv":
        inventory = save_inventory_to_csv(inventory)
    elif choice == "6" or choice == "quit":
        inventory = quit_program(inventory)
        valid = True