n = int(input())

kamar = 0

for i in range(n):
    p, q = map(int, input().split())
    if q - p >= 2:
        kamar += 1

print(kamar)
