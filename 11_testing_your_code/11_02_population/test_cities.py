from city_functions import get_city_country


def test_city_country():
    """Does a city and country format correctly?"""
    result = get_city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'


def test_city_country_population():
    """Does a city, country, and population format correctly?"""
    result = get_city_country('santiago', 'chile', population=5000000)
    assert result == 'Santiago, Chile - population 5000000'