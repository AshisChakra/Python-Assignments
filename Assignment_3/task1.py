number = input("Enter a number: ")

def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

factorial_result = factorial(int(number))
print(f"The factorial of {number} is: {factorial_result}")