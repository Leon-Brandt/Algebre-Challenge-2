"""Brandt Leon, Claerhout Julien

LINFO1112-Algèbre: Challenge 2
Gaussian Elimination
"""

def gauss_jordan(A):
    """
Should return the Gauss-Jordan Eliminated matrix

    :param A: Matrix of n*m size, n>1, m>1
    :return: Reduced matrix, same size
    """
    num_lines = len(A)
    num_colons = len(A[0])

    if num_colons > num_lines: #------------ Raising Error if Matrix is unsolvable
        raise Exception('Dimension mismatch')
"""
    ref_line = A[0]
    if ref_line[0] == 0:
        raise Exception('A[0][0] = 0')

    for i in range(1, num_lines):
        if A[i][0] != 0:
        """