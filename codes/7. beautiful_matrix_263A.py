jarak = 0

for i in range(5):
    matriks = list(map(int, input().split()))

    for j in range(len(matriks)):
        if matriks[j] == 1:
            jarak = abs(2 - i) + abs(2 - j)

print(jarak)