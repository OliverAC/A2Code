from crop_class import *

class Wheat(Crop):
    """A wheat class crop"""
    #constructor
    def __init__(self):
        #call the parent class constructor
        # groth rate = 1 ; light = 2 waterneed = 3
        super().__init__(1,3,6)
        self._type = "Wheat"

    # overide grow method fpr subclass
    def grow(self,light,water):
        if light>= self._light_need and water >= self._water_need:
            if self._status == "Seedling" and water>=self._water_need:
                self._growth += self._growth_rate*1.8
            elif self._status == "Young" and water > self._water_need:
                self._growth += self._growth_rate*1.5
            else:
                self._growth += self._growth_rate
        # increment days growing
        self._days_growing+=1
        #update the status
        self._update_status()

    
def main():
    #Create a new potato crop
    wheat_crop = Wheat()
    print(wheat_crop.report())
    #manually_grow the crop
    manual_grow(wheat_crop)
    print(wheat_crop.report())
    manual_grow(wheat_crop)
    print(wheat_crop.report())

if __name__ == "__main__":
    main()
