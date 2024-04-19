L = [10, 7, 2, 9, 7, 0, 6, 7, 6, 2, 13, 27, 1, 0, 91, 6, 47]

a = 0
fim = len(L)
while fim > 0:
    for i in range(fim-1):
        if L[i] > L[i+1]:
            a = L[i+1]
            L[i+1] = L[i]
            L[i] = a
    fim -= 1
print(L)
