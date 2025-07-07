number = input("Enter a number: ")

if number.isdigit():
    number = int(number)
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")