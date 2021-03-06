import math
'''Descripción del código
Funciones
multiple_op(a): Recibe de parámetro un número.
Si no es un número devuelve un error y retorna falso.
En caso de si ser un número retorna un array de 3 elementos
con los siguientes valores : a*a, 2^a y a!
Verify_array_op(t): Recibe como parámetro un array de n elementos.
Este genera un array vacio de la cantidad
de elementos de dicho array. Revisa que todos los
elementos del array introducido sean numeros, en caso de
no serlos mediante el flag Bro se indica que un elemento no
es un número y retorna false. El flag bro
es inicializado en 0 y cambia a 1 en caso de error.
Si el flag bro se mantiene en 0, se genera un array de arrays
mediante el array ArraySalida'''


def multiple_op(a):
    if type(a) == int:
        b = a*a
        c = pow(2, a)
        d = math.factorial(a)
        Oarray = [b, c, d]
        for i in range(0, len(Oarray)):
            print(Oarray[i])
        # return 0 if pass
        return 0, Oarray
    else:
        # return 1 if fail
        return 1, 0


def verify_array_op(t):
    # lenghtVar = len(t) # No se usa
    ArraySalida = [None] * len(t)
    for i in range(0, len(t)):
        # if multiple_op fails
        if (multiple_op(t[i])[0]) == 1:
            # return 2 if fail
            return 2, 0
        else:
            ArraySalida[i] = multiple_op(t[i])[1]
    for i in range(0, len(ArraySalida)):
        print(ArraySalida[i])
    return 0, ArraySalida


# Uncomment following lines for testing
# t = [0,1,2]
# verify_array_op(t)
