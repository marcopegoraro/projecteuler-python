import time


start = time.process_time()

total = 0

for i in range(0, 1000):
    if i % 3 == 0 or i % 5 == 0:
        total += i

print('Solution: ' + str(total))
print('\nSolution found in %s seconds.' % (time.process_time() - start))
