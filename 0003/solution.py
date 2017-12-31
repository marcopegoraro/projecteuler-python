# The number (let's call it n) is not even; the largest possible divisor is thus n/3
# I'll just iterate checking the divisibility for n/k, where k is 3, 5, 7, ... and then check for primality

import time
import math

def is_prime(n):
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

start = time.time()

n = 600851475143
k = 3
found = False

while not found:
    if n % k == 0:
        if n % (n // k) == 0 and is_prime(n // k):
            found = True
            print('\n' + str(n // k))
    k += 2

print('\nSolution found in %s seconds.' % (time.time() - start))
