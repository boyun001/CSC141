from pathlib import Path


def count_the(filename):
    """Count how many times 'the' appears in a text file."""
    path = Path(__file__).parent / filename
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        text = contents.lower()
        print(f"\n{filename}:")
        print(f"  'the'  appears {text.count('the')} times.")
        print(f"  'the ' appears {text.count('the ')} times.")


filenames = ['text_1.txt', 'text_2.txt', 'text_3.txt']
for filename in filenames:
    count_the(filename)