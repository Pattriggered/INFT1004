#Author: <Patrick Triggell>
#Date: <17/6/26> – <upload date>
#Task: INFT1004 Assignment 2 – Library Management System – Part 2

import pandas as pd
import matplotlib

#Seperate dictionary created to store maximum amounts per genre
maxAmnt = {"Fiction":30, "Nonfiction":20,"Science":15,"History":25}

#Using pandas import csv file and convert to a dictionart
def load_inventory_from_csv():
    try:
        df = pd.read_csv("LibraryInventory.csv",header = None) #load into pandas dataframe
        inventory = {}
        
        for i in range(len(df)):  #processing csv data into a dictionary
            genre = df[0][i]
            amount = int(df[1][i])
            inventory[genre] = amount
        print(inventory)
        return inventory

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
                        valid = True
                amount = int(input("How many books do you want to checkout? "))
                if amount <= 0:
                    print("must be a positive integer") 
                    valid = False
                else:
                    if inventory[genre] - amount < 0:
                        print("You cannot checkout more books than are available")
                        valid = False
                    else:
                        inventory[genre] -= amount
                        print("You have checked out",amount, "books from", genre)
                        valid = True                   
            else:
                print("Error! invalid input. Please choose from one of the options")
                valid = False
        elif prompt == "return" or prompt == "r":
            print("")
            valid = True
        else:
            print("Error! invalid input. Please choose from one of the options")
            valid = False
    return inventory

def inventory_analysis_and_visualisation():
    pass

def save_inventory_to_csv():
    pass

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


inventory = load_inventory_from_csv()
valid = False
while not valid:

    choice = display_menu()
    if choice == "1" or choice == "inventory":
        display_inventory(inventory)
    elif choice == "2" or choice == "add new genre":
        inventory, maxAmnt = add_new_genre(inventory)
    elif choice == "3" or choice == "checkout or return":
        inventory = checkout_or_return(inventory)
    elif choice == "6" or choice == "quit":
        print("Farewell!")
        valid = True