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

def intercambioMarcas(marcas, columnaMayor, k):
        marcaAux = marcas[k]
        marcas[k] = marcas[columnaMayor]
        marcas[columnaMayor] = marcaAux
        return marcas

def reordenar(x, marcas):
        x_aux = [i for i in x]
        orden = [i for i in range(len(x))]
        for i, j in zip(marcas,orden):
            x[i] = x_aux[j]
        return x

def sustitucionProgresiva(Lb, n):
        x = [Lb[0][n] / Lb[0][0]]
        while len(x) < n:
            r = 0
            for i in range(len(x)):
                r += Lb[len(x)][i]*x[i]
            r = (Lb[len(x)][n] - r)/Lb[len(x)][len(x)]
            x.append(r)
        return x

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

def intercambioFilas(Ab, filaMayor, k):
        filaAux = Ab[k]
        Ab[k] = Ab[filaMayor]
        Ab[filaMayor] = filaAux
        return Ab

def luParcial(A, b):
        etapa = 0
        L = []
        for i in range(len(A)):
            row = []
            for j in range(len(A)):
                if i != j:
                    row.append(0.0)
                else:
                    row.append(1.0)
            L.append(row)
        U = [[0.0 for i in range(len(A))] for j in range(len(A))]
        A = [[float(i) for i in j] for j in A]
        U[0] = [i for i in A[0]]
        def factorizacionLU(A, b, n, etapa, html):
            Ab, html_aux = formaMatrizAumentada(A,b) 
            html += f"</br>{html_aux}</br>" 
            marcas = [i for i in range(n)]                   
            for k in range(n-1):
                L[k][k] = 1
                Ab, mayor = pivoteoParcial(Ab, n, k, True)
                if mayor != k:
                    marcas = intercambioMarcas(marcas, mayor, k)
                mults_aux = {}
                for i in range(k+1, n):
                    if Ab[k][k] == 0:
                        html += f"</br>a 0 has been found on the diagonal, at position {k+1},{k+1} the method is suspended by a division by 0</br>"
                        return Ab, html
                    mults_aux[(i,k)] = multiplicador = Ab[i][k] / Ab[k][k]
                    for j in range(k, n+1):
                        Ab[i][j] -= (multiplicador * Ab[k][j])
                for i, j in mults_aux:
                    Ab[i][j] = mults_aux[(i,j)]
                for i, j in mults_aux:
                    L[i][j] = Ab[i][j]
                etapa += 1
                html += f"</br>Stage {etapa}</br></br>"
                for i in Ab:
                    result = ""
                    for j in i[:len(Ab)]:
                        result += f"{j:.10e} "
                    html+=f"{result}</br>"
                html+="</br>L:</br>"
                for i in L:
                    result = ""
                    for j in i:
                        result += f"{j:.10e} "
                    html+=f"{result}</br>"
                html+="</br>U:</br>"
                i = Ab[etapa]
                U[etapa] = i[:len(Ab)]
                for i in U:
                    result = ""
                    for j in i:
                        result += f"{j:.10e} "
                    html+=f"{result}</br>"
                html+="</br>P:(marcas)</br>"
                result = ""
                for i in marcas:
                    l = float(i)
                    result += "{0:.10e}".format(l)+" "
                html += result+"</br>"
            return Ab, marcas, html

        html=f"</br>LU with partial pivot:</br></br>Results</br></br>Stage {etapa}</br></br>"
        for i in A:
            result = ""
            for j in i:
                result += f"{j:.10e} "
            html+=result+"</br>"

        Ab, marcas, html = factorizacionLU(A,b, len(A), etapa, html)

        if "diagonal" in html:
            return html
        
        if "has no solution" in html:
            return html

        b = reordenar(b, marcas)
        Lb, result = formaMatrizAumentada(L,b)
        z = sustitucionProgresiva(Lb,len(L))
        Uz, result = formaMatrizAumentada(U,z)
        x = sustitucionRegresiva(Uz,len(U))

        if type(x) ==  str:    
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

        html+="</br>After applying forward and backward substitution</br></br>x:</br>"

        for i in x:
            html+=f"{i}</br>"

        return html