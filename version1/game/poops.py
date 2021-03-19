class Poops:
    def __init__(self, amount=5):
        # start the game with 5 poops, unless otherwise specified
        self.amount = amount

    def get_poops(self):
        return self.amount

    def poopsAvailable(self):
        return self.amount > 0

    def addPoops(self, amount):
        self.amount += amount

    def make_poop(self):
        self.amount -= 1

    def __repr__(self):
        return f'Poops:{self.amount}'
