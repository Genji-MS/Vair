class Food:
    #normal and harmful foods added for now
    def __init__(self, type):
        self.type = type
        if self.type == 'normal':
            self.TimeToProcess = 4
            self.PoopValue = 5
            self.HealthValue = 1
            self.HarmValue = 0
        elif self.type == 'harmful':
            self.TimeToProcess = 4
            self.PoopValue = 2
            self.HealthValue = 0
            self.HarmValue = -1
        
        
