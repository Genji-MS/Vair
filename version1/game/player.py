from .food import Food


class Player:
    def __init__(self):
        self.pos = (15, 5)
        self.value = '\u001b[31mX'

    def eat(self, food):
        pass

    def can_eat(self):
        return True

    def has_poops(self):
        return True

    def poop(self):
        return Food('poop', 'poop')

    def update_position(self, pos):
        self.pos = (self.pos[0] + pos[0], self.pos[1] + pos[1])
