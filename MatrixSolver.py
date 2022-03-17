def matrixMul(matrixA, matrixB):
    if len(matrixA) == len(matrixA[0]) and len(matrixB) == len(matrixB[0]) and len(matrixA) == len(matrixB):
        matrixC = [[0 for x in range(len(matrixA))] for y in range(len(matrixB))]
        for i in range(len(matrixC)):
            for j in range(len(matrixC)):
                for k in range(len(matrixC)):
                    matrixC[i][j] += matrixA[i][k] * matrixB[k][j]
        return matrixC
    else:
        print("Not NxN / same size")


def machineEpsilon(func=float):
    machine_epsilon = func(1)
    machine_epsilon_last = 0.0
    while func(1) + machine_epsilon != func(1):
        machine_epsilon_last = machine_epsilon
        machine_epsilon = func(machine_epsilon) / func(2)
    return machine_epsilon_last


def I_matrix(A):
    matrixC = [[0 for x in range(len(A))] for y in range(len(A))]
    for i in range(len(A)):
        matrixC[i][i] = 1
    return matrixC


"""
X = [[12, 7, -4],
     [4, 5, 6],
     [7, 8, 9]]
# 3x4 matrix
Y = [[5, 8, 1],
     [6, 7, 3],
     [-9, 5, 9]]
# result is 3x4
result = [[ 0, 0, 0],
          [ 0, 0, 0],
          [ 0, 0, 0]]
result=matrixMul(X,Y)
for i in range(3):
    print(result[i])"""


def copy_matrix(A):
    matrixC = [[A[y][x] for x in range(len(A))] for y in range(len(A))]
    return matrixC


def determinant_recursive(A, total=0):
    indices = list(range(len(A)))
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val
    for fc in indices:
        As = copy_matrix(A)
        As = As[1:]
        height = len(As)
        for i in range(height):
            As[i] = As[i][0:fc] + As[i][fc + 1:]
        sign = (-1) ** (fc % 2)
        sub_det = determinant_recursive(As)
        total += sign * A[0][fc] * sub_det
    return total


def matrixSolve(matrix):
    elementary = []
    for i in range(len(matrix)):
        if len(matrix) != len(matrix[i]):
            exit(0)
    if determinant_recursive(matrix) != 0:
        solve = I_matrix(matrix)
        for i in range(len(matrix)):
            if matrix[i][i] == 0.0 or abs(matrix[i][i]) - machineEpsilon() < 0.0:
                k = i
                while k < len(matrix) and matrix[k][i] == 0:
                    k += 1
                temp = solve[i]
                solve[i] = solve[k]
                solve[k] = temp
                elementary.append(solve)
                matrix = matrixMul(solve, matrix)
            if matrix[i][i] != 1:
                solve = I_matrix(matrix)
                solve[i][i] = 1 / matrix[i][i]
                elementary.append(solve)
                matrix = matrixMul(solve, matrix)
            m = i + 1
            while m < len(matrix):
                if matrix[m][i] != 0 or abs(matrix[m][i])-machineEpsilon()<0:
                    solve = I_matrix(matrix)
                    solve[m][i] = -matrix[m][i] / matrix[i][i]
                    elementary.append(solve)
                    matrix = matrixMul(solve, matrix)
                m = m + 1
        n = len(matrix) - 1
        while n >= 0:
            m = n - 1
            while m >= 0:
                if matrix[m][n] != 0 or abs(matrix[m][n])-machineEpsilon()<0:
                    solve = I_matrix(matrix)
                    solve[m][n] = -matrix[m][n] / matrix[n][n]
                    elementary.append(solve)
                    matrix = matrixMul(solve, matrix)
                m = m - 1
            n = n - 1

    return matrix


def printMatrix(matrix):
    for i in matrix:
        print('\t'.join(map(str, i)))


X = [[12, 7, -4,1],
     [4, 5, 6,1],
    [4, 3, 6,4],
     [7, 8, 9,3]]
printMatrix(matrixSolve(X))
