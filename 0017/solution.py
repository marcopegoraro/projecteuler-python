import time


start = time.process_time()

n_list = [''] * 1000
hun = 'hundred'
a = 'and'

n_list[0] = 'one'
n_list[1] = 'two'
n_list[2] = 'three'
n_list[3] = 'four'
n_list[4] = 'five'
n_list[5] = 'six'
n_list[6] = 'seven'
n_list[7] = 'eight'
n_list[8] = 'nine'
n_list[9] = 'ten'
n_list[10] = 'eleven'
n_list[11] = 'twelve'
n_list[12] = 'thirteen'
n_list[13] = 'fourteen'
n_list[14] = 'fifteen'
n_list[15] = 'sixteen'
n_list[16] = 'seventeen'
n_list[17] = 'eighteen'
n_list[18] = 'nineteen'

n_list[19] = 'twenty'
n_list[29] = 'thirty'
n_list[39] = 'forty'
n_list[49] = 'fifty'
n_list[59] = 'sixty'
n_list[69] = 'seventy'
n_list[79] = 'eighty'
n_list[89] = 'ninety'

for i in range(8):
    tens_index = 19 + i * 10
    for j in range(9):
        n_list[tens_index + j + 1] = n_list[tens_index] + n_list[j]

for i in range(9):
    hundreds_index = 99 + i * 100
    n_list[hundreds_index] = n_list[i] + hun
    for j in range(99):
        n_list[hundreds_index + j + 1] = n_list[hundreds_index] + a + n_list[j]

n_list[999] = 'onethousand'

print('Solution: ' + str(sum([len(n) for n in n_list])))
print('\nSolution found in %s seconds.' % (time.process_time() - start))
