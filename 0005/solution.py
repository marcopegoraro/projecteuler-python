# This is faster to do with a calculator than to code, but I will leave both solutions

import time

from utils_prime import lcm_list

start = time.process_time()

# print('Solution: ' + str(lcm_list(range(2, 21))))
print('Solution: ' + str(2**4*3**2*5*7*11*13*17*19))
print('\nSolution found in %s seconds.' % (time.process_time() - start))
