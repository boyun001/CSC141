import pytest
from employee import Employee


@pytest.fixture
def employee():
    """An employee that is available to all test functions."""
    return Employee('annie', 'kim', 50000)


def test_give_default_raise(employee):
    """Does a default raise of $5,000 work?"""
    employee.give_raise()
    assert employee.annual_salary == 55000


def test_give_custom_raise(employee):
    """Does a custom raise amount work?"""
    employee.give_raise(10000)
    assert employee.annual_salary == 60000
    