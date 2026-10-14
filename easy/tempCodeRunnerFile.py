
score = input().split()

for i in range(n):
    if i == k - 1:
        score_k = int(score[i])

if score_k > 0:
    lolos = 1
    for a in score:
        if a >= score_k:
            lolos += 1
else:
    for a in score:
            if a > score_k:
                lolos += 1
print(lolos)