def get_pairs(my_list):
    my_dict = {}
    count = 0
    for i in my_list:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1

    for v in my_dict.values():
        count += v // 2

    return count if count > 0 else "No pair found"

    

my_list = [6,1,6,5,1,2,8,2,9,4]
my_list1 = [13]
print(get_pairs(my_list))
print(get_pairs(my_list1))