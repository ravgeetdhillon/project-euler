def sumDigits(num):
    s = 0
    while num != 0:
        s += num%10
        num //= 10
    return s

test = int(input())
while test != 0:
    n = int(input())
    n = 2**n
    print(sumDigits(n))
    test -= 1
