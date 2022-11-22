from tabulate import tabulate


def interceptoX(xi, xf, yi, yf):
    m = (yf - yi) / (xf - xi)
    #return (m*xi - f(xi))/m
    return xi - yi/m

def regla_falsa(xi, f, xf, tol, tError):
    headers=["ite","xi","f(xi)","xm","f(xm)","xf","f(xf)","Error"]
    table=[]
    ite = 0
    if f(xi)*f(xf) ==  0:
        if f(xi) == 0:
            print(f'xi: {xi} es raiz')
        else:
            print(f'xf: {xf} es raiz')
    elif f(xi)*f(xf) > 0: 
        print('Intervalo no valido')
    else:
        xm = interceptoX(xi, xf, f(xi), f(xf))
        error  = tol + 1
        ite = 0
        table.append([ite,xi, f(xi), xm, f(xm), xf, f(xf), format(error, ".1E")])

        while (error >= tol and f(xm) != 0):
            if f(xi)*f(xm) < 0:
                xf = xm
            else:
                xi = xm
            
            xm = interceptoX(xi, xf, f(xi), f(xf))
            if tError == 0:
                error = abs(xm - xi)
            else:
                error = abs((xm - xi)/xm)
            ite += 1
            table.append([ite,xi, f(xi), xm, f(xm), xf, f(xf), format(error, ".1E")])

        print(tabulate(table, headers))
        if f(xm) == 0:
            print(f'El valor {xm} es raiz en la iteracion {ite}')
        else: 
            print(f"El valor {xm} es raiz con tolerancia {format(tol, '.1E')} en la iteracion {ite}")
    

funcion = lambda x: x**3 - 7.51*x**2 + 18.4239*x - 14.8331
regla_falsa(3, funcion, 3.5, 0.00005, 0 )