from tabulate import tabulate
import math

def secante(f, x0, x1, tol, maxIter, tError):
    headers=["ite","x","f(x)","Error"]
    table=[]
    if f(x0) == 0:
        print(f'El valor {x0} es raiz')
    else:
        ite = 0
        error = tol + 1
        den = f(x1) - f(x0)
        table.append([ite,x0, f(x0), error])
        ite += 1
        table.append([ite,x1, f(x1), error])
        while(error >= tol and f(x1) != 0 and den != 0 and ite < maxIter):
            x2 = x1 - f(x1)*(x1 - x0)/den

            if tError == 0:
                error = abs(x2 - x1)
            else:
                error = abs((x2 - x1)/x2)
            x0 = x1
            x1 = x2
            den = f(x1) - f(x0)
            ite += 1
            table.append([ite,x1, f(x1), format(error, ".1E")])

        print(tabulate(table, headers))
        if f(x1) == 0:
            print(f'El valor {x1} es raiz')
        elif error < tol:
            print(f'{x1} es raiz con tolerancia {format(tol, ".1E")} en iter {ite}')
        elif den == 0:
            print(f'Hay una posible raiz multiple')
        else:
            print(f'No llegamos en {ite}')

# f = lambda x: math.exp(-x) - x
# fi = lambda x: -math.exp(-x) - 1
f = lambda x: math.exp(-x) - (x**2)*math.cos(2*x-4) + 6*x + 3
f = lambda x: math.exp(-x) - x
f = lambda x: x**3 - x**2 - 2*x + 2 + math.sin(x-1)
f = lambda x: x - (3*x)/math.sqrt( x**2 + 9) - 10000/1000
secante(f, 1, 2, 0.00005, 100, 0)