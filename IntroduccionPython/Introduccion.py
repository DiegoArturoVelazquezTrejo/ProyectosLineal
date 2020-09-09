# Importamos la biblioteca con la que trabajaremos
import numpy as np

print("Hola Mundo!")

x = 3
y = 4
print(x+y,x*y)


A = np.array([[1,0,3], [0,1, -1]])

B = np.array([[4,1,0,-1],[5,-1,-8,0],[0,0,1,-2]])

# Imprimimos la matriz A
print(A)
# Imprimimos la matriz B
print(B)

# Multiplicaremos matrices

C = np.matmul(A, B)

#Imprimimos el resultado
print("La multiplicación de \n{}\n y \n{}\n es la matriz \n{}".format(A,B,C))

# Diego Arturo Velázquez Trejo 317227257
