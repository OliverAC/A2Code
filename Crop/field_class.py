from potato_class import *
from wheat_class import * 
from Sheep_class import *
from Cow_class import *

class Field:
    """ Simulate a fiel that can contain animals and plants"""

    #constructor
    def __init__(self,max_animals, max_crops):
        self._crops =[]
        self._animals = []
        self._max_animals = max_animals
        self._max_crops = max_crops

def main():
    new_field = Field(5,2)
    print(new_field._crops)
    print(new_field._animals)
    print(new_field._max_animals)
    print(new_field._max_crops)

if __name__ == "__main__":
    main()
