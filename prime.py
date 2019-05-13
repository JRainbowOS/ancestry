# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:03:28 2019

@author: YS15101711
"""

import time
from functools import wraps


def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print('Elapsed time: {}'.format(end - start))
        return result
    return wrapper

def isPrime(n):
    isPrime = True
    for i in range(2, int(n ** (1/2)) + 1):
        if (n % i == 0):
            isPrime = False
    return isPrime

#@timing
def firstNPrimes(n):
    i = 2
    primes = []
    while len(primes) < n:
        if isPrime(i):
            primes.append(i)
        i += 1
    return primes

def createDict(n):
    result = {}
    for i in range(n): 
        result[i] = [i]
    return result

#@timing
#def main():
#    for i in range(20):
#        print(isPrime(i))
#        
#    N = 10000
#    firstN = firstNPrimes(N)
#    print(firstN)
#        
#main()