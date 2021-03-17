from food import Food
from poops import Poops
from health import Health
class Stomach:
    max_food_contents = 5 #maximum food allowed in stomach
    starting_empty_counter = 3 #actions that can be taken on an empty stomach before damage is applied
    empty_counter_damage = 1 #damage that occurs after empty counter is depleted
    starting_contents = [] #placeholder for possible starting food contents
    starting_food_counter = 0 #placeholder for starting food counter

    def __init__(self):
        self.current_food_counter = starting_food_counter
        self.contents = starting_contents
        self.empty_counter = starting_empty_counter
    
    def eat(self, food):
        #check if we have max items in contents already
        if len(self.contents) < max_food_contents:
            self.contents.insert(0,food)
            self.empty_counter = starting_empty_counter
            return 1
        else:
            #return false if we already have max food items in contents
            return -1

    def isFull(self):
        return len(self.contents) == max_food_contents

    def update(self, poops_instance, health_instance, actions=1):
        if self.current_food_counter <= 0:
            #if no food counter, checks for contents in the stomach
            if self.contents:
                #if contents are found, begin processing the item at the beginning of the queue
                self.current_food_counter += self.contents[-1].TimeToProcess
                #reset empty_counter when a food is being digested
                self.empty_counter = starting_empty_counter
            else:
                #if no contents, subtract actions from empty counter to deal damage eventually
                if (self.empty_counter - actions) <= 0:
                    #decrement empty counter damage from the health bar
                    health_instance.lose_hp(empty_counter_damage)
                    #reset empty_counter
                    self.empty_counter = starting_empty_counter

                elif (self.empty_counter - actions) > 0:
                    self.empty_counter -= actions
                    
        elif self.current_food_counter > 0:
            #check if we are already processing food
            self.current_food_counter -= actions
            if self.current_food_counter <= 0:
                #if the current food finishes processing, we will remove it from contents and add the poop value to our poops
                poop_instance.addPoops(self.contents.pop().PoopValue)
        pass








