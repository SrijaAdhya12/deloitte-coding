def check_age(age):
    if age >= 18:
        return "Eligible"
    return "Not eligible"







age = int(input())
print(check_age(age))