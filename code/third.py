n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

first = second = third = -(10**9)

for num in arr:
    if num > first:
        third = second
        second = first
        first = num
    elif num > second and num != first:
        third = second
        second = num
    elif num > third and num != first and num != second:
        third = num

print("Second highest:", second)
print("Third highest:", third)
