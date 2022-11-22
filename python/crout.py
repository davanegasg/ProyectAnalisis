

from ex_funciones import dotm,columna, zero, eye
from sustituciones import sustitucion_progresiva, sustitucion_regresiva

def crout(A,b):
    #Inicializamos
    n = len(A)
    L = zero(n) 
    U = eye(n) 

    #Factorización
    for i in range(n-1):
        #Encontramos la columna L con la U que ya existe
        for j in range(i,n):
            L[j][i] = A[j][i] - dotm(L[j],0,i-1,columna(U,i),0,i-1)
        #Encontramos la fila U con la L que ya existe
        for j in range(i+1,n):
            U[i][j] = (A[i][j] - dotm(L[i],0,i-1,columna(U,j), 0, i-1))/L[i][i] 
    print(f'L: \n {L}\nU: \n {U}')
    L[n-1][n-1] = A[n-1][n-1] - dotm(L[n-1],0,n-1,columna(U,n-1),0,n-1)

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

# A = [[4, 3, -2, -7],
#      [3, 12, 8, -3],
#      [2, 3, -9, 3],
#      [1, -2, -5, 6],]
  
# b = [20, 18, 31, 12]

A = [
  [4,-1,0,3],
  [1,15.5,3,8],
  [0,-1.3,-4,1.1],
  [14,5,-2,30],
]

b = [1,1,1,1]

# A = [[4,-1,0,3],
#      [1,15.5,3,8],
#      [0,-1.3,-4,1.1],
#      [14,5,-2,30],]
     
# b = [1,1,1,1]
crout(A, b)