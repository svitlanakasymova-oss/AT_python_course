import pytest
import allure


@allure.title("Trivial test")
def test_trivial_assert():
    assert True