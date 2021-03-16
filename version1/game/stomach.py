class Stomach:
    def __init__(self):
        #having trouble starting out the game.
        self.current_food_counter = 0
        self.contents = []
        self.poops = 0
    
    def eat(self, food):
        #check if we have 5 items in contents already
        if len(self.contents) < 5:
            self.contents.insert(0,food)
            return 1
        else:
            #return false if we already have 5 food items in contents
            return -1


    def update(self):
        if self.current_food_counter <= 0:
            #if no food counter, checks for contents in the stomach
            if self.contents:
                #if contents are found, begin processing the item at the beginning of the queue
                self.current_food_counter += self.contents[-1].TimeToProcess
            else:
                #if no contents found, return false to indicate we cannot process food at the moment. 
                return -1
        elif self.current_food_counter > 0:
            #check if we are already processing food
            self.current_food_counter -= 1
            if self.current_food_counter <= 0:
                #if the current food finishes processing, we will remove it from contents and add the poop value to our poops
                self.poops += (self.contents.pop().PoopValue)
        pass





