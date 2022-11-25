def eliminacionSimple(A,b):
        html="</br>Simple Gaussian Elimination</br></br>"

        Ab, html = eliminacion(A,b,len(A),html)
        
        if "diagonal" in html:
            return html
        
        if "has no solution" in html:
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

        html+="</br>After applying back substitution</br></br>x:</br>"

        for i in x:
            html+=f"{i}</br>"

        return html
    
    
def eliminacion(A, b, n, html):
        Ab, html_aux = formaMatrizAumentada(A,b)
        html += f"</br>{html_aux}</br>"
        html+="Results</br></br>"
        etapa = 0
        html+=f"Stage {etapa}</br></br>"
        etapa += 1
        for i in A:
            result = ""
            for j in i:
                result += f"{j:.10e} "
            html += result+"</br>"
        for k in range(n-1):
            for i in range(k+1, n):
                if Ab[k][k] == 0.0:
                    html += f"</br>a 0 has been found on the diagonal, at position {k+1},{k+1} the method is suspended by a division by 0</br>"
                    return Ab, html
                multiplicador = Ab[i][k] / Ab[k][k]
                for j in range(k, n+1):
                    Ab[i][j] -= (multiplicador * Ab[k][j])
            html+=f"</br>Stage {etapa}</br></br>"
            for i in Ab:
                result = ""
                for j in i:
                    result += f"{j:.10e} "
                html+=result+"</br>"
            etapa += 1
        return Ab, html

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
    
#A = [[2, -1, 0, 3],[1, 0.5, 3, 8],[0, 13, -2, 11],[14, 5, -2, 3]]

#b = [[1],[1],[1],[1]]

#b = [1,1,1,1]

#print(eliminacionSimple(A,b))