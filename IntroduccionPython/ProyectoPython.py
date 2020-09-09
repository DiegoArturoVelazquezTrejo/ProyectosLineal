# Numpy y el ágebra lineal numérica
import numpy as np

A = np.array([[1, 0, 1, 0],
             [-1, 2, -1, 2],
             [3, 1, 3, 1],
             [0, -1, 0, -1]])
# Vamos a calcular la n-ésima potencia de una matriz
D = np.linalg.matrix_power(A, 20)

#Imprimimos el resultado de elevar a la 20 potenicia a A
print(D)

# Definimos la matriz B de la siguiente forma
B = np.array([[5, 4], [3, -5]])

# Para calcular el determinante de la matriz se realiza
print("El determinante de A es {}".format(np.linalg.det(A)))
print("El determinante de B es {}".format(np.linalg.det(B)))

# Notamos que el determinante de A es cero, eso quiere decir que la matriz no es
# Invertible, mientras que el determinante de B si es un número real distinto de cero,
# por lo que B es una matriz invertible, pero su determinante es -37 y tiene un 000000000000014

# Métodos Simbólicos
import sympy as sp

from sympy.printing.str import StrPrinter

printer = StrPrinter()

# Vamos a crear una matriz con sympy
A = sp.Matrix([[1, 0, 1, 0],
             [-1, 2, -1, 2],
             [3, 1, 3, 1],
             [0, -1, 0, -1]])

B = sp.Matrix([[5, 4], [3, -5]])

# Cálculos con matrices y sympy
A.det() # Determinante de A
A.rref() # Forma escalonada reducida FER
A.eigenvals() #Eigenvalores de A con multiplicidad
A.nullspace() #Da una base del núcleo de M

# Vamos a calcular los determinantes y mostrarlos
print("El determinante de A es {}".format(A.det()))
print("El determinante de B es {}".format(B.det()))

print("Forma escalonada reducida de A \n{}\n".format(A.rref()))
print("El rango  de A es 2 una vez que tiene dos variables pivote")


# Implementando la regla de Crammer

'''
Considérese el siguiente sistema de ecuaciones:

    −2x 1 + 6x 2 + 6x 3 + 8x 4 − 4x 5 = 6
    7x 1 − 2x 2 + 6x 3 + 4x 4 + 3x 5 = 14
    −4x 1 + 7x 2 + 5x 3 + 5x 4 + 6x 5 = 36
    5x 1 + 3x 2 − 4x 3 + 8x 4 + 2x 5 = 40
    6x 1 + 8x 2 + 6x 3 + x 4 + 9x 5 = 79

'''
# En el siguiente código se usan los métodos col_del y col_insert
C = sp.Matrix([[-2, 6, 6, 8, -4],
               [7, -2, 6, 4, 3],
               [-4, 7, 5, 5, 6],
               [5, 3, -4, 8, 2],
               [6, 8, 6, 1, 9]])

C1 = sp.Matrix([-2, 7, -4, 5, 6])
C2 = sp.Matrix([6, -2, 7, 3, 8])
C3 = sp.Matrix([6, 6, 5, -4, 6])
C4 = sp.Matrix([8, 4, 5, 8, 1])
C5 = sp.Matrix([-4, 3, 6, 2, 9])

b = sp.Matrix([6, 14, 36, 40, 79])

determinante_C = C.det()

# Vamos a calcular los xi utilizando el col insert
N = C.col_insert(0, b)
N.col_del(1)

x1 = N.det() / determinante_C
print("x1 = {}".format(x1))

# Vamos a calcular x2
N = C.col_insert(1, b)
N.col_del(2)

x2 = N.det() / determinante_C
print("x2 = {}".format(x2))

# Vamos a calcular x3
N = C.col_insert(2, b)
N.col_del(3)

x3 = N.det() / determinante_C
print("x3 = {}".format(x3))

# Vamos a calcular x4
N = C.col_insert(3, b)
N.col_del(4)

x4 = N.det() / determinante_C
print("x4 = {}".format(x4))

# Vamos a calcular x5
N = C.col_insert(4, b)
N.col_del(5)

x5 = N.det() / determinante_C
print("x5 = {}".format(x5))

# Python y Conjeturas Matemáticas
# Define términos iniciales de Tribonacci
a,b,c=0,0,1
# Se van a mostrar 15 términos
for j in range(15):
    print("El término {} de la sucesión de Tribonacci es {}".format(j,a))
    # Ahora cambiamos a,b,c de acuerdo a la recursión de Tribonacci
    a,b,c=b,c,a+b+c

T = sp.Matrix([[0,0,1], [1,0,1],[0,1,1]])

# Para conseguir la potencia de una matrix M**n
for i in range(8):
    print("T elevada a la {} es \n{}\n".format(i, (T**(i+1)).table(printer, rowsep=', \n')))

'''
    Conjetura:
    La sucesión de los números de Tribonacci, se define como sigue. Comienza
    con 0, 0, 1 y luego cada término es la suma de los tres anteriores. Sus primeros términos son:
                                0, 0, 1, 1, 2, 4, 7, 13, 24, . . . .
    Nótese que se obtienen las siguientes matrices:

    T elevada a la 0 es
    [0, 0, 1],
    [1, 0, 1],
    [0, 1, 1]

    T elevada a la 1 es
    [0, 1, 1],
    [0, 1, 2],
    [1, 1, 2]

    T elevada a la 2 es
    [1, 1, 2],
    [1, 2, 3],
    [1, 2, 4]

    T elevada a la 3 es
    [1, 2, 4],
    [2, 3, 6],
    [2, 4, 7]

    T elevada a la 4 es
    [2, 4,  7],
    [3, 6, 11],
    [4, 7, 13]

    T elevada a la 5 es
    [4,  7, 13],
    [6, 11, 20],
    [7, 13, 24]

    T elevada a la 6 es
    [ 7, 13, 24],
    [11, 20, 37],
    [13, 24, 44]

    T elevada a la 7 es
    [13, 24, 44],
    [20, 37, 68],
    [24, 44, 81]

    La sucesión de Tribonacci aparece en la primera fila de las matrices, en donde aparecen en tercias, y haciendo salto
    por salto, es decir:
    Sean a1, a2, a3, a4, a5, a6, a7 términos de la serie:

    a1 a2 a3 en la primera fila de la matriz elevada a la 1
    a3 a4 a5 en la primera fila de la matriz elevada a la 2
    a4 a5 a6 en la primera fila de la matriz elevada a la 3
    y así sucesivamente.

'''

# Diego Arturo Velázquez Trejo 317227257
