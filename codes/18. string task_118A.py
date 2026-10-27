s = input().lower()

hasil = (
    s.replace("a", "")
    .replace("o", "")
    .replace("y", "")
    .replace("e", "")
    .replace("u", "")
    .replace("i", "")
)

yow = list(hasil)

for i in yow:
    print(f".{i}", end="")
