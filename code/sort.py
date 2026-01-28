n = int(input("Enter number of pairs: "))

arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])


arr.sort(lambda x: x[0], -x[1] )