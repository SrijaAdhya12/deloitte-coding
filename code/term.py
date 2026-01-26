def summation(x,n):
    term = 0
    total = 0
    for _ in range(n):
        term = term * 10 + x
        total += term
    return total





x = int(input())
n = int(input())
print(summation(x,n))