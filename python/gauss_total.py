
def pivoteo_total(Ab, n, k):
    mayor = fila2 = columna2 = 0
    for i in range(k, n): 
        for j in range(k, n):
            fila2, columna2 = (i, j) if abs(mayor) < abs(Ab[i][j]) else (fila2, columna2)
            mayor = Ab[i][j] if abs(mayor) < abs(Ab[i][j]) else mayor
    return mayor, fila2, columna2
    
def cambio_fila(Ab, fila1, fila2):
    Ab_aux = Ab.copy()
    Ab[fila1] = Ab[fila2]
    Ab[fila2] = Ab_aux[fila1]
    return Ab

def cambio_columna(Ab, columna1, columna2, x_aux, n):
    columna_aux = 0
    x_aux_copy = x_aux.copy()
    x_aux[columna1] = x_aux[columna2]
    x_aux[columna2] = x_aux_copy[columna1]
    for i in range(0, n): 
        columna_aux = Ab[i][columna1]
        Ab[i][columna1] = Ab[i][columna2]
        Ab[i][columna2] = columna_aux
    return Ab


def eliminacion_gausiana_piv_total(A,b, n):
    print("Empezo el metodo:")
    Ab=[]
    x=[]
    x_aux = []
    for i in range(n):
        x_aux.append(i)
    sum=0
    #Matriz ampliada
    for i in range(n):
        A[i].append(b[i])
        x.append(0)
    Ab = A
    
    for k in range(0, n): #Array de pivotes
        for i in range(k+1, n): #Hallar multiplicador, vuelve cero Ab[i][k]
            mayor, fila2, columna2 = pivoteo_total(Ab, n, k)
            Ab = cambio_fila(Ab, k, fila2)
            Ab = cambio_columna(Ab, k, columna2, x_aux, n)
            M = Ab[i][k]/Ab[k][k]
            Ab[i][k] = 0
            
            for j in range(k+1, n+1): #Resta la filaActual - anterios*multiplicador
                Ab[i][j] = Ab[i][j] - M*Ab[k][j]
    
    print("Empezo el sustitución:")
    #Sustitución regresiva
    for k in range(n, 0, -1):
        sum = 0
        for j in range(k, n):
            sum += Ab[k-1][j]*x[j]
        x[k-1] = (Ab[k-1][n] - sum)/Ab[k-1][k-1]
    for i in range(n):
        print('x' + str(x_aux[i]) + '=' + str(x[i]))
        

# A = [[-7, 2, -3, 4],
#      [5, -1, 14, -1],
#      [1, 9, -7, 5],
#      [-12, 13, -8, -4],]
  
# b = [-12, 13, 31, -32]

# x = [0, 1, 2, 3]
A = [
  [4,-1,0,3],
  [1,15.5,3,8],
  [0,-1.3,-4,1.1],
  [14,5,-2,30],
]

b = [1,1,1,1]

eliminacion_gausiana_piv_total(A, b, 4)
# mayor, fila2 = pivoteo_parcial(A, 4, 0)
# nuevo = cambio_fila(A, 0, 3)

# print(mayor, fila2)

# nuevo = cambio_columna(A, 1, 3, x, 4)
# mayor, fila2, columna2 = pivoteo_total(A, 4, 0)

# print(mayor, fila2, columna2)