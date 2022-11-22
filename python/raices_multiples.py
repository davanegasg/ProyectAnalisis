import math
from tabulate import tabulate

def raices_multiples(f, xi, tol, fi, fii, maxIter, tError):
    headers=["ite","x","f(x)","fi(x)", "fii(x)","Error"]
    table=[]
    if f(xi) == 0:
        print(f'El valor {xi} es raiz')
    else:
        ite = 0
        error = tol + 1
        table.append([ite,xi, f(xi), fi(xi), fii(xi), format(error, ".1E")])

        while(error >= tol and ite < maxIter):
            xn = xi - (f(xi)*fi(xi))/(((fi(xi))**2) - f(xi)*fii(xi))
            if tError == 0:
                error = abs(xn - xi)
            else:
                error = abs((xn - xi)/xn)
            ite += 1
            xi = xn
            table.append([ite,xi, f(xi), fi(xi), fii(xi), format(error, ".1E")])

        print(tabulate(table, headers))
        if error < tol:
            print(f'{xi} es raiz con tolerancia {format(tol, ".1E")} en iter {ite}')
        else:
            print('No llegamos')

# f = lambda x: math.exp(-x) - x
# fi = lambda x: -math.exp(-x) - 1
f = lambda x: math.exp(-x) - (x**2)*math.cos(2*x-4) + 6*x + 3
fi = lambda x: -math.exp(-x) - 2*x*math.cos(2*x-4) - 2*(x**2)*math.sin(2*x-4) + 6
fii = lambda x: math.exp(-x) - 4*(x**2)*math.cos(2*x-4) + 8*x*math.sin(2*x-4) - 2*math.cos(2*x-4)

f = lambda x: x*math.exp(x) - math.exp(x) + 1
fi = lambda x: x*math.exp(x)
fii = lambda x: x*math.exp(x) + math.exp(x)

f = lambda x: x**3 - x**2 - 2*x + 2 + math.sin(x-1)
fi = lambda x: 3*x**2 - 2*x - 2 + math.cos(x-1)
fii = lambda x: 6*x - 2 - math.sin(x-1)
raices_multiples(f, 0.5, 0.005, fi, fii, 1000, 1)