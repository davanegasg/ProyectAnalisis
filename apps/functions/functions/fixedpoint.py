from math import *
from sympy import *
import numpy as np
from tabulate import tabulate

def g(g1, x):
    return eval(g1)  # evaluate the function


def f(f1, x):
    return eval(f1)


def fixed_point(g1, f1, x0, tol, itermax):
    try:
        iter = 0
        resultados = [[iter, x0,  g(g1, x0), f(f1, x0), "NA"]]
        while iter <= itermax:
            x1 = g(g1, x0)  # evaluate function in last point
            error = abs(f(f1, x0))
            x0 = x1
            iter += 1
            resultados.append([iter,x0,g(g1, x0), f(f1, x0), error])
            if error < tol:  # if we reach the desired tolerance stop
                return(tabulate(resultados, headers=["iteration", "Xi", "g(xi)", "f(x)", "error"], tablefmt="html", floatfmt=(".10f",".10f",".10f")))
        if iter > itermax:
            return(f"solution not found, iterations used: {iter}")

        return(tabulate(resultados, headers=["iteration", "Xi", "g(xi)", "f(x)", "error"], tablefmt="html", floatfmt=(".10f",".10f",".10f")))
    except Exception as e:
        return f"Sorry we have a problem with: {e}, please check the function"

#punto_fijo("log(pow(sin(x),2) + 1) - (1/2)", "log(pow(sin(x),2) + 1) - (1/2)", -0.5, 10**-7, 100)