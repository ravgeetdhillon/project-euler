def gcd(a, b):
    smaller = min(a ,b)
    larger = max(a ,b)
    while smaller != 0:
        rem = larger%smaller
        larger = smaller
        smaller = rem

    return larger

def conditionSuper(a, b, c):
    area = a * b * c
    if area%6 == 0 and area%28 == 0:
        return True
    return False

test = int(input())

while test != 0:
    n = int(input())
    count = 0
    i = 1
    c = 1
    while c <= n:
        print('----',c)
        for a in range(1, c):
            for b in range(a + 1, c):
                print(a,b,c)
                print(a**2,b**2,c**2,'--')
                if a ** 2 + b ** 2 == c ** 2:
                    if gcd(a, b) == 1 and gcd(b, c) == 1 and conditionSuper == False:
                        count += 1
        i += 1
        c = (c + 1) ** 2

    print(count)
    
    test -= 1
