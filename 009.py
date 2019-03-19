def isTriplet(a, b, c):
    lhs = (a ** 2) + (b ** 2)
    rhs = (c ** 2)
    if lhs == rhs:
        return True

def specialTriplet(num):
    ans = -1
    for i in range(1, num):
        for j in range(i + 1, num):
            k = num - i - j
            if k <= j:
                break
            if isTriplet(i, j, k) == True:
                ans = i * j * k
    return ans

test = int(input())
while test != 0:
    n = int(input())
    print(specialTriplet(n))
    test -= 1
