

def factorizacionDirecta(A,etapa,html,me="cr"):
        L, U =  inicializaLU(len(A),1.0)
        for k in range(len(A)):
            sum1 = 0
            for p in range(k):
                sum1 += L[k][p]*U[p][k]
            if me == "do":
                U[k][k] = A[k][k] - sum1
            elif me == "cr":
                L[k][k] = A[k][k] - sum1
            else:
                try:
                    L[k][k] = math.sqrt(A[k][k] - sum1)
                    U[k][k] = math.sqrt(A[k][k] - sum1)
                except:
                    html+=f"The program does not support imaginary numbers and the method requires it for this exercise.</br>"
                    return L, U, html
            for i in range(k+1,len(A)):
                sum2 = 0
                for p in range(k):
                    sum2 += L[i][p]*U[p][k]
                if me == "do":
                    if U[k][k] == 0:
                        html += f"</br>A 0 has been found on the diagonal, in the position {k+1},{k+1} the method is suspended by a division by 0</br>"
                        return L, U, html 
                    L[i][k] = (A[i][k] - sum2)/U[k][k]
                if me == "cr":
                    L[i][k] = A[i][k] - sum2
                else:
                    if U[k][k] == 0:
                        html += f"</br>A 0 has been found on the diagonal, in the position {k+1},{k+1} the method is suspended by a division by 0</br>"
                        return L, U, html 
                    L[i][k] = (A[i][k] - sum2)/U[k][k]
            for j in range(k+1,len(A)):
                sum3 = 0
                for p in range(k):
                    sum3 += L[k][p]*U[p][j]
                if me == "do":
                    U[k][j] = A[k][j] - sum3
                if me == "cr":
                    if L[k][k] == 0:
                        html += f"</br>A 0 has been found on the diagonal, in the position {k+1},{k+1} the method is suspended by a division by 0</br>"
                        return L, U, html         
                    U[k][j] = (A[k][j] - sum3)/L[k][k]
                else:
                    if L[k][k] == 0:
                        html += f"</br>A 0 has been found on the diagonal, in the position {k+1},{k+1} the method is suspended by a division by 0</br>"
                        return L, U, html   
                    U[k][j] = (A[k][j] - sum3)/L[k][k]
            etapa += 1
            html += f"</br>Stage {etapa}</br></br>L:</br>" 
            for i in L:
                result = ""
                for j in i:
                    result += f"{j:.10e} "
                html += f"{result}</br>"
            html+="</br>U:</br>"
            for i in U:
                result = ""
                for j in i:
                    result += f"{j:.10e} "
                html += f"{result}</br>"
            html += "</br>"
        return L, U, html

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

def inicializaLU(n,val):
        L = [[0 for i in range(n)] for j in range(n)]
        U = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            L[i][i]  = val
            U[i][i]  = val
        return L, U

def crout(A,b):
        etapa = 0
        html = f"</br>Crout</br></br>Results</br></br>Stage {etapa}</br></br>"
        for i in A:
            result = ""
            for j in i:
                result += f"{j:.10e} "
            html+=result+"</br>"
        L, U, html = factorizacionDirecta(A,etapa,html,"cr")

        if "diagonal" in html:
            return html
        
        if "there is no solution" in html:
            return html

        Lb, result = formaMatrizAumentada(L,b)
        z = sustitucionProgresiva(Lb,len(L))
        Uz, result = formaMatrizAumentada(U,z)
        x = sustitucionRegresiva(Uz,len(U))

        html+="</br>After applying forward and backward substitution</br></br>x:</br>"

        for i in x:
            html+=f"{i}</br>"

        return html

# A = [[4, -1, 0, 3],[1, 15.5, 3, 8],[0, -1.3, -4, 1.1],[14, 5, -2, 30]]

#b = [[1],[1],[1],[1]]

#b = [1,1,1,1]

#print(crout(A,b))