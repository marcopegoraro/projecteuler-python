# Strategy: try out the three digits number descending from 999 to 100. checking if the product is a palindrome.
# To avoid duplication I'll check each number only against the ones smaller than itself

import time

from utils_string import is_palindrome

start = time.process_time()

maxfound = 0
for i in range(999, 99, -1):
    for j in range(i - 1, 99, -1):
        if is_palindrome(str(i*j)):
            if i*j > maxfound:
                maxfound = i*j

print('Solution: ' + str(maxfound))
print('\nSolution found in %s seconds.' % (time.process_time() - start))
