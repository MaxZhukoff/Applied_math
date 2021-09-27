import numpy as np
from scipy.sparse import csr_matrix, random
from scipy import stats


# n = 2
# b = np.array([11, 13])
# epsilon = 0.01
# x = np.array([0, 0])

n = 1000

denst = 0.1


b = np.zeros(n)
for i in range(len(b)):
    b[i] = np.random.randint(0, 15)

epsilon = 0.01

x = np.zeros(n)

def init():
    # square_matrix = np.array([[2, 4, 3, 5], [-4, -7, -5, -8], [6, 8, 2, 9], [4, 9, -2, 14]])
    # square_matrix = np.array([[2, 1], [5, 7]])
    # square_matrix = np.array([[10, -1, 2, 0], [-1, 11, -1, 3], [2, -1, 10, -1], [0, 3 , -1 , 8 ]])
    # matrix = csr_matrix(square_matrix).toarray()
    rvs = stats.poisson(10, loc=10).rvs
    matrix = random(n, n, density=denst, data_rvs=rvs, format="csr", dtype=float).toarray()
    for i in range(n):
        diag_max = 0
        for j in range(n):
            if i != j:
                diag_max += matrix[i][j]
            if j == n - 1:
                matrix[i][i] = diag_max + np.random.randint(0, 15)
    return matrix

def LU_decomposition(matrix):
    it = 0
    L = np.zeros(shape=(n, n), dtype=np.float_)
    U = np.zeros(shape=(n, n), dtype=np.float_)
    for i in range(n):
        U[0][i] = matrix[0, i]
        L[i][0] = matrix[i][0] / U[0][0]
        for j in range(n):
            it += 1
            sigmaU = 0
            for k in range(i):
                sigmaU += L[i][k] * U[k][j]
            U[i][j] = matrix[i][j] - sigmaU
            if i <= j:
                sigmaL = 0
                for l in range(i):
                    sigmaL += L[j][l] * U[l, i]
                L[j][i] = (matrix[j][i] - sigmaL) / U[i][i]
            print(i, j, U[i][j], L[i][j])
    print("LU iterations: ", it)
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


iter = 0
def solving_l_e(L, U, b):
    global iter
    y = np.array([])
    for i in range(n):
        iter += 1
        y_i = 0
        for j in range(i):
            y_i += L[i][j] * y[j]
        y_i = (b[i] - y_i)
        y = np.append(y, y_i)
    x = np.zeros(n)
    for i in reversed(range(n)):
        iter += 1
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
    it = 0
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
        it += 1
        next_x = np.matmul(inverse_D, b - np.matmul(L + U, curr_x))
        if (np.sqrt(np.absolute(length_point(next_x) - length_point(curr_x)))) <= epsilon:
            it += 1
            print("Jacobi method iterations: ", it)
            return next_x
        curr_x = next_x

def init_cond_matrix(k):
    # matrix = np.random.randint(-5, 1, n ** 2).reshape(-1, n)
    rvs = stats.poisson(10, loc=10).rvs
    matrix = random(k, k, density=denst, data_rvs=rvs, format="csr").toarray()
    for i in range(k):
        for j in range(k):
            if i == j:
                matrix[i, j] = matrix[i, i] + 10 ** (-k)
    return matrix

def init_gilbert_matrix(k):
    # matrix = np.random.randint(-5, 1, n ** 2).reshape(-1, n)
    rvs = stats.poisson(10, loc=10).rvs
    matrix = random(k, k, data_rvs=np.zeros, format="csr").toarray()
    for i in range(k):
        for j in range(k):
            matrix[i][j] = 1/((i + 1) + (j + 1) - 1)
    return matrix

def error_of_answer(matrix, b, answer):
    true_answer = np.linalg.solve(matrix, b)
    error = np.linalg.norm(true_answer - answer)
    return error

# np.set_printoptions(precision=5)

A = init()
print("A:\n", A)

L, U = LU_decomposition(A)
print("L:\n", L)
print("U:\n", U)

inverse_A = inverse_matrix(A)
print("A^(-1):\n", inverse_A)

lu_answer = solving_l_e(L, U, b)
print("Solving linear equations:\n", lu_answer)

print("LU solving iterations: ", iter)

jacobi_answer = jacobi(A, b, x, epsilon)
print("Jacobi solution:\n", jacobi_answer)

cond_matrix = init_cond_matrix(n)
print("Cond matrix:\n", cond_matrix)

error = error_of_answer(A, b, jacobi_answer)
print("Error: ", error)

gilbert_matrix = init_gilbert_matrix(n)
print("Gilbert matrix\n", gilbert_matrix)
