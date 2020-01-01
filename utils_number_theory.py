from utils_prime import is_even

def sum_first_n(n):
    """
    Returns the sum of the first n natural numbers.
    """

    return n*(n + 1) // 2


def gen_triangs2max(max_n):
    """
    Return triangular numbers up to a maximum.
    """

    if max_n < 1:
        return []

    triangs = [1]

    i = 2
    while triangs[-1] + i <= max_n:
        triangs.append(triangs[-1] + i)
        i += 1

    return triangs


def gen_triangs(n_triangs):
    """
    Returns triangular numbers up to a specific sequence length.
    """

    if not n_triangs:
        return []

    triangs = [1]

    i = 2
    while len(triangs) < n_triangs:
        triangs.append(triangs[-1] + i)
        i += 1

    return triangs


def collatz_steps(n):
    if n == 1:
        return [1]
    if is_even(n):
        return [n] + collatz_steps(n // 2)
    else:
        return [n, 3 * n + 1] + collatz_steps(n // 2)


def collatz_n_steps(n):
    if n == 1:
        return 0
    if is_even(n):
        return 1 + collatz_n_steps(n // 2)
    else:
        return 2 + collatz_n_steps((3 * n + 1) // 2)


def collatz_n_steps2max(n):
    steps_list = [0]
    for i in range(2, n + 1):
        done = False
        acc_steps = 0
        step = i
        while not done:
            if step <= len(steps_list):
                steps_list.append(acc_steps + steps_list[step - 1])
                done = True
            else:
                if is_even(step):
                    acc_steps += 1
                    step = step // 2
                else:
                    acc_steps += 2
                    step = (3 * step + 1) // 2

    return steps_list
