n, k = map(int, input().split())

lolos = 0

score = list(map(int, input().split()))

score_k = score[k-1]

for a in score:
    if a > 0 and a >= score_k:
        lolos += 1

print(lolos)