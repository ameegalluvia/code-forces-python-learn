a = list(input().lower())
b = list(input().lower())

andi = []
jono = []

for kontoru in a:
    hasan = ord(kontoru)
    andi.append(hasan)


for aziz in b:
    deki = ord(aziz)
    jono.append(deki)


if andi > jono:
    print("1")
elif andi < jono:
    print("-1")
else:
    print("0")
