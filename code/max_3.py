def max_num(num_list):
    num1 = num_list[0]
    num2 = num_list[1]
    num3 = num_list[2]
    if num1 > num2 and num1 > num2:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

num_list = list(map(int, input().split()))
print(max_num(num_list))