#!/usr/bin/env python
# -*- coding:utf-8 -*-
''' Enumerate prime numbers upto 10000 '''

import time
import sys

argvs = sys.argv
if len(argvs) < 2:
    MAX = 10000
else:
    try:
        MAX = int(argvs[1])
    except:
        MAX = 10000

def sqrt(num):
    sq = num ** .5
    return sq

def main():
    prime_set = set(xrange(2,MAX+1))
    possible_set = set(xrange(2,int(sqrt(MAX+1))))
    temp_set = set() # append prime upto sqrt(MAX)
    while 1:
        try:
            prime = sorted(possible_set).pop(0)
            temp_set.add(prime)
        except:
            prime_set = sorted(prime_set | temp_set)
            print 'List: ', prime_set
            print 'Count: ', len(prime_set)
            return
        prime_set = set(ifilter(lambda x: x % prime, prime_set))
        possible_set = set(ifilter(lambda x: x % prime, possible_set))


if __name__ == '__main__':
    starttime = time.clock()
    from itertools import ifilter
    main()
    endtime = time.clock()
    time = endtime - starttime
    print 'Time: ', time
