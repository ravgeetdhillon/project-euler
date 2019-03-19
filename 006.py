def sumSquareDiff(num):
    a_part = (num * (num + 1) * ((num * 2) + 1)) // 6
    b_part = ((num * (num + 1)) // 2) ** 2
    ans = b_part - a_part
    return ans

test = int(input())
while test != 0:
    n = int(input())
    print(sumSquareDiff(n))
    test -= 1
