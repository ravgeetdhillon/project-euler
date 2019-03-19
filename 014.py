num = int(input())
linum = ['']
skip = []
max = 0
for i in range(1, num+1):
    if i not in skip:
        save = i
        count = 0
        while i != 1:
            if i%2 == 0:
                i //= 2
            else:
                i = i*3 + 1

            if i > save:
                count += 1
                skip.append(i)
            elif i < save:
                c = linum[i]
                count += c + 1
                break
        linum.append(count)
        print(save)
        print(linum)
        print(skip)
        if count > max:
            max = count
print(max)
