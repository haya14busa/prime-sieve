#!/usr/bin/env python
# -*- coding:utf-8 -*-
''' Enumerate prime numbers upto 10000 '''

import time



def sqrt(num):
    sq = num ** .5
    return num

def main():
    maxn = 10000
    prime_list = []
    possible_list = range(2,sqrt(maxn))
    while possible_list != []:
        prime = possible_list[0]
        prime_list.append(prime)
        for i in possible_list:
            if i % prime == 0:
                possible_list.remove(i)
    print prime_list
    

if __name__ == '__main__':
    time1 = time.clock()
    main()
    time2 = time.clock()
    time = time2 - time1
    print time
