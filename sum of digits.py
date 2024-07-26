def sum_of_digits(number):
    total = 0
    for digit in str(number):
        total += int(digit)
    return total

number = 12345
print(sum_of_digits(number))  # Output: 15
