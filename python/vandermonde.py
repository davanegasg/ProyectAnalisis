from ex_funciones import zero, ampliar
from gauss_pl import *

def vander_matrix(x):
    n = len(x)
    vander = zero(n)
    for j in range(n):
        for i in range(n):
            vander[i][j] = (x[i])**(n-1-j)
    return vander


def vandermonde(x, y):
    vander = vander_matrix(x)
    xy = ampliar(vander, y)
    eliminacion_gausiana(vander, y, len(vander))

X = [3,2,6,7]
Y = [5,6,7,1] 
vandermonde(X,Y)