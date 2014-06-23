from animal_class import *

class Cow(Animal):
    """ A Cow """
    # a constructor
    def __init__(self):
        # call the parent constructor
        # growth rate = 1  food need = 2  waterneed = 3
        super().__init__(1,3,6)
        self._type = "Cow"

         # overide grow method for subclass
    def grow(self, food, water):
        if food>= self._food_need and water >= self._water_need:
            if self._status == "Calf" and water>=self._water_need:
                self._growth += self._growth_rate*5
            elif self._status == "Young" and water > self._water_need:
                self._growth += self._growth_rate*2
            else:
                self._growth += self._growth_rate
        # increment days growing
        self._days_growing+=1
        #update the status
        self._update_status()

def main():
    #Create a new Cow
    a_cow = Cow()
    print(a_cow.report())
    #manually_grow the Potato
    manual_grow(Animal)
    print(a_cow.report())
    manual_grow(a_cow)
    print(a_cow.report())



if __name__ == "__main__":
    main()
