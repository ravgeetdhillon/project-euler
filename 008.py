def productDigits(num):
    product = 1
    while num!= 0:
        product *= num%10
        num //= 10
    return product

test = int(input())
while test != 0:
    parameters = [int(i) for i in input().split()]
    size = parameters[0]
    bar = parameters[1]
    num = int(input())

    max = 0
    i = 0
    while i + bar <= size:
        piece1 = num // 10 ** (size - bar - i)
        piece2 = piece1 // (10 ** bar)
        piece = piece1 - piece2 * (10 ** bar)

        product = productDigits(piece)
        if product > max:
            max = product
        i += 1
    print(max)
    test -= 1
