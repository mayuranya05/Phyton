columns = int(input('How many colume? '))

for h in range(1, 101, columns):
    for c in range(columns):
        num = h + c
        if num <= 100:
         print (h + c, end=' ')
    print()