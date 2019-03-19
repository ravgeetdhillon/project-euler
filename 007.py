def nPlacePrime(num):
    count = 0
    i = 2
    while count != num:
        if isPrime(i) == True:
            count += 1
            prime = i
        i += 1
    return prime
        
def isPrime(num):
    for i in range(2, num//2+1):
        if num%i == 0:
            return False
    return True

test = int(input())
while test != 0:
    n = int(input())
    print(nPlacePrime(n))
    test -= 1
