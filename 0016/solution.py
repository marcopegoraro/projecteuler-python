import time


input_number = 2 ** 1000

start = time.process_time()

print('Solution: ' + str(sum([int(digit) for digit in list(str(input_number))])))
print('\nSolution found in %s seconds.' % (time.process_time() - start))
