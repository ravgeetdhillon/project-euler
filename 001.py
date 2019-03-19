def sumMultiples(limit):
    li = [3, 5, 15]
    totalSum = 0
    for num in li:
        if limit%num == 0:
            n = limit // num - 1
        else:
            n = limit // num
        currSum = (n * ((2 * num) + (n - 1) * num))//2
        if num == 15:
            totalSum -= int(currSum)
        else:
            totalSum += int(currSum)
    return totalSum

test = int(input())
while test != 0:
    limit = int(input())
    print(sumMultiples(limit))
    test -= 1
