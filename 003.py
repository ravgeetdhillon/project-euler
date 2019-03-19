import math

def findLargestPrimeFactor(num):
    maxPrime = 0
    i = 2
    while i <= int(math.sqrt(num)) * 2:
        if num%i == 0 and isPrime(i):
            while num%i != 0:
                num //= i
            maxPrime = i
        i += 1
    if maxPrime == 0:
        maxPrime = num

    return maxPrime
        
def isPrime(num):
    if num == 2 or num == 3:
        return True
    else:
        preQuot = num
        for i in range(2,num):
            if num%i == 0:
                return False
            else:
                curQuot = num // i
                if curQuot == preQuot:
                    return True
                preQuot = curQuot

test = int(input())
while test != 0:
    n = int(input())
    print(findLargestPrimeFactor(n))
    test -= 1
