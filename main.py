L = [10, 7, 22, 72, 35, 2, 2, 2, 9, 7, 0, 6, 7, 6, 2, 13, 27, 1, 0, 91, 6, 47]

print(len(L))
print(L)

a = 0
while True:
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            a = L[i+1]
            L[i+1] = L[i]
            L[i] = a
        else:
            pass
    else:
        break
        print(L)
