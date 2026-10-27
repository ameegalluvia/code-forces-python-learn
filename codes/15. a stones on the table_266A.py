n = int(input())

s = list(input())

hapus = 0


for i in range(n - 1):
    if s[i] == s[i + 1]:
        hapus += 1

print(hapus)
