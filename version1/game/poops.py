class Poops:
    max_poops = 200
    def __init__(self, amount=50):
        # start the game with 5 poops, unless otherwise specified
        self.amount = amount

    def get_poops(self):
        return self.amount
    
    def max_poop_check(self):
        if self.amount > self.max_poops:
            self.amount = self.max_poops

    def poopsAvailable(self):
        return self.amount > 0

    def addPoops(self, amount):
        self.amount += amount
        self.max_poop_check()

    def make_poop(self):
        self.amount -= 1

    
    def get_stats(self):
        return f'{self.amount} / {self.max_poops}'
    
    def get_bar_width(self):
        return self.amount / self.max_poops
        
    def new_game(self):
        self.amount = 50

    def __repr__(self):
        return f'Poops:{self.amount}'
