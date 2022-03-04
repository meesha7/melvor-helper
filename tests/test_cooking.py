import pytest

from melvor.cooking import Cooking, CookingBonuses


def test_time_to_use_all_ingredients():
    bonuses = CookingBonuses(
        chance_to_preserve=0,
        chance_to_double=0,
        chance_to_perfect=0,
        success_rate=100,
    )

    cooking = Cooking(base_heal=100, cook_time=10, recipe=1, output=1, bonuses=bonuses)

    assert pytest.approx(cooking.time_to_use_all_ingredients(10)) == 100

    bonuses.chance_to_preserve = 10
    assert pytest.approx(cooking.time_to_use_all_ingredients(10)) == 110


def test_will_produce():
    bonuses = CookingBonuses(
        chance_to_preserve=0,
        chance_to_double=0,
        chance_to_perfect=0,
        success_rate=100,
    )

    cooking = Cooking(base_heal=100, cook_time=10, recipe=1, output=1, bonuses=bonuses)

    assert cooking.will_produce_normal(10) == 10

    bonuses.chance_to_perfect = 50

    assert pytest.approx(cooking.will_produce_normal(10)) == 5
    assert pytest.approx(cooking.will_produce_perfect(10)) == 5


def test_total_heal():
    bonuses = CookingBonuses(
        chance_to_preserve=0,
        chance_to_double=0,
        chance_to_perfect=0,
        success_rate=100,
    )

    cooking = Cooking(base_heal=100, cook_time=10, recipe=1, output=1, bonuses=bonuses)

    assert pytest.approx(cooking.total_heal(10)) == 1000

    bonuses.chance_to_perfect = 50
    assert pytest.approx(cooking.total_heal(10)) == 1050

    bonuses.chance_to_double = 10
    assert pytest.approx(cooking.total_heal(10)) == 1155
