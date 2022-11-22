import math
from tabulate import tabulate

def busqueda_incremental(funcion, xi, maxIter, deltaX):
    headers=["ite","x","f(x)"]
    table=[]
    if funcion(xi) == 0:
        print(f'{xi} es raiz')
    else: 
        xf = xi + deltaX
        ite = 0
        table.append([ite, xi, funcion(xi)])
        while(funcion(xi)*funcion(xf) > 0 and ite < maxIter):
            xi = xf
            xf = xi + deltaX
            ite += 1
            table.append([ite, xi, funcion(xi)])
        ite += 1
        table.append([ite, xf, funcion(xf)])
        print(tabulate(table, headers))
        if funcion(xi)*funcion(xf) == 0:
            print(f'{xf} es raiz')
            print(f'La iteración final fue {ite}')
        elif funcion(xi)*funcion(xf) < 0:
            print(f'Entre {xi} y {xf} hay una raiz')
            print(f'La iteración final fue {ite}')
        else:
            print(f'Maximo de iteraciones alcanzado ({ite})')
            print(f'xf: {xf}')

funcion = lambda x: 90*(x+40)*(x+27)*(x+95) - 50000000
# funcion = lambda x: math.exp(3*x - 12) + x*math.cos(3*x) - x**2 + 4
# busqueda_incremental(funcion, -3, 1000, 1)        
# f = lambda x: math.exp(-x) - (x**2)*math.cos(2*x-4) + 6*x + 3
# f = lambda x: x**3 - 7.51*x**2 + 18.4239*x - 14.8331
# busqueda_incremental(funcion, 0, 1000, 1)

# f = lambda x: x**3 - x**2 - 2*x + 2 + math.sin(x-1)
# busqueda_incremental(f, -0, 1000, -0.5)

f = lambda x: 1/x + 0.4 - 1.74*math.log(50*(x**1/2))

busqueda_incremental(f, 0.31, 1000, 0.001)

