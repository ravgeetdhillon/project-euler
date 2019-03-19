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
`                    return True
                preQuot = curQuot

variables = [int(i) for i in input().split()]

a = variables[0]
b = variables[1]
c = variables[2]

test = int(input())

listPrimes = []
listPrimesIndex = []

pre_max_n = 0

while test != 0:
    
    n = int(input())
    
    if n <= pre_max_n:
        count = 0
        for ind in listPrimesIndex:
            if ind <= n:
                count += 1
            else:
                print(count)
                break
            
    elif n > pre_max_n:
        for i in range(pre_max_n + 1, n + 1):
            p = (a * (i ** 2)) + (b * i) + c
            if isPrime(p):
                listPrimes.append(p)
                listPrimesIndex.append(i)
        print(len(listPrimesIndex))
        pre_max_n = n
        
    test -= 1
