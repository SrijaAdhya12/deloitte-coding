def find_max(my_list):
    max_num = 0
    for i in my_list:
        if i > max_num:
            max_num = i
    return max_num


my_list = list(map(int, input().split()))
print(find_max(my_list))