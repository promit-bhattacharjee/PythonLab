def factorial(n):
    if n < 0:
        return "Invalid input. Please enter a non-negative integer."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

number = int(input("Enter a non-negative integer: "))

result = factorial(number)
last_four_digits = result % 10000
print(f"The last four digits of the factorial are: {last_four_digits}")

