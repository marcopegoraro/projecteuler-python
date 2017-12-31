# Of course, the challenge is to find the requested sum with as little RAM as possible
# I'll use two variables to generate the Fibonacci sequence, and another to keep the sum

totaleven = 0
first, second = 1, 1
while second <= 4000000:

    # If the third number is even, sum it to the total
    if second % 2 == 0:
        totaleven += second

    # Generate the next couple of Fibonacci numbers
    first, second = second, first + second

print (totaleven)
