n = int(input())

x = 0

for i in range(n):
    bit = str(input()).upper()
    if bit == "X++" or bit == "++X":
        x += 1
    else:
        x -= 1

print(x)
