import numpy as np
from scipy.sparse import csr_matrix

data = np.array([2, 4, 3, 5, -4, -7, -5, -8, 6, 8, 2, 9, 4, 9, -2, 14])
indices = np.array([0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3])
indptr = np.array([0, 4, 8, 12, 16])

L = np.matrix('1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 0 1')
sK = 0
matrix = csr_matrix((data, indices, indptr), shape=(4, 4)).toarray()
print("matrix:\n", matrix)
length = len(matrix) - 1
swing = 1

for i in range(len(matrix)):
    while sK <= len(matrix) - 1:
        column = 0
        if swing > length:
            sK += 1
            length -= 1
            swing = 1
            continue
        if matrix[sK][sK] != 0:
            if matrix[sK + swing, sK] - matrix[sK + swing, sK] / matrix[sK, sK] * matrix[sK, sK] == 0:
                l = matrix[sK + swing, sK] / matrix[sK, sK]
                L[sK + swing, sK] = l
                while column <= len(matrix) - 1:
                    matrix[sK + swing, column] = matrix[sK + swing, column] - l * matrix[sK, column]
                    column += 1
        swing += 1
print("U:\n", matrix)
print("L:\n", L)