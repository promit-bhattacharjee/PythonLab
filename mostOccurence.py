number = input()
digit_count = [0] * 10
for digit in number:
    digit_count[int(digit)] += 1

max_digit = max(range(10), key=digit_count.__getitem__)
print(f"The digit that occurs the most is: {max_digit}")
