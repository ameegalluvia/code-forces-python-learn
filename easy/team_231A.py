n = int(input())

jawab = 0

for i in range(n):
    p, v, t = map(int, input().split())
    if p + v + t >= 2:
        jawab += 1

print(jawab)