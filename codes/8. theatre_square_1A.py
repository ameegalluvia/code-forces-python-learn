n, m, a = map(int, input().split())

sisi_n = (n + a - 1) // a #pembulatan ke atas dari n/a
sisi_m = (m + a - 1) // a #pembulatan ke atas dari m/a

jumlah_batu = sisi_m * sisi_n

print(jumlah_batu)
