
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

    def is_alive(self):
        return self.current_hp > 0
    
    def get_stats(self):
        return f'{self.current_hp} / {self.max_hp}'
    
    def get_bar_update(self):
        bar_percent = self.current_hp / self.max_hp
        color = None
        if bar_percent >= 0.75:
            color = (0, 100, 0)
        elif bar_percent > 0.25:
            color = (128, 128, 0)
        elif bar_percent <= 0.25:
            color = (255, 0, 0)
        return [bar_percent * 50, color]
    
    def new_game(self):
        self.current_hp = self.max_hp

    def __repr__(self):
        return f'HP:{self.current_hp}'
