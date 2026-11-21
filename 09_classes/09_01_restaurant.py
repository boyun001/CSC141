# This is tough
class Restaurant:
    """ Model a restaurant with OOP """
    def __init__(self, restaurant_name, cuisine_type, location, price_range, Michelin_rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.location = location
        self.price_range = price_range

    def describe_restaurant(self):
        print(f'The restaurant name is {self.restaurant_name}.')
        print(f'The price is {self.price_range}.')

    def can_you_take_a_date(self):
        if self.price_range > 50:
            print(f"Don't embarrass yourself. It's too expensive!")
        else:
            print(f'You can afford {self.restaurant_name}.')
    
    def michelin_rating(self):
        if self.Michelin_rating >= 3:
            print(f'{self.restaurant_name} is a great Michelin star restaurant!')
        else:
            print(f'{self.restaurant_name} is not a Michelin star restaurant.')

ev_restaurant = Restaurant('Cici Shack', 'Soul Food', 'Philadelphia', 70, 3)
ev_restaurant.can_you_take_a_date()
ev_restaurant.michelin_rating()