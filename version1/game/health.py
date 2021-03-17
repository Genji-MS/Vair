class Health:
    starting_hp = 5

    def __init__(self, current_hp):
        self.current_hp = starting_hp

    def max_hp_check(self):
        if self.amount > starting_hp:
            self.amount = starting_hp

    def add_hp(self, amount_to_add):
        self.current_hp += amount_to_add
        self.max_hp_check()

    def lose_hp(self, amount_to_lose):
        self.current_hp -= amount_to_lose
        self.max_hp_check()

    def is_not_dead(self):
        return self.current_hp > 0
