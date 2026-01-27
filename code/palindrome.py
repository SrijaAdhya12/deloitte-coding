def check_palindrome(num):
    temp = 0
    number = num
    while number > 0:
        temp = temp*10 + number%10
        number = number//10
    if temp == num:
        return "is palindrome"
    return "not palindrome"








number = int(input())
print(check_palindrome(number))