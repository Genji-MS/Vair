class Poops:
    def __init__(self, amount=5):
        #start the game with 5 poops, unless otherwise specified
        self.amount = amount
    
    def get_poops(self):
        return self.amount

    def poopsAvailable(self):
        return self.amount > 0
    
    def addPoops(self, amount):
        self.amount += amount
    
    def decrement_poop(self, x, y):
        self.amount -= 1