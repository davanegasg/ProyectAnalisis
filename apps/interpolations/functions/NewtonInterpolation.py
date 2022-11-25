import json
import numpy as np
from math import *
from sympy import Function
from tabulate import tabulate
from sympy.parsing.sympy_parser import parse_expr


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


def newton(xi_str, yi_str):
    
    #solution = ""
    solution_table = ""
    solution_divided_table = ""
    interpolating_polynomial = ""
    if (xi_str and yi_str) == "":
        return {
            #"solution":solution,
            "solution_table":solution_table,
            "solution_divided_table":solution_divided_table,
            "interpolating_polynomial":interpolating_polynomial
        }
    
    x = convert_string_to_list(xi_str)
    y = convert_string_to_list(yi_str)
    
    nx = len(x)
    ny = len(y)
        
    tabla = np.zeros((nx+1, nx+1))

    if not checkUnique(x):
            return{
            "solution_table":'X vector can\'t contain repeated values',
            "solution_divided_table":solution_divided_table,
            "interpolating_polynomial":interpolating_polynomial,
            "xi": 0,
            "yi": 0
            }

    if (nx == ny):
        for i in range(nx):
            tabla[i][0] = x[i]
            tabla[i][1] = y[i]

        res = polinomioNewton(tabla, nx)[0].tolist()
        for i in range(len(res)):
            res[i].pop(0)
        res.pop()
        #solution = np.array(res).tolist()
        solution_table = tabulate(tabla, headers=["xi", "yi", "First", "Second",
                                                  "Third", "Quarter", "Fifth", "Sixth", "Seventh"], tablefmt="html")
        solution_divided_table = f"Divided difference: <br/> {format(imprimirDDividida(tabla))}"
        interpolating_polynomial = f"Interpolating polynomial: <br/> {polinomioNewton(tabla, nx)[1]}"
        return {
            #"solution":solution,
            "solution_table":solution_table,
            "solution_divided_table":solution_divided_table,
            "interpolating_polynomial":interpolating_polynomial,
            "xi": x,
            "yi": y
        }

    else:
        return{
            "solution_table":f"The size must be the same {nx} != {ny}\n {x} != {y}",
            "solution_divided_table":solution_divided_table,
            "interpolating_polynomial":interpolating_polynomial,
            "xi": 0,
            "yi": 0
        }


def polinomioNewton(tabla, n):
    polinomio = "P(X) = " + str(tabla[0][1])
    for j in range(2, n+1):
        for i in range(j-1, n):
            tabla[i][j] = (tabla[i][j-1] - tabla[i-1][j-1]) / \
                (tabla[i][0] - tabla[i-j+1][0])
            if (i == j-1):
                polinomio += " + " + str(tabla[i][j])
                for i in range(0, i):
                    polinomio += "(x - " + str(tabla[i][0]) + ")"
    return tabla, polinomio


def imprimirDDividida(tabla):
    respuesta = ""
    for i in range(1, len(tabla)):
        respuesta = respuesta + " | " + str(tabla[i-1][i])
    return respuesta


# print(newton("", ""))
