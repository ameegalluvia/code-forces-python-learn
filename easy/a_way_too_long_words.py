n = int(input())

kumpulan_kata = []

for i in range(n):
    kumpulan_kata.append(input())

for kata in kumpulan_kata:
    if len(kata) > 10:
        print(kata[0] + str(len(kata) - 2) + kata[-1])
    else:
        print(kata)