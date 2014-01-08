# http://d.hatena.ne.jp/itchyny/20121027/1351299600


def prime(n):
    candidate = 1  # candidate of prime
    count = 1      # the number of prime
    primelist = [2]
    while count < n:
        candidate += 2
        flag = 0   # 0->prime, 1->not prime
        for prime in primelist:
            remainder = candidate
            while prime < remainder:
                remainder -= prime
            if remainder == prime:
                flag = 1
        if flag == 0:
            primelist.append(candidate)
            count += 1
    return primelist


def main():
    print(prime(100)[-1])

if __name__ == '__main__':
    main()
