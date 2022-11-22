from ex_funciones import factorizar, inversa_D
from ex_funciones import prod_matrices, prod_matriz_vector, resta_vectores, suma_matrices, suma_vectores, norma


def jacobi(A, b, x, iter, tol):
    D, L, U = factorizar(A)
    cont = 0
    error = tol + 1
    # D^-1(L+U)x + D^-1b
    Di = inversa_D(D)
    T = prod_matrices(Di, suma_matrices(L,U))
    C = prod_matriz_vector(Di, b)
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

jacobi(A, b, [2,2,2,2], 10000, 0.0005)