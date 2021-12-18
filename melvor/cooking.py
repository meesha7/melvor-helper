class CookingBonuses:
    def __init__(
        self, chance_to_preserve, chance_to_double, chance_to_perfect, success_rate
    ):
        self.chance_to_preserve = chance_to_preserve
        self.chance_to_double = chance_to_double
        self.chance_to_perfect = chance_to_perfect
        self.success_rate = success_rate


class Cooking:
    def __init__(self, base_heal, cook_time, output, bonuses):
        self.base_heal = base_heal
        self.cook_time = cook_time
        self.output = output
        self.bonuses = bonuses

    def time_to_use_all_ingredients(self, amount):
        preserve_mod = 1 + self.bonuses.chance_to_preserve / 100

        return amount * self.cook_time * preserve_mod

    def will_produce_normal(self, amount):
        double_mod = 1 + self.bonuses.chance_to_double / 100
        success_mod = self.bonuses.success_rate / 100
        perfect_mod = self.bonuses.chance_to_perfect / 100

        return amount * self.output * double_mod * success_mod * (1 - perfect_mod)

    def will_produce_perfect(self, amount):
        double_mod = 1 + self.bonuses.chance_to_double / 100
        success_mod = self.bonuses.success_rate / 100
        perfect_mod = self.bonuses.chance_to_perfect / 100

        return amount * self.output * double_mod * success_mod * perfect_mod

    def total_heal(self, amount):
        return (
            self.will_produce_normal(amount) * self.base_heal
            + self.will_produce_perfect(amount) * self.base_heal * 1.1
        )
