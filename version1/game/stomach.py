from food import Food
from poops import Poops
from health import Health
class Stomach:
    max_food_contents = 5 #maximum food allowed in stomach
    starting_empty_counter = 3 #actions that can be taken on an empty stomach before damage is applied
    empty_counter_damage = 1 #damage that occurs after empty counter is depleted
    starting_contents = [] #placeholder for possible starting food contents
    starting_food_counter = 0 #placeholder for starting food counter

    def __init__(self, poop_instance, health_instance):
        self.current_food_counter = self.starting_food_counter
        self.contents = self.starting_contents
        self.empty_counter = self.starting_empty_counter
        self.poop_instance = poop_instance
        self.health_instance = health_instance
    
    def __repr__(self):
        return f'food counter: {self.current_food_counter}, empty_counter: {self.empty_counter} contents: {self.contents}'

    def eat(self, food):
        #check if we have max items in contents already
        if len(self.contents) < self.max_food_contents:
            self.contents.insert(0,food)
            self.empty_counter = self.starting_empty_counter
            return 1
        else:
            #return false if we already have max food items in contents
            return -1

    def isFull(self):
        return len(self.contents) == self.max_food_contents

    def update(self, actions=1):
        if self.current_food_counter <= 0:
            #if no food counter, checks for contents in the stomach
            if self.contents:
                #if contents are found, begin processing the item at the beginning of the queue
                self.current_food_counter += self.contents[-1].TimeToProcess
                #reset empty_counter when a food is being digested
                self.empty_counter = self.starting_empty_counter
            else:
                #if no contents, subtract actions from empty counter to deal damage eventually
                if (self.empty_counter - actions) <= 0:
                    #decrement empty counter damage from the health bar
                    self.health_instance.lose_hp(self.empty_counter_damage)
                    #reset empty_counter
                    self.empty_counter = self.starting_empty_counter

                elif (self.empty_counter - actions) > 0:
                    self.empty_counter -= actions
                    
        elif self.current_food_counter > 0:
            #check if we are already processing food
            self.current_food_counter -= actions
            if self.current_food_counter <= 0:
                #if the current food finishes processing, we will remove it from contents and add poop, help, and harm values from the food to their respective classes
                popped_food = self.contents.pop()
                self.poop_instance.addPoops(popped_food.PoopValue)
                self.health_instance.add_hp(popped_food.HealthValue)
                self.health_instance.lose_hp(popped_food.HarmValue)

#Tests
#instantiate stomach, poops, and health
poops = Poops()
health = Health()
stomach = Stomach(poops,health)

#instantiate foods
normal = Food('normal food', 'normal')
helpful = Food('helpful food', 'helpful')
harmful = Food('harmful food', 'harmful')
poop = Food('poop', 'poop')

#The following tests run through eating food, and digesting it through updates where 1 action happens each update. Food gets digested, and 
#poops, hp, and counters are all updated as expected. 
stomach.eat(normal)
print(stomach.contents)
stomach.eat(helpful)
print(stomach.contents)
stomach.eat(harmful)
print(stomach.contents)
stomach.eat(poop)
print(stomach.contents)
stomach.eat(normal)
print(stomach.contents)

stomach.update()
print(stomach)
stomach.update()
print(stomach)
stomach.update()
print(stomach)
stomach.update()
print(stomach)
stomach.update()
print(stomach)
stomach.update()
print(stomach)
stomach.update()
print(stomach)
stomach.update()
print(stomach)
stomach.update()
print(stomach)
stomach.update()
print(stomach)
stomach.update()
print(stomach)
stomach.update()
print(stomach)
stomach.update()
print(stomach)
stomach.update()
print(stomach)
stomach.update()
print(stomach)
stomach.update()
print(stomach)
print(health)
print(poops)
stomach.update()
print(stomach)
stomach.update()
print(stomach)
stomach.update()
print(stomach)
print(health)


