def find_second_max(my_list):
    highest = float("-inf")
    second = float("-inf")
    for i in my_list:
        if i > highest:
            second = highest
            highest = i
        elif i > second and i != highest:
            second = i

    return second










my_list = list(map(int, input().split()))
print(find_second_max(my_list))


