x = int(input())

total = 0

langkah = x // 5
sisa = x % 5
total += langkah

for i in reversed(range(1, 5)):
    langkah = sisa // i
    sisa = sisa % i
    total += langkah


print(total)
