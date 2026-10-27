def HitungJarak(v, t):
    s = v * t
    return s


def main():
    v, t = map(int, input().split())
    print(HitungJarak(v, t))


main()
