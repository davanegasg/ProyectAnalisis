def sustitucion_progresiva(L, n, b):
    z=[]
    sum=0
    for k in range(n):
        sum = 0
        for j in range(k):
            sum += L[k][j]*z[j]
        z.append((b[k] - sum)/L[k][k])
    return z


# L = [[1, 0, 0, 0],
#      [0.75, 1, 0, 0],
#      [0.5, 0.15, 1, 0],
#      [0.25, -0.28, 0.19, 1],]

# b = [20, 18, 31, 12]
# z = sustitucion_progresiva(L, 4, b)
# print(z)

def sustitucion_regresiva(U,z):
   #Sustitución regresiva
    n = len(U)
    x=[]
    for i in range(n):  # Construye x
        U[i].append(z[i])
        x.append(0)
    for k in range(n, 0, -1):
        sum = 0
        for j in range(k, n):
            sum += U[k-1][j]*x[j]
        x[k-1] = (U[k-1][n] - sum)/U[k-1][k-1]
    return x

# result = sustitucion_regresiva(U,b)
# print(result)