def find_product(my_list):
    ans = 1
    for i in my_list:
        ans *= i

    return ans


num = int(input())
my_list = list(map(int , input().split()))
print(find_product(my_list))