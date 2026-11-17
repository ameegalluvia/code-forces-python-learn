s = list(input())

ref = ["h", "e", "l", "l", "o"]

for i in range(len(s)):
    if s[i] in ref:
        if s[i] == ref[0]:
            ref.remove(ref[0])

if ref == []:
    print("YES")
else:
    print("NO")
