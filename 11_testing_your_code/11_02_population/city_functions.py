def get_city_country(city, country, population=''):
    """Return 'Santiago, Chile', with the population if one is given."""
    city_country = f"{city.title()}, {country.title()}"
    if population:
        return f"{city_country} - population {population}"
    return city_country