class Food:
    def __init__(self, amount, heal):
        self.heal = heal
        self.amount = amount

class AutoEat:
    def __init__(self, tier, food):
        self.tier = tier
        self.food = food

        match self.tier:
            case 1:
                self.efficiency = 60
            case 2:
                self.efficiency = 80
            case 3:
                self.efficiency = 100

    def one_heal(self):
        return self.food.heal * self.efficiency / 100

    def max_heal(self):
        return self.food.amount * self.one_heal()
