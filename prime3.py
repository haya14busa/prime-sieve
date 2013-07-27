import time
def prime3():
    counter = 0
    primes = [2, 3]

    for n in range(5, 15001, 2):
        isprime = True
        for i in range(1, len(primes)):
            counter += 1
            if primes[i] ** 2 > n:
                break
            counter += 1
            if n % primes[i] == 0:
                isprime = False
                break
        if isprime:
            primes.append(n)

    print primes, len(primes)
    print 'Count : %d' % counter

time1 = time.clock()
prime3()
time2 = time.clock()
time = time2 - time1
print time
