import json
from math import sqrt
import numpy as np
        
def estrictamenteDiagonalDominante(A):
        X=np.array(A)

        Sum_values_in_given_row = np.sum(abs(X),axis=1)
        if np.all(((abs(np.diag(X)))) > np.sum(abs(X),axis=1)):
            return True
        else:
            return False
        
def convert_string_to_list(string1):
    res = f"[{string1}]".strip(" ")
    res_to_json = json.loads(res)
    return res_to_json

def sor(A,b,x0,Tol,w,Nmax):
        
        
        
        html = "</br>SOR(relaxation)</br></br>Results:</br></br>"
        H = [[0 if i >= j else -A[i][j] for i in range(len(A))] for j in range(len(A))]
        T = [[0 if i < j else A[i][j] for i in range(len(A))] for j in range(len(A))]
        T = np.array(T)
        try:
            C = list((np.linalg.inv(T)).dot(np.array(b)))
        except:
            return html + "</br>The array C constructed is singular, which implies the method stops</br>"

        try:
            T = list((np.linalg.inv(T)).dot(np.array(H)))
        except:
            return html + "</br>The constructed matrix T is singular, which implies the method stops</br>"

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

        x1 = [0 for i in range(len(A))]
        count = 0
        disp = Tol + 1

        def calcularNuevoSor(x0):
            for i in range(len(A)):
                sum1 = 0
                for j in range(len(A)):
                    if j != i:
                        sum1 += A[i][j]*x1[j]
                x1[i] = ((1-w)*x0[i])+(w*(b[i] - sum1)/A[i][i])
            return x1

        def norma(x1,x0):
            result = 0
            for i, j in zip(x1,x0):
                result += (i-j)**2
            return sqrt(result)

        while disp > Tol and count < Nmax:
            x1 = calcularNuevoSor(x0)
            result = [f"{i:.10e}" for i in x0]
            if count <= 9:
                ite = f"0{count}"
            else:
                ite = count
            html+=f"{ite} {disp:.10e} {result}</br>"
            disp = (norma(x1,x0))
            x0 = [i for i in x1]    
            count += 1
            
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
            html+=f"Failure in {Nmax} iterations</br>"
            return html


# print(sor([[4, -1, 0, 3], [1, 15.5, 3, 8], [0, -1.3, -4, 1.1], [14, 5, -2, 30]],[1,1,1,1],[0,0,0,0],0.0000007,1.5,100))