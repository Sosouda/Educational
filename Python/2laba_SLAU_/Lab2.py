#Solution on C++ in CPP/LabaM2

import numpy as np

def determinant(a):
    det = (  a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1]) 
           - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0]) 
           + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))
    return det

def kramer(A, B):
    print("Метод Крамера: ")
    det = determinant(A)
    for j in range (3):
        Ai = np.copy(A)
        for i in range (3):
            Ai[i][j] = B[i]
        print ("X[{}] = {}".format(j+1,(determinant(Ai)) / det))

def iterations_method(A, B):
    print("Метод простых итераций: ")
    x = np.array([0, 0, 0], dtype=float)
    x_new = np.array([0, 0, 0], dtype=float)
    epsilon = 0.0001
    max_iterations = 100

    for k in range(max_iterations):
        for i in range(3):
            sum = 0
            for j in range(3):
                if j != i:
                    sum += A[i][j] * x[j]
            x_new[i] = (B[i] - sum) / A[i][i]

        p = np.sum(np.abs(x_new - x))
        x = np.copy(x_new)

        if p < epsilon:
            print("Итераций: ", k + 1)
            for i in range(3):
                print("X[{}] = {}".format(i, x[i]))
            break

A = np.array([[10, -1, 2], [-1, 11, -1], [2, -1, 10]])
B = np.array([6, 25, -11])

print()
kramer(A, B)
print()
iterations_method(A, B)