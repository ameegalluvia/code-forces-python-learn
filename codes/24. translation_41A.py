a = list(input())
b = list(input())

if len(a) == len(b):
    for i in range(len(a)):
        if a[i] != b[-(i + 1)]:
            print("NO")
            exit()
    print("YES")
else:
    print("NO")
