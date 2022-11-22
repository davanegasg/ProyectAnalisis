
def pivoteo_parcial(Ab, n, k):
    mayor = fila2 = 0
    for i in range(k, n): #Array de pivotes
        fila2 = i if abs(mayor) < abs(Ab[i][k]) else fila2
        mayor = Ab[i][k] if abs(mayor) < abs(Ab[i][k]) else mayor
    return mayor, fila2
    
def cambio_fila(Ab, fila1, fila2):
    Ab_aux = Ab.copy()
    Ab[fila1] = Ab[fila2]
    Ab[fila2] = Ab_aux[fila1]
    return Ab

def eliminacion_gausiana_piv_parcial(A,b, n):
    print("Empezo el metodo:")
    Ab=[]
    x=[]
    sum=0
    #Matriz ampliada
    for i in range(n):
        A[i].append(b[i])
        x.append(0)
    Ab = A
    
    for k in range(0, n): #Array de pivotes
        for i in range(k+1, n): #Hallar multiplicador, vuelve cero Ab[i][k]
            mayor, fila2 = pivoteo_parcial(Ab, n, k)
            Ab = cambio_fila(Ab, k, fila2)
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
        print('x' + str(i) + '=' + str(x[i]))
        

# A = [[-7, 2, -3, 4],
#      [5, -1, 14, -1],
#      [1, 9, -7, 5],
#      [-12, 13, -8, -4],]
  
# b = [-12, 13, 31, -32]

# A = [[4, 3, -2, -7],
#      [3, 12, 8, -3],
#      [2, 3, -9, 3],
#      [1, -2, -5, -6],]
  
# b = [20, 18, 31, 12]
A = [
  [4,-1,0,3],
  [1,15.5,3,8],
  [0,-1.3,-4,1.1],
  [14,5,-2,30],
]

b = [1,1,1,1]
eliminacion_gausiana_piv_parcial(A, b, 4)
# mayor, fila2 = pivoteo_parcial(A, 4, 0)
# nuevo = cambio_fila(A, 0, 3)

# print(mayor, fila2)