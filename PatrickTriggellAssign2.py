#Author: <Patrick Triggell>
#Date: <17/6/26> – <upload date>
#Task: INFT1004 Assignment 2 – Library Management System – Part 2

import pandas as pd
import matplotlib

def load_inventory_from_csv():
    try:
        file = open('LibraryInventory.csv','r')
        file_content = file.readlines()
        print("File read successfully.")
        print(file_content)
        inventory = {}
        for line in file_content:
            genre, amount = line.strip().split(",")
            inventory[genre] = int(amount)
        print(inventory)
    except FileNotFoundError:
        print("File was not found.")

    
def display_inventory():
    pass


def add_new_genre():
    pass

def checkout_or_return():
    pass

def inventory_analysis_and_visualisation():
    pass

def save_inventory_to_csv():
    pass

def menu():
    print("Welcome to the main menu!")
    choice = input("What would you like to do display inventory/add new genre/checkout or return/analysis/save to csv")

load_inventory_from_csv()