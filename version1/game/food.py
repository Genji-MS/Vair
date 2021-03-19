class Food:
    # normal and harmful foods added for now
    def __init__(self, name, food_type):
        self.name = name
        self.type = food_type
        if self.type == 'normal':
            # Magenta
            self.value = '\u001b[35mN'
            self.TimeToProcess = 3
            self.PoopValue = 5
            self.HealthValue = 0
            self.HarmValue = 0
        elif self.type == 'harmful':
            # red
            self.value = '\u001b[31mB'
            self.TimeToProcess = 2
            self.PoopValue = 0
            self.HealthValue = 0
            self.HarmValue = 1
        elif self.type == 'helpful':
            # Yellow
            self.value = '\u001b[33mG'
            self.TimeToProcess = 1
            self.PoopValue = 3
            self.HealthValue = 1
            self.HarmValue = 0
        elif self.type == 'poop':
            # Yellow
            self.value = '\u001b[33mP'
            self.TimeToProcess = 2
            self.PoopValue = 0
            self.HealthValue = 0
            self.HarmValue = 0

    def __repr__(self):
        return f'{self.name}:{self.type}'

    @classmethod
    def from_json(cls, f_ob):
        return cls(f_ob['name'], f_ob['type'])
