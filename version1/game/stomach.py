class Stomach:
    def __init__(self):
        self.current_food_counter = 0
        self.contents = []
        self.poops = 0
    
    def eat(self, food):
        self.contents.insert(0,food)
        

    def update(self):
        '''method to update the stomach after an action is
        performed. If there are contents in the stomach, and the counter is greater than 0, 
        we'll digest the food and remove from the stomach counter and add to the poops count'''
        if self.contents:
            if self.food_counter > 0:
                food_to_digest = self.contents.pop()
                self.counter -= food_to_digest.counter_modifier
                self.poop_level -= food_to_digest.poop_modifier





