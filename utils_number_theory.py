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
