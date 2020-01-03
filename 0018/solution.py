# Intuition: the path goes from top to bottom of the number triangle and has to yield a maximum sum. The solution is to
# swap every number n for n + max(adjacent numbers on the level above). This has to be done top to bottom.
# Then, the solution is simply the maximum value on the bottom row.

import time

triangle = []

with open('input') as f:
    for line in f:
        triangle.append([int(n) for n in line.split()])

start = time.process_time()

for i in range(1, len(triangle)):
    for j in range(len(triangle[i])):
        if j == 0:
            triangle[i][j] += triangle[i - 1][j]
        elif j == len(triangle[i]) - 1:
            triangle[i][j] += triangle[i - 1][j - 1]
        else:
            triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])

print('Solution: ' + str(max(triangle[-1])))
print('\nSolution found in %s seconds.' % (time.process_time() - start))
