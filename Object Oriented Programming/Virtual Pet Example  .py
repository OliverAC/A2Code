import random

# Class Definition
class VirtualPet:
    """ A representation of a virtual pet """
    def __init__(self,name):
        print("I've Been Born!")
        self.name = name
        self.hunger = 10
        self.energy = 1
        self.fitness = 1
        
    #Methods  (Still inside the class)
    def talk(self,speak):
        if speak == 1:
            print ("Hi i'm {0}, Your Pet.".format(self.name))
        if speak == 2:
            print("La La La")
        if speak == 3:
            print("Waaaaaaaaaaaaaaaaaaaaaaaa")
        if speak == 4:
            print("When I grow up... I want to be an adult!")

    def exercise(self, what_exercise):
    if what_exercise == 1 and self.hunger <4  and self.energy > 4 :
        print("")
    elif what_exercise == 2:
    elif what_exercise == 3:
    elif what_exercise == 4:

    def feed(self, food):
        print()
        if self.hunger>0 and food == 1:
            self.hunger -= 1
            self.energy += 5
            print("Yum Yum ")
        elif self.hunger>=3 and food == 2:
            self.hunger -= 4
            self.energy += 4
            print("Yuck .")
        elif self.hunger>0 and food == 3:
            self.hunger -= 2
            self.energy += 2
            print("Yum Soup")
        else:
            print("Im Full Thanks.")

def main():
    # Create an instance of a class
    name = input("Please enter your pets name:  ")
    pet_one = VirtualPet(name)                      # Pass the name into Virtual pet
    menu_option = 0
    while menu_option != 9:
        menu_option = display_menu()
        if menu_option == 1:
            what_to_say = speak()
            pet_one.talk(what_to_say)
        if menu_option == 2:
            print(pet_one.hunger)
            food = what_food()
            pet_one.feed(food)
            print(pet_one.hunger)
        if menu_option == 3:
            print("Name = {0}".format(pet_one.name))
            print("Hunger = {0}".format(pet_one.hunger))
            print("Energy = {0}".format(pet_one.energy))
        if menu_option == 4:
            exercise()

def exercise():
    what_exercise =random.randint(1,4)


def speak():
    what_to_say = random.randint(1,4)
    return what_to_say




def display_menu():
    print()
    print("1) Talk")
    print("2) feed your pet")
    print("3) Check how you pet is")
    print("4) Exercise")
    print("9) Quit")
    print()
    menu_option = int(input("What should your pet do? "))
    print()
    return (menu_option)

def what_food():
    print("1)Sweets")
    print("2)Vegetables")
    print("3)Soup")
    food = int(input("what would you like to feed you pet?  "))
    return food

if __name__ == "__main__":
    main()
    
    
