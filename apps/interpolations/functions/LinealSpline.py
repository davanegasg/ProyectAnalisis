import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from apps.interpolations.functions.convert_string_to_type import convert_string_to_list
import json


#ingreso
xi = "-1,0,3,4"
fi = "15.5,3,8,1"


def checkUnique(x):
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] == x[j] and i != j:
                return False
    return True


def lineal_spline(xi_str,yi_str):
  xi = np.array(convert_string_to_list(xi_str))
  fi = np.array(convert_string_to_list(yi_str))

  resultado = ""
  #procedimiento
  n = len(xi)
  ny = len(fi)

  if not checkUnique(xi):
            return (0, 'X vector can\'t contain repeated values')
  if(n==ny):
    x = sym.Symbol('x')
    px_table = []
    section = 1
    for section in range(1,n,1):
        numerator = fi[section]-fi[section-1]
        denominator = xi[section]-xi[section-1]
        m = numerator/denominator
        pxsection = fi[section-1]
        pxsection = m*(x-xi[section-1]) + pxsection 
        px_table.append(pxsection )

    #salida
    polinomio = []
    for section in range(1,n,1):
        pxsection = px_table[section-1]
        polinomio.append( str(pxsection))
        #print(pxsection)
    #print(px_table)
    return(polinomio,"")
  else:
    return(0,f"The size must be the same {n} != {ny}")




#GRAFICACION DEL EJERCICIO 
# -----------------------------------------------
# samples = 11
# xstreak = np.array([])
# ystreak = np.array([])
# for section in range(1,n,1):
#     a = xi[section-1]
#     b = xi[section]
#     xsection = np.linspace(a,b,samples)
#     pxsection = px_table[section-1]
#     pxt = sym.lambdify(x,pxsection)
#     ysection = pxt(xsection)
#     xstreak = np.concatenate((xstreak,xsection))
#     ystreak = np.concatenate((ystreak,ysection))

# plt.plot(xi,fi, 'ro', label='puntos')
# plt.plot(xstreak,ystreak, label='trazador')
# plt.show()
# -----------------------------------------------
