class Food:
    def __init__(self, amount, heal):
        self.heal = heal
        self.amount = amount


class AutoEat:
    def __init__(self, tier, food, player_hp=None):
        self.tier = tier
        self.food = food
        self.player_hp = player_hp

        match self.tier:
            case 1:
                self.efficiency = 60
            case 2:
                self.efficiency = 80
            case 3:
                self.efficiency = 100

    def one_heal(self):
        one_heal_hp = self.food.heal * self.efficiency / 100

        if self.player_hp < one_heal_hp:
            return self.player_hp

        return one_heal_hp

    def max_heal(self):
        return self.food.amount * self.one_heal()
