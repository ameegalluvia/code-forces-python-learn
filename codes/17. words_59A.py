s = list(input())

upper = 0
lower = 0

for huruf in s:
    kode = ord(huruf)
    if kode > 90:
        lower += 1
    else:
        upper += 1

if upper > lower:
    print("".join(s).upper())
else:
    print("".join(s).lower())
