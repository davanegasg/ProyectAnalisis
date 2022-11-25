def estrictamenteDiagonalDominante(A):
        import numpy as np

        X=np.array(A)

        Sum_values_in_given_row = np.sum(abs(X),axis=1)
        if np.all(((abs(np.diag(X)))) > np.sum(abs(X),axis=1)):
            return True
        else:
            return False

def jacobi(A,b,x0,Tol,Nmax):
        import numpy as np

        html = "</br>Jacobi</br></br>Results:</br>"

        C = []
        T = [[0 for i in range(len(A))] for j in range(len(A))]
        for i in range(len(A)):
            coef = 0
            if A[i][i] == 0:
                return html+f"</br>There is a 0 on the diagonal, at position {i+1},{i+1}, which generates a division by zero when you want to build the matrix C</br>"
            C.append((1/A[i][i])*b[i])
            coef = -(1/A[i][i])
            for j in range(len(A)):
                if i != j:
                    T[i][j] = A[i][j]*coef

        html += "</br>T:</br>"
        for i in T:
            result = ""
            for j in i:
                result += f"{j:.10e} "
            html+=result+"</br>"

        html += "</br>C:</br>"
        for i in C:
            html += f"{i}</br>"

        val, ne =  np.linalg.eig(T) # T es la matriz
        sr = max(abs(val))
        
        html += f"</br>Spectral radius:</br>{sr}</br></br>"
        if sr < 1:
            html += f"The system converges to the unique solution x=Tx + c since p(T) < 1</br></br>"
        else:
            html += f"The system does not converge to the unique solution x=Tx + c since p(T) >= 1</br></br>"

        if estrictamenteDiagonalDominante(A):
            html += f"The matrix is ​​strictly diagonal dominant and therefore converges for any initial approximation x0</br></br>"
        else:
            html += f"The matrix is ​​not strictly diagonal dominant and therefore does not converge for every initial approximation x0</br></br>"

        html += f"|i|E|X|</br>"
        x1 = [0 for i in range(len(A))]
        count = 0
        disp = Tol + 1

        def calcularNuevoJacobi(x0):
            for i in range(len(A)):
                sum1 = 0
                for j in range(len(A)):
                    if j != i:
                        sum1 += A[i][j]*x0[j]
                x1[i] = (b[i] - sum1)/A[i][i]
            return x1

        def norma(x1,x0):
            result = 0
            for i, j in zip(x1,x0):
                result += (i-j)**2
            from math import sqrt
            return sqrt(result)

        while disp > Tol and count <= Nmax:
            x1 = calcularNuevoJacobi(x0)
            result = [f"{i:.10e}" for i in x0]
            if count <= 9:
                ite = f"0{count}"
            else:
                ite = count
            html+=f"{ite} {disp:.10e} {result}</br>"
            count += 1
            disp = norma(x1,x0)
            x0 = [i for i in x1]
        if disp < Tol:
            if count <= 9:
                ite = f"0{count}"
            else:
                ite = count
            result = [f"{i:.10e}" for i in x0]
            html+=f"{ite} {disp:.10e} {result}</br></br>"
            html+=f"x:</br>"
            for i in x0:
                html+=f"{i}</br>"

            return html
        else:
            html+=f"Failed in {Nmax} iterations</br>"
            return html