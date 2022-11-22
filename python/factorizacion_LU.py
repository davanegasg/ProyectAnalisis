from ex_funciones import eye
from sustituciones import sustitucion_progresiva, sustitucion_regresiva


def pivoteo_parcial(A, n, k):
    mayor = fila2 = 0
    for i in range(k, n): #Array de pivotes
        fila2 = i if abs(mayor) < abs(A[i][k]) else fila2
        mayor = A[i][k] if abs(mayor) < abs(A[i][k]) else mayor
    return mayor, fila2
    
def cambio_fila(A, fila1, fila2):
    A_aux = A.copy()
    A[fila1] = A[fila2]
    A[fila2] = A_aux[fila1]
    return A

def factorizacion_LU(A,b, n):
    print("Empezo el metodo:")
    L = eye(4)
    P = eye(4)
    
    
    for k in range(0, n): 
        for i in range(k+1, n): 
            mayor, fila2 = pivoteo_parcial(A, n, k)
            A = cambio_fila(A, k, fila2)
            P = cambio_fila(P, k, fila2)
            b = cambio_fila(b, k, fila2)
            M = A[i][k]/A[k][k]
            L[i][k] = M
            A[i][k] = 0
            
            for j in range(k+1, n): #Resta la filaActual - anterios*multiplicador
                A[i][j] = A[i][j] - M*A[k][j]
    
    print("Empezo la sustitución:")
    #Sustitución progresiva
    z = sustitucion_progresiva(L, n, b)
    x = sustitucion_regresiva(A, z)
    
    print('U')
    print(A)
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

A = [[4, 3, -2, -7],
     [3, 12, 8, -3],
     [2, 3, -9, 3],
     [1, -2, -5, 6],]
  
b = [20, 18, 31, 12]

A = [[4,-1,0,3],
     [1,15.5,3,8],
     [0,-1.3,-4,1.1],
     [14,5,-2,30],]
     
b = [1,1,1,1]
factorizacion_LU(A, b, 4)
# mayor, fila2 = pivoteo_parcial(A, 4, 0)
# nuevo = cambio_fila(A, 0, 3)

# print(mayor, fila2)