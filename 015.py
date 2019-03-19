def totalRoutes(n, m):
    a = max(n, m)
    b = min(n, m)
    top = 1
    for i in range(n+m, a, -1):
        top *= i
    bottom = fac(b)
    return (top // bottom) % ((10**9) + 7)

def fac(num):
    ans = 1
    for i in range(num, 1, -1):
        ans *= i
    return ans

test = int(input())
while test != 0:
    variables = [int(i) for i in input().split()]
    n = variables[0]
    m = variables[1]
    print(totalRoutes(n ,m))
    test -= 1
