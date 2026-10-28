n, h = map(int, input().split())

a = list(map(int, input().split()))

baris = 0

for anak in a:
    if anak > h:
        baris += 2
    else:
        baris += 1

print(baris)
