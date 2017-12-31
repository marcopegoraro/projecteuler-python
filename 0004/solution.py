# First strategy: try out the three digits number descending from 999 to 100. checking if the product is a palindrome.
# To avoid duplication I'll check each number only against the ones smaller than itself

import time

start = time.time()

maxfound = 0
for i in range(999, 99, -1):
    for j in range(i-1, 99, -1):
        if str(i*j) == str(i*j)[::-1]:
            if i*j > maxfound:
                maxfound = i*j

print('\n' + str(maxfound))

print('\nSolution found in %s seconds.' % (time.time() - start))
