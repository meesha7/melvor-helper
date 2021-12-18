from unittest import TestCase

from melvor.cooking import Cooking, CookingBonuses


class TestCooking(TestCase):
    def test_time_to_use_all_ingredients(self):
        bonuses = CookingBonuses(
            chance_to_preserve=0,
            chance_to_double=0,
            chance_to_perfect=0,
            success_rate=100,
        )

        cooking = Cooking(base_heal=100, cook_time=10, output=1, bonuses=bonuses)

        self.assertAlmostEqual(cooking.time_to_use_all_ingredients(10), 100)

        bonuses.chance_to_preserve = 10
        self.assertAlmostEqual(cooking.time_to_use_all_ingredients(10), 110)

    def test_will_produce(self):
        bonuses = CookingBonuses(
            chance_to_preserve=0,
            chance_to_double=0,
            chance_to_perfect=0,
            success_rate=100,
        )

        cooking = Cooking(base_heal=100, cook_time=10, output=1, bonuses=bonuses)

        self.assertAlmostEqual(cooking.will_produce_normal(10), 10)

        bonuses.chance_to_perfect = 50

        self.assertAlmostEqual(cooking.will_produce_normal(10), 5)
        self.assertAlmostEqual(cooking.will_produce_perfect(10), 5)

    def test_total_heal(self):
        bonuses = CookingBonuses(
            chance_to_preserve=0,
            chance_to_double=0,
            chance_to_perfect=0,
            success_rate=100,
        )

        cooking = Cooking(base_heal=100, cook_time=10, output=1, bonuses=bonuses)

        self.assertAlmostEqual(cooking.total_heal(10), 1000)

        bonuses.chance_to_perfect = 50

        self.assertAlmostEqual(cooking.total_heal(10), 1050)

        bonuses.chance_to_double = 10

        self.assertAlmostEqual(cooking.total_heal(10), 1155)
