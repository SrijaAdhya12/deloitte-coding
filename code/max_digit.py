def max_digit(num):
    digit = 0
    while num > 10:
        n = num % 10
        if n > digit:
            digit = n
        num //=10
    return digit


number = int(input())
print(max_digit(number))