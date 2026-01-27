def sum_digit(number):
    total = 0
    while number > 0:
        n = number%10
        total += n
        number= number // 10
    return total
    
number = int(input())
print(sum_digit(number))