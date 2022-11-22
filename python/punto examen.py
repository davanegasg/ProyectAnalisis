import math

def secreto(errores, valor_conocido, incognita):
    k = 0
    alpha = 0
    En = 0
    En1 = 0
    if (incognita == 0):    # Incognita es k
        alpha = valor_conocido
        for i in range(5 - 1):
            k = errores[i+1]/(errores[i]**alpha) + k
        print(f'La clave es {k / (5 - 1)}')
        return k / (5 - 1)
    else:                   # Incognita es alpha
        k = valor_conocido
        for i in range(5 - 1):
            alpha = math.log((errores[i+1])/k, errores[i]) + alpha
        print(f'La clave es {alpha / (5 - 1)}')
        


    
errores = [0.5, 0.3725, 0.2567, 0.1829, 0.1371]

secreto(errores, 1, 0)

secreto(errores, 0.7240555815334593, 1)

