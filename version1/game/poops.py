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
    
    def get_bar_update(self):
        bar_percent = self.amount / self.max_poops
        color = None
        if bar_percent >= 0.75:
            color = (0, 100, 0)
        elif bar_percent > 0.25:
            color = (128, 128, 0)
        elif bar_percent <= 0.25:
            color = (255, 0, 0)
        return [bar_percent * 50, color]

    def new_game(self):
        self.amount = 50

    def __repr__(self):
        return f'Poops:{self.amount}'
