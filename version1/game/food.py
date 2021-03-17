class Food:
    #normal and harmful foods added for now
    def __init__(self, name, food_type):
        self.name = name
        self.type = food_type
        if self.type == 'normal':
            self.TimeToProcess = 3
            self.PoopValue = 5
            self.HealthValue = 0
            self.HarmValue = 0
        elif self.type == 'harmful':
            self.TimeToProcess = 2
            self.PoopValue = 0
            self.HealthValue = 0
            self.HarmValue = -1
        elif self.type == 'helpful':
            self.TimeToProcess = 1
            self.PoopValue = 3
            self.HealthValue = 1
            self.HarmValue = 0
        
        
