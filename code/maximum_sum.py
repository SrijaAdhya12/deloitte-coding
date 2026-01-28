def find_maxsum_subarray(my_list):
    current_sum = 0
    max_sum = float("-inf")
    for i in my_list:
        current_sum += i
        max_sum = max(current_sum, max_sum)
        if current_sum < 0:
            current_sum = 0
    return max_sum





my_list = list(map(int, input().split()))
print(find_maxsum_subarray(my_list))
