import time


triplet_sum = 1000
prod = 0

start = time.process_time()

found = False

for i in range(2, triplet_sum):
    for j in range(i + 1, triplet_sum - i):
        k = triplet_sum - i - j
        if i ** 2 + j ** 2 == k ** 2 and i + j + k == triplet_sum:
            found = True
            prod = i * j * k
            break
    if found:
        break

print('Solution: ' + str(prod))
print('\nSolution found in %s seconds.' % (time.process_time() - start))
