import numpy as np
import sympy as sp
import scipy
import json


def dispersion(x, deltaX):
    resultado = list(range(len(x)))

    for a in range(len(x)):
        resultado[a] = abs(deltaX-x)

    return resultado


def mayorError(x):
    mayor = x[0]
    for a in x:
        if a > mayor:
            mayor = a
    return a


def encontrarx(mat, x):
    print(mat)
    print(x)
    resultado = list(range(len(mat)))
    for a in range(len(mat)):
        cont = 0
        for b in range(len(mat)):
            if b != a:
                cont -= (mat[a][b]*x[b])
        cont += mat[a][len(mat)-1]
        print(str(cont))
        print(str(mat[a][a]))
        cont = cont/x[a]
        resultado[a] = cont
    print(resultado)
    return resultado


def plu(mat):
    P, L, U = scipy.linalg.lu(mat)
    return P, L, U


def susre(Ab):
    n = len(Ab)
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        sumatoria = 0
        for p in range(i+1, n):
            sumatoria += Ab[i][p]*x[p]

        x[i] = (Ab[i][n]-sumatoria)/float(Ab[i][i])
    return x


def suslu(Ab):
    n = len(Ab)
    x = np.zeros(n)
    for i in range(n):
        sumatoria = 0
        for p in range(n):
            sumatoria += Ab[i][p]*x[p]
        print(sumatoria)
        x[i] = (Ab[i][n]-sumatoria)/float(Ab[i][i])
    return x


def printmat(x):
    for i in range(len(x)):
        for j in range(len(x)):
            print(str(x[i][j])+", ", end="")
        print("= "+str(x[i][len(x)])+"\n")
    print("\n\n\n\n_________________")


def checkUnique(x):
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] == x[j] and i != j:
                return False
    return True


def swapRows(matrix, row1, row2):
    temp = np.copy(matrix[row2])
    matrix[row2] = matrix[row1]
    matrix[row1] = temp


def swapValues(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp


def swapCols(matrix, col1, col2):
    for i in range(len(matrix)):
        matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]


def methodStep(matrix, b):
    m = np.copy(matrix)
    b2 = np.copy(b)
    n = np.zeros((len(m), len(m)+1))
    for i in range(len(m)):
        for j in range(len(m)):
            n[i][j] = "{0:0.5e}".format(m[i][j])
        n[i][len(m)] = "{0:0.5e}".format(b2[i])

    return n


def convert_string_to_list(string):
    res = f"[{string}]".strip(" ")
    res_to_json = json.loads(res)
    return res_to_json


def splain(x_str, y_str):

    x_list = convert_string_to_list(x_str)
    y_list = convert_string_to_list(y_str)

    x = np.array(x_list)
    y = np.array(y_list)
    nx =len(x)
    ny=len(y)
    if(nx==ny):

        if not checkUnique(x_list):
            return "", "",'X vector can\'t contain repeated values'

        dimension = 3*len(x) - 3

        matrix = np.zeros((dimension, dimension))

        m = (dimension-len(y))
        b = np.append(y, np.zeros(m))

        interpolation(x, matrix)
        continuity(x, matrix)
        smoothness(x, matrix)
        borderline(matrix)

        np.set_printoptions(formatter={'float': lambda x: "{0:0.5f}".format(x)})

        xact = np.linalg.solve(matrix, b)
        coefficients = []
        count = 0
        for i in range(0, len(matrix), 3):
            expr = f'a{count} = {float("{:.5f}".format(xact[i]))}, b{count} = {float("{:.5f}".format(xact[i+1]))}, c{count} = {float("{:.5f}".format(xact[i+2]))}'
            coefficients.append(expr)

        xv = sp.symbols('x')
        tracers = []
        for i in range(0, len(matrix), 3):
            expr = float("{:.5f}".format(xact[i]))*xv*xv + float(
                "{:.5f}".format(xact[i+1]))*xv + float("{:.5f}".format(xact[i+2]))
            tracer = [sp.latex(expr)]
            tracers.append(tracer)

        for i in range(len(x)-1):
            tracers[i].append(f'{x[i]} <= x <= {x[i+1]}')

        return tracers, coefficients, ""
    else:
        return "", "", f"The size must be the same {nx} != {ny}"


def interpolation(x, matrix):

    matrix[0][0] = pow(x[0], 2)
    matrix[0][1] = x[0]
    matrix[0][2] = 1

    xn = 1
    i = 0
    for j in range(1, len(x)):
        matrix[j][i] = pow(x[xn], 2)
        matrix[j][i+1] = x[xn]
        matrix[j][i+2] = 1
        i += 3
        xn += 1


def continuity(x, matrix):
    start = len(x)
    dimension = 2*len(x) - 2

    xn = 1
    i = 0
    for j in range(start, dimension):
        matrix[j][i] = pow(x[xn], 2)
        matrix[j][i+1] = x[xn]
        matrix[j][i+2] = 1
        matrix[j][i+3] = -pow(x[xn], 2)
        matrix[j][i+4] = -x[xn]
        matrix[j][i+5] = -1
        xn += 1
        i += 3


def smoothness(x, matrix):
    start = 2*len(x) - 2
    dimension = len(matrix) - 1

    xn = 1
    i = 0
    for j in range(start, dimension):
        matrix[j][i] = 2*x[xn]
        matrix[j][i+1] = 1
        matrix[j][i+3] = -2*x[xn]
        matrix[j][i+4] = -1
        xn += 1
        i += 3


def borderline(matrix):
    border = [2]
    m = len(matrix)-1
    b = np.append(border, np.zeros(m))
    matrix[m] = b

# print(splain(x,y))
