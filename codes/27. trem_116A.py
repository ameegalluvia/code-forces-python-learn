n = int(input())

total = 0

cari = []

for i in range(n):
    k, m = map(int, input().split())

    total = total - k + m

    cari.append(total)


maks = cari[0]
for i in range(n):
    if cari[i] > maks:
        maks = cari[i]

print(maks)
