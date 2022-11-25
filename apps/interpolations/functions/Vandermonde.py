import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from tabulate import tabulate

import json

def checkUnique(x):
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] == x[j] and i != j:
                return False
    return True


def convert_string_to_list(string):
    res = f"[{string}]".strip(" ")
    res_to_json = json.loads(res)
    return res_to_json


def vandermonde(xi_str, yi_str):
    result = ""
    result_table = ""
    result_coefficients = ""
    result_polynomial = ""
    
    xi = np.array(convert_string_to_list(xi_str))
    B = np.array(convert_string_to_list(yi_str))
    n = len(xi)
    ny = len(B)

    if(n==ny):
        if not checkUnique(xi):
            return{
            "result":'X vector can\'t contain repeated values',
            "result_table": '',
            "result_coefficients": '',
            "result_polynomial": ''
            }
        D = np.zeros(shape=(n, n), dtype=float)
        for i in range(0, n, 1):
            for j in range(0, n, 1):
                potencia = (n-1)-j
                D[i, j] = xi[i]**potencia

        coeficiente = np.linalg.solve(D, B)

        x = sym.Symbol('x')
        polinomio = 0
        for i in range(0, n, 1):
            potencia = (n-1)-i
            termino = coeficiente[i]*(x**potencia)
            polinomio = polinomio + termino

        
        result_table = tabulate(D, tablefmt="html")
        result_coefficients = f"Polynomial coefficients: <br> {coeficiente}"
        result_polynomial = f"Interpolation polynomial: <br> {polinomio}"
        result_error=""
        
        return {
            "result":result,
            "result_table": result_table,
            "result_coefficients": result_coefficients,
            "result_polynomial": result_polynomial,
        }
    else:
        return {
            "result":f"The size must be the same {n} != {ny}",
            "result_table": '',
            "result_coefficients": '',
            "result_polynomial": '',
        }
    

# GRAFICACION DEL EJERCICIO
# --------------------------------------------
# # px = sym.lambdify(x,polinomio)
# a = np.min(xi)
# b = np.max(xi)
# xin = np.linspace(a,b,muestras)
# yin = px(xin)
# plt.plot(xi,fi,'o', label='[xi,fi]')
# plt.plot(xin,yin, label='p(x)')
# plt.xlabel('xi')
# plt.ylabel('fi')
# plt.legend()
# plt.title(polinomio)
# plt.show()
# --------------------------------------------


#print(vandermonde(xi, fi))
