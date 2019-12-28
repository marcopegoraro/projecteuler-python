import time

from utils_prime import get_primes2max

limit = 2000000

start = time.process_time()

print('Solution: ' + str(sum(get_primes2max(limit))))
print('\nSolution found in %s seconds.' % (time.process_time() - start))
