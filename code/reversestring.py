def sol(n,m,input_str):
    ans = ""
    for i in range(n,n+m):
        ans += input_str[i]

    return ans[::-1]



num_list = list(map(int, input().split()))
n, m = num_list[0], num_list[1]
input_str = input()
print(sol(n,m,input_str))







