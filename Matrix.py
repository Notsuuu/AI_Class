#Perhitungan Matrix dengan Library
import numpy as np

A = np.array([[3, 0], [-1, 2], [1, 1]])
B = np.array([[4, -1], [0, 2]])
C = np.array([[1, 4, 2], [3, 1, 5]])
D = np.array([[1, 5, 2], [-1, 0, 1], [3, 2, 4]])
E = np.array([[6, 1, 3], [-1, 1, 2], [4, 1, 3]])

A_kali_C = np.dot(A, C)
print("Hasil dari A x C : ")
print(A_kali_C)

try:
    A_kali_D = np.dot(A, D)
    print("Hasil dari A x D : ")
    print(A_kali_D)
except Exception as e:
     print("Error pada perhitungan A x D:", e)

D_tambah_E = D + E
print("Hasil dari D + E : ")
print(D_tambah_E)

D_kurang_E = D - E
print("Hasil dari D - E : ")
print(D_kurang_E)

#Perhitungan Matrix tanpa Library
A = [[3, 0], [-1, 2], [1, 1]]
B = [[4, -1], [0, 2]]
C = [[1, 4, 2], [3, 1, 5]]
D = [[1, 5, 2], [-1, 0, 1], [3, 2, 4]]
E = [[6, 1, 3], [-1, 1, 2], [4, 1, 3]]

def perkalian_matrix(X, Y):
    result = [[0 for _ in range(len(Y[0]))] for _ in range(len(X))]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result

def penjumlahan_matrix(X, Y):
    result = [[0 for _ in range(len(X[0]))] for _ in range(len(X))]
    for i in range(len(X)):
        for j in range(len(X[0])):
            result[i][j] = X[i][j] + Y[i][j]
    return result

def pengurangan_matrix(X, Y):
    result = [[0 for _ in range(len(X[0]))] for _ in range(len(X))]
    for i in range(len(X)):
        for j in range(len(X[0])):
            result[i][j] = X[i][j] - Y[i][j]
    return result

try:
    A_kali_C = perkalian_matrix(A, C)
    print("\nHasil dari A x C:")
    for row in A_kali_C:
        print(row)
except Exception as e:
    print("Error pada perhitungan A x C:", e)

try:
    A_kali_D = perkalian_matrix(A, D)
    print("\nHasil dari A x B:")
    for row in A_kali_D:
        print(row)
except Exception as e:
    print("Error pada perhitungan A x D:", e)

try:
    D_tambah_E = penjumlahan_matrix(D, E)
    print("\nHasil dari D + E:")
    for row in D_tambah_E:
        print(row)
except Exception as e:
    print("Error pada perhitungan D + E:", e)

try:
    D_kurang_E = pengurangan_matrix(D, E)
    print("\nHasil dari D - E:")
    for row in D_kurang_E:
        print(row)
except Exception as e:
    print("Error pada perhitungan D - E:", e)