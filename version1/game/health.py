class Health:
    max_hp = 5

    def __init__(self):
        self.current_hp = self.max_hp

    def max_hp_check(self):
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp

    def add_hp(self, amount_to_add):
        self.current_hp += amount_to_add
        self.max_hp_check()

    def lose_hp(self, amount_to_lose):
        self.current_hp -= amount_to_lose
        self.max_hp_check()

    def is_not_dead(self):
        return self.current_hp > 0

    def __repr__(self):
        return f'HP:{self.current_hp}'
