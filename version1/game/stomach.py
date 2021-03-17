from food import Food
from poops import Poops
class Stomach:
    def __init__(self):
        self.current_food_counter = 0
        self.contents = []
        self.empty_counter = 3
    
    def eat(self, food):
        #check if we have 5 items in contents already
        if len(self.contents) < 5:
            self.contents.insert(0,food)
            self.empty_counter = 3
            return 1
        else:
            #return false if we already have 5 food items in contents
            return -1

    def isFull(self):
        return len(self.contents) == 5

    def update(self, poops_instance, health_instance, actions=1):
        if self.current_food_counter <= 0:
            #if no food counter, checks for contents in the stomach
            if self.contents:
                #if contents are found, begin processing the item at the beginning of the queue
                self.current_food_counter += self.contents[-1].TimeToProcess
                #reset empty_counter when a food is being digested
                self.empty_counter = 3
            else:
                #if no contents, subtract actions from empty counter to deal damage eventually
                if (self.empty_counter - actions) <= 0:
                    #decrement 1 from the health bar
                    #reset empty_counter to 3
                    self.empty_counter = 3
                elif (self.empty_counter - actions) > 0:
                    self.empty_counter -= actions
                    
        elif self.current_food_counter > 0:
            #check if we are already processing food
            self.current_food_counter -= actions
            if self.current_food_counter <= 0:
                #if the current food finishes processing, we will remove it from contents and add the poop value to our poops
                poop_instance.amount += (self.contents.pop().PoopValue)
        pass








