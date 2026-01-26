def encrypt(input_str):
    res_list = input_str.split("-")
    ans = ""
    for i in res_list:
        ans += i[-1]
    return ans

input_str = input()
print(encrypt(input_str))