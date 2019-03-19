def smallestMultiple(num):
    val = num
    while True:
        for i in range(2,num+1):
            if val%i == 0:
                continue
            else:
                val += num
                break
        else:
            return val

test = int(input())
while test != 0:
    n = int(input())
    print(smallestMultiple(n))
    test -= 1
