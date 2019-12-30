import time

from utils_prime import get_n_factors


n_divisors = 500

start = time.process_time()

triang = 1

i = 2
while get_n_factors(triang) <= n_divisors:
    triang += i
    i += 1

print('Solution: ' + str(triang))
print('\nSolution found in %s seconds.' % (time.process_time() - start))
