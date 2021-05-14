import numpy as np
from scipy.sparse import csr_matrix


# n = 2
#
# b = np.array([11, 13])
#
# epsilon = 0.01
#
# x = np.array([0, 0])

n = 4

b = np.array([6, 25, -11, 15])

epsilon = 0.01

x = np.array([0, 0, 0, 0])

def init():
    # square_matrix = np.array([[2, 4, 3, 5], [-4, -7, -5, -8], [6, 8, 2, 9], [4, 9, -2, 14]])
    # square_matrix = np.array([[2, 1], [5, 7]])
    square_matrix = np.array([[10, -1, 2, 0], [-1, 11, -1, 3], [2, -1, 10, -1], [0, 3 , -1 , 8 ]])
    matrix = csr_matrix(square_matrix).toarray()
    return matrix

def LU_decomposition(matrix):
    L = np.zeros(shape=(n, n), dtype=np.float_)
    U = np.zeros(shape=(n, n), dtype=np.float_)
    for i in range(n):
        U[0][i] = matrix[0, i]
        L[i][0] = matrix[i][0] / U[0][0]
        for j in range(n):
            sigmaU = 0
            for k in range(i):
                sigmaU += L[i][k] * U[k][j]
            U[i][j] = matrix[i][j] - sigmaU
            if i <= j:
                sigmaL = 0
                for l in range(i):
                    sigmaL += L[j][l] * U[l, i]
                L[j][i] = (matrix[j][i] - sigmaL) / U[i][i]
    return L, U

def inverse_matrix(matrix):
    L, U = LU_decomposition(matrix)
    b = np.zeros(shape=(n, n))
    for i in range(n):
        b[i, i] = 1
    inverse_A = np.zeros(shape=(n, n))
    for i in range(n):
        solve = solving_l_e(L, U, b[i])
        inverse_A[i] = solve
    inverse_A = inverse_A.transpose()
    return inverse_A

def solving_l_e(L, U, b):
    y = np.array([])

    for i in range(n):
        y_i = 0
        for j in range(i):
            y_i += L[i][j] * y[j]
        y_i = (b[i] - y_i)
        y = np.append(y, y_i)
    x = np.zeros(n)
    for i in reversed(range(n)):
        x_i = 0
        for j in reversed(range(n)):
            x_i += U[i][j] * x[j]
        buf = ((y[i] - x_i) / U[i][i])
        x[i] = buf
    return x

def length_point(x):
    length = 0
    for i in x:
        length += i ** 2
    return length

def jacobi(A, b, x, epsilon):
    curr_x = x
    D = np.zeros(shape=(n, n))
    E = np.zeros(shape=(n, n))
    L = np.zeros(shape=(n, n))
    U = np.zeros(shape=(n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                D[i][j] = A[i][j]
                E[i][j] = 1
            elif i > j:
                L[i][j] = A[i][j]
            elif i < j:
                U[i][j] = A[i][j]
    inverse_D = inverse_matrix(D)
    while (True):
        next_x = np.matmul(inverse_D, b - np.matmul(L + U, curr_x))
        if (np.sqrt(np.absolute(length_point(next_x) - length_point(curr_x)))) <= epsilon:
            return next_x
        curr_x = next_x

np.set_printoptions(precision=5)

A = init()

L, U = LU_decomposition(A)
#
inverse_A = inverse_matrix(A)
#
x = solving_l_e(L, U, b)

jacobi_answer = jacobi(A, b, x, epsilon)

print("A:\n", A)
#
print("L:\n", L)
#
print("U:\n", U)
#
print("A^(-1):\n", inverse_A)
#
print("Solving linear equations:\n", x)


print("Jacobi solution:\n", jacobi_answer)