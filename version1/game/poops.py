class Poops:
    def __init__(self, amount=0):
        self.amount = amount
    
    def poopsAvailable(self):
        return self.amount > 0
    
    def addPoops(self, amount):
        self.amount += amount