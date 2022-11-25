import json
import numpy as np
from cmath import sqrt
from tabulate import tabulate


def sustProg(L, b, n):
    result = ""
    if (L[0][0] == 0):
        return
    else:
        z = np.zeros(n, dtype=complex)
        suma3 = 0
        z[0] = b[0][0]/L[0][0]
        for k in range(1, n):
            if (L[k][k] == 0):
                result += f"Element {k} in L diagonal, is zero"
                return result
            else:
                for r in range(k):
                    suma3 = suma3+(L[k][r]*z[r])
                z[k] = (b[k][0]-suma3)/L[k][k]
                suma3 = 0
    return z, result


def sustRegr(U, z, n):
    result = ""
    if (U[0][0] == 0):
        return
    else:
        x = np.zeros(n, dtype=complex)
        suma4 = 0
        x[n-1] = z[n-1]/U[n-1][n-1]
        for k in range(n-2, -1, -1):
            if U[k][k] == 0:
                result += f"Element {k} in U diagonal, is zero"
                return result
            else:
                suma4 = 0
                for r in range(k+1, n):
                    suma4 = suma4+(U[k][r]*x[r])
                x[k] = (1/U[k][k])*(z[k]-suma4)
    return x, result


def cholesky(A):
    result = ""
    n = len(A)
    L = [[0 for j in range(n)] for i in range(n)]
    U = [[0 for j in range(n)] for i in range(n)]
    for i, j in zip(range(n), range(n)):
        U[i][j] = 1
    for i, j in zip(range(n), range(n)):
        L[i][j] = 1

    for k in range(n):
        suma1 = 0
        for p in range(0, k):
            suma1 += L[k][p]*U[p][k]
        L[k][k] = sqrt(A[k][k]-suma1)  # Complex number handled
        U[k][k] = L[k][k]
        for i in range(k, n):
            suma2 = 0
            for p in range(k):
                suma2 += L[i][p]*U[p][k]
            L[i][k] = (A[i][k]-suma2)/(U[k][k])
        for j in range(k+1, n):
            suma3 = 0
            for p in range(k):
                suma3 += L[k][p]*U[p][j]
            U[k][j] = (A[k][j]-suma3)/(L[k][k])
            
        result += f"<br>Stage: {k+1}:"
        result += f"<br>Matrix L:"
        table_L = tabulate(L,[f"x{i}" for i in range(len(L))], tablefmt="html", stralign="left")
        result += f"{table_L}"
        
        result += f"<br>Matrix U:"
        table_U = tabulate(U,[f"x{i}" for i in range(len(U))], tablefmt="html", stralign="left")
        result += f"{table_U}"

        

    return L, U, result


def convert_string_to_list(string):
    res = f"[{string}]".strip(" ")
    res_to_json = json.loads(res)
    return res_to_json


def fill_matrix(A_str, b_str):
    result = []
    # Fill matrix
    # [[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]]
    A = np.array(convert_string_to_list(A_str))
    b = np.array(convert_string_to_list(b_str),
                 dtype=complex)  # [[1],[1],[1],[1]]
    
    LU_cholesky = cholesky(A)
    L = LU_cholesky[0]
    U = LU_cholesky[1]
    stages = LU_cholesky[2]
    
    n = len(A)

    # Apply sustitution
    z = sustProg(L, b, n)[0]
    x = sustRegr(U, z, n)[0]
    

    # Show answer
    
    return x, stages

##stages todas las l y u por etapas 
## x respuesta 
## L lFinal
## U uFinal
#fill_matrix("[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]", "[1],[1],[1],[1]")