k, n, w = map(int, input().split())

harga = 0

for i in range(w):
    harga += (i + 1) * k

if harga > n:
    print(harga - n)
else:
    print(0)
