from math import *
from sympy import diff
from tabulate import tabulate

def fun(function, x):
    try:
        eval_f = eval(f"{function}")
        return eval_f, function
    except Exception as e:
        return f"Syntax error, can not be evaluated {e}", f"Syntax error {e}"


def dfun(function, x):
    try:
        df = diff(fun(function, x)[1])
        eval_df = eval(f"{df}")
        return eval_df, df
    except Exception as e:
        return f"Syntax error, can not be evaluated: {e}", f"Syntax error {e}"

def d2fun(function, x):
    try:
        d2f = diff(dfun(function, x)[1])
        eval_d2f = eval(f"{d2f}")
        return eval_d2f, d2f
    except Exception as e:
        return f"Syntax error, can not be evaluated: {e}", f"Syntax error {e}"

def multipleroot(function, x0, tol, n):
    solution = ""
    solution_table = ""

    try:
        xant = x0
        fant = fun(function, xant)[0]
        e_abs = float("inf")
        iteration = 0
        results = [[iteration, xant, fun(function, xant)[0], ""]]
        dfunction = dfun(function, xant)[1]
        d2function = d2fun(function, xant)[1]

        while iteration <= n:
            if ((dfun(dfunction, xant)[0]) ** 2 - fant * d2fun(d2function, xant)[0]) == 0:
                solution = "Zero division"
                return solution, solution_table
            xact = xant - fant * dfun(dfunction, xant)[0] / (
                (dfun(dfunction, xant)[0]) ** 2 - fant * d2fun(d2function, xant)[0])

            fact = fun(function, xact)[0]
            e_abs = abs(xact-xant)
            iteration += 1
            xant = xact
            fant = fact
            results.append([iteration, xant, fun(function, xant)[0], e_abs])

            if e_abs < tol:
                solution = f"Solution found in X = {xact}, iterations:  {iteration-1}  error = {e_abs}"
                solution_table = tabulate(
                    results, headers=["iter", "Xi", "f(x)", "error"], tablefmt="html")
                break

        if iteration > n:
            solution = f"Solution not found for tolerance = {tol}"

        return solution, solution_table
    except Exception as e:
        solution = f"Sorry we have a problem with: {e}, please check the function"
        return solution, solution_table

# print(multipleroot("cos(x)",1,0.000007,100))
