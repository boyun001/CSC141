from pathlib import Path

path = Path('guest.txt')

your_name = input("What is your name? ")
path.write_text(your_name)