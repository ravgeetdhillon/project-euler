def isPalindrome(num):
    rev = 0
    a = num
    while a != 0:
        rev = rev * 10 + a%10
        a //= 10
    if num == rev:
        return True
    return False

def largestPalindrome(num):
    ans = 0
    for p in range(110, 991, 11):
        for q in range(100000//p + 1, 1000, 1):
            product = p * q
            if product >= num:
                break
            elif isPalindrome(product):
                if product > ans:
                    ans = product
    return ans

test = int(input())
while test != 0:
    n = int(input())
    print(largestPalindrome(n))
    test -= 1
