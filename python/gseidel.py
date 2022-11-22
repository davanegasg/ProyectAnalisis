import numpy as np
from ex_funciones import factorizar, resta_matrices
from ex_funciones import prod_matrices, prod_matriz_vector, resta_vectores, suma_matrices, suma_vectores, norma


def gseidel(A, b, x, iter, tol):
    D, L, U = factorizar(A)
    cont = 0
    error = tol + 1
    #inv(D-L)
    DL = resta_matrices(D,L)
    DL = np.array(DL)
    DLi = np.linalg.inv(DL)
    #T=inv(D-L)*U
    T = prod_matrices(DLi, U) 
    #C=inv(D-L)*b
    C = prod_matriz_vector(DLi, b)
    x_ant = x
    while error > tol and cont < iter:
        x = suma_vectores(prod_matriz_vector(T, x), C)
        #Error relativo o absoluto
        error = norma(resta_vectores(x, x_ant))
        x_ant = x
        cont += 1
        # print(f'Ite: {cont}\nx: {x}')
    # print(x)
    print(f'Ite: {cont}\nx: {x}\nError: {error}')


A = [[4, 3, -2, -7],
     [3, 12, 8, -3],
     [2, 3, -9, 3],
     [1, -2, -5, 6],]
  
b = [20, 18, 31, 12]

gseidel(A, b, [2,2,2,2], 20, 0.0005)