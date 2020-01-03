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
# because it is also the central binomial coefficient, which has a simple, exact non-recurrent formulation
# (although it need the factorial).
# Just for this time, since the numbers are very small, I will use math.factorial.

import time
from math import factorial

from utils_number_theory import pascals_triangle

grid_x = 20
grid_y = 20

start = time.process_time()

# print('Solution: ' + str(pascals_triangle(grid_x + 1, grid_y + 1)[grid_x][grid_y]))
print('Solution: ' + str(factorial(2*grid_x) // factorial(grid_x) ** 2))
print('\nSolution found in %s seconds.' % (time.process_time() - start))
