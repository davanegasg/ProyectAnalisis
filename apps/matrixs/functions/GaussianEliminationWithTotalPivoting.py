def eliminacionTotal(A,b):
        html="</br>Gaussian elimination with full pivoting</br></br>"

        Ab, marcas, html = eliminacionGaussianaConPivoteo(A, b, len(A), html,"")

        if "diagonal" in html:
            return html

        if "no tiene solucion" in html:
            return html
        x = sustitucionRegresiva(Ab, len(A))
        if type(x) == str:    
            html += x
            x = infinitasSoluciones(Ab)
            html+="</br>Since the system is compatible indeterminate, it has infinitely many solutions and can be represented by:</br></br>x:</br>"

            for i in x:
                html+=f"{i}</br></br>"
            
            html += "</br>with t = 0</br>x:</br>"

            for i in x:
                fun = eval(f"lambda t:{i}")
                result = fun(0) 
                html+=f"{result:.10f}</br>"

            return html
        x = reordenar(x, marcas)

        html+="</br>After applying back substitution</br></br>x:</br>"

        for i in x:
            html+=f"{i}</br>"

        return html

def eliminacionGaussianaConPivoteo(A, b, n, html, pivoteo="parcial"):
        Ab, html_aux = formaMatrizAumentada(A, b)
        html += f"<br>{html_aux}</br>"
        if pivoteo == "parcial" or pivoteo == "parcialLU":
            if pivoteo == "parcial":
                etapa = 0
                html+="Results</br></br>"
                html+=f"Stage {etapa}</br></br>"
                for i in A:
                    result = ""
                    for j in i:
                        result += f"{j:.10e} "
                    html += result+"</br>"
                etapa += 1
            else:
                etapa = None
            pivoteo = pivoteoParcial
            for k in range(n-1):
                Ab = pivoteo(Ab, n, k)
                for i in range(k + 1, n):
                    if Ab[k][k] == 0:
                        html += f"</br>a 0 has been found on the diagonal, at position {k+1},{k+1} the method is suspended by a division by 0</br>"
                        return Ab, html
                    multiplicador = Ab[i][k] / Ab[k][k]
                    for j in range(k, n+1):
                        Ab[i][j] -= multiplicador * Ab[k][j]
                if etapa:
                    html+=f"</br>Stage {etapa}</br></br>"
                    for i in Ab:
                        result = ""
                        for j in i:
                            result += f"{j:.10e} "
                        html+=result+"</br>"
                    etapa += 1
            return Ab, html
        else:
            etapa = 0
            html+="Results</br></br>"
            html+=f"Stage {etapa}</br></br>"
            for i in A:
                result = ""
                for j in i:
                    result += f"{j:.10e} "
                html += result+"</br>"
            etapa += 1
            pivoteo = pivoteoTotal
            marcas = [i for i in range(n)]
            for k in range(n-1):
                Ab, marcas = pivoteo(Ab, n, k, marcas)
                for i in range(k + 1, n):
                    if Ab[k][k] == 0:
                        html += f"</br>a 0 has been found on the diagonal, at position {k+1},{k+1} the method is suspended by a division by 0</br>"
                        return Ab, marcas, html
                    multiplicador = Ab[i][k] / Ab[k][k]
                    for j in range(k, n+1):
                        Ab[i][j] -= multiplicador * Ab[k][j]
                html+=f"</br>Stage {etapa}</br></br>"
                for i in Ab:
                    result = ""
                    for j in i:
                        result += f"{j:.10e} "
                    html+=result+"</br>"
                etapa += 1
            return Ab, marcas, html
        
def sustitucionRegresiva(Ab, n):
        x = [0 for i in range(n)]
        if Ab[n-1][n-1] == 0:
            return f"</br>When trying to do backward substitution, a division by 0 is generated, which indicates that the system has infinitely many solutions.</br>" 
        x[n-1] = Ab[n-1][n] / Ab[n-1][n-1]
        for i in range(n-1, -1, -1):
            sumatoria = 0
            for p in range(i+1, n):
                sumatoria += Ab[i][p] * x[p]
            if Ab[i][i] == 0:
                return f"</br>When trying to do backward substitution, a division by 0 is generated, which indicates that the system has infinitely many solutions.</br>"    
            x[i] = (Ab[i][n] -  sumatoria)/Ab[i][i]
        return x

def infinitasSoluciones(Ab):
        x = []
        x.append("t")
        for i in range(len(Ab)-2,-1,-1):
            result = f"{Ab[i][len(Ab)]}"
            index = len(Ab)-1
            for j in x:
                result += f"-{Ab[i][index]}*{j}"
                index -= 1#
            result = f"({result})/{Ab[i][i]}"
            x.append(result)
        return x[::-1]

def reordenar(x, marcas):
        x_aux = [i for i in x]
        orden = [i for i in range(len(x))]
        for i, j in zip(marcas,orden):
            x[i] = x_aux[j]
        return x

def formaMatrizAumentada(A,b):
        import numpy as np
        n = len(A[0])
        det =  np.linalg.det(np.array(A))

        for i in A:
            if n != len(i):
                return A, "Matrix A presents equations with more or fewer unknowns than others, therefore the system is inconsistent and has no solution.</br>"
        ranA = np.linalg.matrix_rank(np.matrix(A))
        for a, b in zip(A, b):
            a.append(b)
        ranAb =  np.linalg.matrix_rank(np.matrix(A))
        result = ''
        if ranA == ranAb and ranAb == n:
            result += "The range of A is equal to the range of the augmented matrix and the range of A is equal to the number of unknowns, then the system is compatible determined and therefore the system has a unique solution.</br>"
        elif ranA == ranAb and ranAb < n:
            result += f"The range of A is equal to the range of the augmented matrix but the range of the augmented matrix is ​​less than the number of unknowns, then the system is compatible indeterminate and for this reason the system has infinite solutions, also the determinant of the matrix is {det:.5f} and therefore the method does not converge</br>"
        else:
            result += "The rank of A is less than the rank of the augmented matrix, so the system is incompatible and has no solution.</br>"
        return A, result

def pivoteoParcial(Ab, n, k, lu=False):
        mayor = abs(Ab[k][k])
        filaMayor = k
        for s in range(k+1, n):
            if abs(Ab[s][k]) > mayor:
                mayor = abs(Ab[s][k])
                filaMayor = s
        if mayor == 0:
            return 0
        else:
            if filaMayor != k:
                Ab = intercambioFilas(Ab, filaMayor, k)
            if lu:
                return Ab, filaMayor
            return Ab
        
def pivoteoTotal(Ab, n, k, marcas):
        mayor = 0
        filaMayor = k
        columnaMayor = k
        for r in range(k, n):
            for s in range(k, n):
                if abs(Ab[r][s]) > mayor:
                    mayor = abs(Ab[r][s])
                    filaMayor = r
                    columnaMayor = s
        if mayor == 0:
            return 0
        else:
            if filaMayor != k:
                Ab = intercambioFilas(Ab, filaMayor, k)
            if columnaMayor != k:
                Ab = intercambioColumnas(Ab, columnaMayor, k)
                marcas = intercambioMarcas(marcas, columnaMayor, k)
            return Ab, marcas

def intercambioFilas(Ab, filaMayor, k):
        filaAux = Ab[k]
        Ab[k] = Ab[filaMayor]
        Ab[filaMayor] = filaAux
        return Ab

def intercambioColumnas(Ab, columnaMayor, k):
        columAux = [Ab[i][k] for i in range(len(Ab))]
        for i in range(len(Ab)):
            Ab[i][k] = Ab[i][columnaMayor]
        for i in range(len(Ab)):
            Ab[i][columnaMayor] = columAux[i]
        return Ab

def intercambioMarcas(marcas, columnaMayor, k):
        marcaAux = marcas[k]
        marcas[k] = marcas[columnaMayor]
        marcas[columnaMayor] = marcaAux
        return marcas

#A = [[2, -1, 0, 3],[1, 0.5, 3, 8],[0, 13, -2, 11],[14, 5, -2, 3]]

#b = [[1],[1],[1],[1]]

#b = [1,1,1,1]

#print(eliminacionTotal(A,b))