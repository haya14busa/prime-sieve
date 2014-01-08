# http://d.hatena.ne.jp/itchyny/20121027/1351299600


def prime(n):
    x = 1
    k = 1
    primelist = [2]
    while k < n:
        x += 2
        a = 0
        for m in primelist:
            b = x
            while m < b:
                b -= m
            if b == m:
                a = 1
        if a == 0:
            primelist.append(x)
            k += 1
    return primelist

print(prime(100))
