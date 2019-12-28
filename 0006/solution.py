import time

from utils_number_theory import sum_first_n


start = time.process_time()

sum_of_squares = sum([i ** 2 for i in range(1, 101)])
square_of_sums = sum_first_n(100) ** 2

print('Solution: ' + str(square_of_sums - sum_of_squares))
print('\nSolution found in %s seconds.' % (time.process_time() - start))
