from city_functions import get_city_country


def test_city_country():
    """Does a city and country format correctly?"""
    result = get_city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'