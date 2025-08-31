import pytest
from praktikum.bun import Bun



@pytest.mark.parametrize("name, price", [
    ("white bun", 100),
    ("black bun", 200),
    ("red bun", 300),
])
def test_bun_getters(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price
