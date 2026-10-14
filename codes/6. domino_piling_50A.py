luas_domino = 2

panjang_papan, lebar_papan = map(int, input().split())

luas_papan = panjang_papan * lebar_papan

maks_domino = luas_papan//luas_domino

print(maks_domino)