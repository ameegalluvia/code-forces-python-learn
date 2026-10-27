n = list(map(int, input()))

streak = 0

for i in range(len(n) - 1):
    if n[i] == n[i + 1]:
        streak += 1
    else:
        streak = 0

    if streak >= 6:
        print("YES")
        break

if streak < 6:
    print("NO")
