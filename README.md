# Enumerating Primes

## Description
- This Python script enumerating primes upto 10000 or command line arguments you type.
- Display the number of prime within MAX numbers too.

## Algorism
- [Sieve of Eratosthenes - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)

## How to make program fast
- This script uses iterator & set to make program faster.
 - set is faster than list.

## How to use

`python prime_stive.py [argument]`

- Default MAX number is 10000.

## Attention
- Set is unsorted even if make regular order.
- So, we needs to sorted(set) and pop out first element.
 - If you wouldn't sort set, this script became buggy when MAX num is over about 15000.
- This script fixed this bug(?) so you can rely on result.
