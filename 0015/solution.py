# Intuition 1: In an nxm lattice, if I take a step to the right, the remainder of possible paths I can
# take is equal to the total amount for a (n)x(m-1) lattice. Taking one step down, the possible
# remaining paths are the total paths of the (n-1)x(m) lattice.
# Referring to the paths in an nxn lattice as L(n, m), the intuition allows to write the general formula
# L(n) = L(n, m-1) + L(n-1, m)
# where L(1, m) = L(n, 1) = 1
# Intuition 2: the orientation of a rectangle does not change the number of path going through the corners.
# So L(n, m) = L(m, n)
# Intuition 3: it is also easy to see that the values for L(n, m) appear in the Pascal's triangle
# (L(n, n) is found on the center element of the (2n - 1)th row of the triangle)

import time

from utils_number_theory import pascals_triangle


start = time.process_time()

print('Solution: ' + str(pascals_triangle(21, 21)[20][20]))
print('\nSolution found in %s seconds.' % (time.process_time() - start))
