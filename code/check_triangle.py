def check_triangle(a,b,c):
    if a+b > c and a+c > b and b+c > a:
        if a==b==c:
            print("Equilateral triangle")
        elif a == b or b ==c or c == a:
            print("Isocelese triangle")
        else:
            print("scalene triangle")
    else:
        print("Triangle is not valid")


a = int(input())
b = int(input())
c = int(input())
check_triangle(a,b,c)