def check_representation(my_list):
    ans = []
    for num in my_list:
        temp = num
        for d in [2, 3, 5]:
            while temp % d == 0:
                temp //= d
        if temp == 1:
            ans.append(num)
    return ans


n = int(input())
my_list = list(map(int, input().split()))
print(*check_representation(my_list))
