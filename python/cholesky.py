import math
from ex_funciones import dotm,columna, zero, eye
from sustituciones import sustitucion_progresiva, sustitucion_regresiva

def cholesky(A,b):
    #Inicializamos
    n = len(A)
    L = eye(n) 
    U = eye(n) 

    #Factorización
    for i in range(n-1):
        L[i][i] = math.sqrt(A[i][i] - dotm(L[i],0, i-1, columna(U,i),0,i-1))
        U[i][i] = L[i][i] 
        #
        for j in range(i,n):
        #
            L[j][i] = (A[j][i] - dotm(L[j],0,i-1,columna(U,i),0,i-1)) / U[i][i]
        
        for j in range(i+1,n):
        #
            U[i][j] = (A[i][j] - dotm(L[i],0,i-1,columna(U,j),0,i-1) ) / L[i][i] 
    print(f'L: \n {L}\nU: \n {U}')
    L[n-1][n-1] = math.sqrt(A[n-1][n-1] - dotm(L[n-1],0,n-1,columna(U,n-1),0,n-1))
    U[n-1][n-1] = L[n-1][n-1]  
    z = sustitucion_progresiva(L,n,b) 
    x = sustitucion_regresiva(U,z) 

    print('U')
    print(U)
    print('L')
    print(L)
    print('z')
    print(z)
    print('x')
    print(x)

A = [[4, 3, -2, -7],
     [3, 12, 8, -3],
     [2, 3, -9, 3],
     [1, -2, -5, 6],]
  
b = [20, 18, 31, 12]

cholesky(A, b)