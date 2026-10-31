n = int(input())

k = list(map(int, input().split()))

for a in k:
    if a == 1:
        print("HARD")
        exit()

print("EASY")
