from tabulate import tabulate

def gaussSeidel(A, b, x, maxIterations, tol):
    N = len(b)
    solution = []
    filaMatrizSolucion =[]
    xprev = [0.0 for i in range(N)]
    for i in range(maxIterations):
        for j in range(N):
            xprev[j] = x[j]
        for j in range(N):
            summ = 0.0
            for k in range(N):
                if (k != j):
                    summ = summ + A[j][k] * x[k]
            x[j] = (b[j] - summ) / A[j][j]
            filaMatrizSolucion.append(x[j])
        
        diff1norm = 0.0
        oldnorm = 0.0
        for j in range(N):
            diff1norm = diff1norm + abs(x[j] - xprev[j])
            oldnorm = oldnorm + abs(xprev[j])  
        if oldnorm == 0.0:
            oldnorm = 1.0
        norm = diff1norm / oldnorm
        solution.append([i,norm, filaMatrizSolucion])
        filaMatrizSolucion =[]
        if (norm < tol) and i != 0:
            return tabulate(solution, headers=["iter", "error", "Solution", ], tablefmt="html")
            
    return "Doesn't converge."

#matrix2 =     [[4, -1, 0, 3],[1, 15.5, 3, 8],[0, -1.3, -4, 1.1],[14, 5, -2, 30]]
#vector2 = [1,1,1,1]
#guess = [0, 0,0,0]



#gaussSeidel(matrix2, vector2, guess, 100, 10**-7)