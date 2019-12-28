# If k divides n, then n/k also divides n
# Strategy: iterate over incresing k and search for the first prime n/k

import time

from utils_prime import is_prime


start = time.process_time()

n = 600851475143
k = 3
largest_factor = 1
found = False

while not found:
    if n % k == 0:
        if is_prime(n // k):
            found = True
            largest_factor = n // k
        else:
            n = n // k
    k += 2

print('Solution: ' + str(largest_factor))
print('\nSolution found in %s seconds.' % (time.process_time() - start))
