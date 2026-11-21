from pathlib import Path
import json

path = Path('user_info.json')

if path.exists():
    contents = path.read_text()
    user = json.loads(contents)
    print(f"Welcome back, {user['name']}!")
else:
    name = input("What is your name? ")
    age = input("How old are you? ")
    city = input("Which city do you live in? ")

    user = {'name': name, 'age': age, 'city': city}
    contents = json.dumps(user)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {name}!")

print("\nHere's what I remember about you:")
print(f"Name: {user['name']}")
print(f"Age: {user['age']}")
print(f"City: {user['city']}")
