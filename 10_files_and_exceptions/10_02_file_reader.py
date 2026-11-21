from pathlib import Path

path = Path('10_files_and_exceptions/learning_python.txt')
contents = path.read_text()

print(contents)

print ("Now, read line by line..."  )
lines = contents.splitlines()
for line in lines:
    print(line.replace('Python', 'C++'))
