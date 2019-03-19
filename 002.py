def fibo(n):
    pre = 0
    nxt = 1
    curr = 0
    s = 0
    for i in range(n):
        curr = pre + nxt
        if curr > n:
            return s
        if curr%2 == 0:
            s += curr
        pre = nxt
        nxt = curr

test = int(input())
while test != 0:
    n = int(input())
    print(fibo(n))
    test -= 1
