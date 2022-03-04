class Bonuses:
    def __init__(self, chance_to_preserve, chance_to_double):
        self.chance_to_preserve = chance_to_preserve
        self.chance_to_double = chance_to_double


class Crafting:
    def __init__(self, recipe, action_time, bonuses, output=1, price=0):
        self.recipe = recipe
        self.action_time = action_time
        self.bonuses = bonuses
        self.output = output
        self.price = price

    def time_to_use_all(self, amount):
        preserve_mod = 1 + self.bonuses.chance_to_preserve / 100

        return (amount / self.recipe) * self.action_time * preserve_mod

    def will_produce(self, amount):
        double_mod = 1 + self.bonuses.chance_to_double / 100
        preserve_mod = 1 + self.bonuses.chance_to_preserve / 100

        return (amount / self.recipe) * self.output * preserve_mod * double_mod

    def total_price(self, amount):
        return self.will_produce(amount) * self.price
