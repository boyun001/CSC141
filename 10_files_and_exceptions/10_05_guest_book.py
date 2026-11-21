from pathlib import Path

path = Path('guest.txt')
contents = ''
while True:
    your_name = input("What is your name? ")
    if your_name == 'quit':
        break
    contents += your_name + "\n"
# At the end, write the contents to the file
path.write_text(contents)