def maximum_product(my_list):
    max_prod = min_prod = res = my_list[0]
    for i in range(1, len(my_list)):
        num = my_list[i]
        temp_max = max(num, max_prod*num, min_prod*num)
        min_prod = min(num, max_prod*num, min_prod*num)
        max_prod = temp_max

        res = max(res, max_prod)
    return res






my_list = list(map(int, input().split()))
print(maximum_product(my_list))
