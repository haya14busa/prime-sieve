#!/usr/bin/env python
# -*- coding:utf-8 -*-
''' Enumerate prime numbers upto 10000 '''

import time


def sqrt(num):
    sq = num ** .5
    return sq

def main():
    maxn = 10000
    prime_set = set(xrange(2,maxn+1))
    temp_set = set()
    possible_set = set(xrange(2,int(sqrt(maxn+1))))
    while 1:
        try:
            prime = possible_set.pop()
            temp_set.add(prime)
        except:
            prime_set = sorted(prime_set | temp_set)
            print prime_set
            print len(prime_set)
            return
        prime_set = set(ifilter(lambda x: x % prime, prime_set))
        possible_set = set(ifilter(lambda x: x % prime, possible_set))


if __name__ == '__main__':
    time1 = time.clock()
    from itertools import ifilter
    main()
    time2 = time.clock()
    time = time2 - time1
    print time
