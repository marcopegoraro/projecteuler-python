# Intuition: we do not need to compute the entire sequence for all numbers. In any specific sequence, once we hit a
# number for which we have already computed the sequence we can just add that number of steps on the current search.

import time

from utils_number_theory import collatz_n_steps2max

max_collatz_input = 1000000

start = time.process_time()

collatz_steps_list = collatz_n_steps2max(max_collatz_input)

print('Solution: ' + str(collatz_steps_list.index(max(collatz_steps_list)) + 1))
print('\nSolution found in %s seconds.' % (time.process_time() - start))
