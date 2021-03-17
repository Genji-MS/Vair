class Food:
    # normal and harmful foods added for now
    def __init__(self, name, food_type):
        self.name = name
        self.type = food_type
        if self.type == 'normal':
            self.value = '\u001b[35m('
            self.TimeToProcess = 3
            self.PoopValue = 5
            self.HealthValue = 0
            self.HarmValue = 0
        elif self.type == 'harmful':
            self.value = '\u001b[31m('
            self.TimeToProcess = 2
            self.PoopValue = 0
            self.HealthValue = 0
            self.HarmValue = 1
        elif self.type == 'helpful':
            self.value = '\u001b[33m('
            self.TimeToProcess = 1
            self.PoopValue = 3
            self.HealthValue = 1
            self.HarmValue = 0
        elif self.type == 'poop':
            self.TimeToProcess = 2
            self.PoopValue = 0
            self.HealthValue = 0
            self.HarmValue = 0
        
    def __repr__(self):
        return f'{self.name}:{self.type}'
