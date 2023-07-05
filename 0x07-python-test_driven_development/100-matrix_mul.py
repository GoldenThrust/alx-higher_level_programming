#!/usr/bin/python3
""" Matrix mulyiplication """


def matrix_mul(m_a, m_b):
    """ Multiply two matrices """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all((isinstance(elem, int) or isinstance(elem, float))
            for elem in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(elem, int) or isinstance(elem, float))
            for elem in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    col = 0
    row = 0
    matrix = []

    for row in m_a:
        i = 0
        row2 = []
        while i < len(m_b[0]):
            res = 0
            j = 0
            for col in row:
                res += col * m_b[j][i]
                j += 1
            row2.append(res)
            i += 1
        matrix.append(row2)

    return matrix
