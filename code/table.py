def print_table(num):
    for i in range(1,11):
        ans = num*i
        print(f"{num} * {i} = {ans}")


num = int(input())
print_table(num)