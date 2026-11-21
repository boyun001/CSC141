try:
    first_number = int(input("First number: "))
    second_number = int(input("Second number: "))
except ValueError:
    print("Sorry, please enter numbers only.")
else:
    print(f"The sum is {first_number + second_number}.")