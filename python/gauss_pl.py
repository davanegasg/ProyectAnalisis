def eliminacion_gausiana(A,b, n):
    print("Empezo el metodo:")
    Ab=[]
    x=[]
    sum=0
    #Matriz ampliada
    for i in range(n):
        A[i].append(b[i])
        x.append(0)
    Ab = A
    
    #Eliminacion Gausiana
    for k in range(0, n): #Array de pivotes
        for i in range(k+1, n): #Hallar multiplicador, vuelve cero Ab[i][k]
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
        

A=[
   [4,-1,0,3],
   [1,15.5,3,8],
   [0,-1.3,-4,1.1],
   [14,5,-2,30],
]
b=[1,1,1,1]

eliminacion_gausiana(A, b, 4)