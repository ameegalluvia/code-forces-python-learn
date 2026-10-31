n = int(input())

n += 1

print(n)

for i in range(3):
    y = list(str(n))
    if y[i] == y[i + 1]:
        for i in range(4):
            y[i] += 1
    elif (
        y[0] != y[1]
        and y[0] != y[2]
        and y[0] != y[3]
        and y[1] != y[2]
        and y[1] != y[3]
        and y[2] != y[3]
    ):
        print(y)
        break
