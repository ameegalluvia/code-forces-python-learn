n = int(input())

s = list(input())

a = 0
d = 0

for huruf in s:
    if huruf == "A":
        a += 1
    else:
        d += 1

if a > d:
    print("Anton")
elif a < d:
    print("Danik")
else:
    print("Friendship")
