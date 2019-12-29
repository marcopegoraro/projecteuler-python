from functools import reduce


def search_in_matrix(matrix, length, element_aggregator, pattern_comparator):
    """
    Searches for adjacent elements in a matrix (horizontally, vertically and diagonally) of a certain length.
    Aggregates the elements in a sequence with the function element_aggregator, and returns the best sequence chosen
    through the comparison operator pattern_comparator.
    """

    x_dim = len(matrix[0])
    y_dim = len(matrix)

    max_rows = reduce(pattern_comparator, [reduce(element_aggregator, [matrix[y][x + n] for n in range(length)]) for x in range(0, x_dim - (length - 1)) for y in range(0, y_dim)])
    max_cols = reduce(pattern_comparator, [reduce(element_aggregator, [matrix[y + n][x] for n in range(length)]) for x in range(0, x_dim) for y in range(0, y_dim - (length - 1))])
    max_diags = reduce(pattern_comparator, [reduce(element_aggregator, [matrix[y + n][x + n] for n in range(length)]) for x in range(0, x_dim - (length - 1)) for y in range(0, y_dim - (length - 1))])
    max_inv_diags = reduce(pattern_comparator, [reduce(element_aggregator, [matrix[y - n][x + n] for n in range(length)]) for x in range(0, x_dim - (length - 1)) for y in range(length - 1, y_dim)])

    return reduce(pattern_comparator, [max_rows, max_cols, max_diags, max_inv_diags])
