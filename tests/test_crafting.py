import pytest

from melvor.crafting import Crafting, Bonuses


def test_time_to_use_all():
    bonuses = Bonuses(0, 0)
    crafting = Crafting(1, 1, bonuses, output=1, price=10)

    assert crafting.time_to_use_all(10) == 10


def test_time_to_use_all_preserve():
    bonuses = Bonuses(10, 0)
    crafting = Crafting(1, 1, bonuses, output=1, price=10)

    assert crafting.time_to_use_all(10) == 11


def test_time_to_use_all_double():
    bonuses = Bonuses(0, 10)
    crafting = Crafting(1, 1, bonuses, output=1, price=10)

    assert crafting.time_to_use_all(10) == 10


def test_will_produce():
    bonuses = Bonuses(0, 0)
    crafting = Crafting(1, 1, bonuses, output=1, price=10)

    assert crafting.will_produce(10) == 10
    assert crafting.total_price(10) == 100


def test_will_produce_preserve():
    bonuses = Bonuses(10, 0)
    crafting = Crafting(1, 1, bonuses, output=1, price=10)

    assert crafting.will_produce(10) == 11
    assert crafting.total_price(10) == 110


def test_will_produce_double():
    bonuses = Bonuses(0, 10)
    crafting = Crafting(1, 1, bonuses, output=1, price=10)

    assert crafting.will_produce(10) == 11
    assert crafting.total_price(10) == 110


def test_will_produce_both():
    bonuses = Bonuses(10, 10)
    crafting = Crafting(1, 1, bonuses, output=1, price=10)

    assert pytest.approx(crafting.will_produce(10)) == 12.1
    assert pytest.approx(crafting.total_price(10)) == 121


def test_will_produce_both_recipe_output():
    bonuses = Bonuses(10, 10)
    crafting = Crafting(2, 1, bonuses, output=10, price=10)

    assert pytest.approx(crafting.will_produce(10)) == 60.5
    assert pytest.approx(crafting.total_price(10)) == 605
