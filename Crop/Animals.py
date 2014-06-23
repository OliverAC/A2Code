from Cow_class import *
from Sheep_class import *

def display_menu():
    print()
    print("Which Animal would you like to create?")
    print()
    print("1. Cow")
    print("2. Sheep")
    print()
    print("Please select an option from the above menu")

def select_option():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option Selected:  "))
            if  choice in (1,2):
                 option_valid = True
            else:
                 print("Please enter a valid option")
        except ValueError:
                 print("Please enter a valid option")
    return choice

def create_animal():
    display_menu()
    choice = select_option()
    if choice == 1:
        Animal = Cow()
    elif choice == 2:
        Animal = Sheep()
    return Animal

def main():
    Animal = create_animal()
    manage_animal(Animal)

if __name__ == "__main__":
    main()
