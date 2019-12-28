import time

from utils_prime import get_primes

start = time.process_time()

print('Solution: ' + str(get_primes(10001)[-1]))
print('\nSolution found in %s seconds.' % (time.process_time() - start))
