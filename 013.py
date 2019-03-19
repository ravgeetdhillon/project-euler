n = int(input())
s = 0
while n != 0:
    num = int(input())
    s += num
    n -= 1
    
while s > 9999999999:
    s //= 10
    
print(s)
