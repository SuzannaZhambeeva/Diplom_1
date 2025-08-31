import pytest
from unittest.mock import MagicMock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient



def test_set_buns_and_price():
    burger = Burger()
    bun = Bun("test bun", 100)
    burger.set_buns(bun)

    # без ингредиентов
    assert burger.get_price() == 200


def test_add_and_remove_ingredient():
    burger = Burger()
    bun = Bun("bun", 100)
    burger.set_buns(bun)

    ing1 = Ingredient("SAUCE", "ketchup", 50)
    ing2 = Ingredient("FILLING", "cutlet", 150)

    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)

    assert len(burger.ingredients) == 2

    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0].get_name() == "cutlet"


def test_move_ingredient():
    burger = Burger()
    bun = Bun("bun", 100)
    burger.set_buns(bun)

    ing1 = Ingredient("SAUCE", "ketchup", 50)
    ing2 = Ingredient("FILLING", "cutlet", 150)
    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)

    burger.move_ingredient(0, 1)
    assert burger.ingredients[0].get_name() == "cutlet"
    assert burger.ingredients[1].get_name() == "ketchup"


def test_get_receipt_with_mock():
    burger = Burger()

    # мок булки
    bun = MagicMock()
    bun.get_name.return_value = "mock bun"
    bun.get_price.return_value = 100
    burger.set_buns(bun)

    # мок ингредиента
    ing = MagicMock()
    ing.get_name.return_value = "mock ingredient"
    ing.get_price.return_value = 50
    ing.get_type.return_value = "FILLING"

    burger.add_ingredient(ing)

    receipt = burger.get_receipt()

    assert "mock bun" in receipt
    assert "mock ingredient" in receipt
    assert "Price: 250" in receipt
