import problema1
# Hasta ahora hemos trabajado con variable que permiten almacenar un unico valor

edad = 18
Altura = 1.71
nombre = "Daniel"
estado = True

# En python podemos utilizar una variable que permita almacerna varios tipos de datos

# Lista de enteros
lista1 = [10, 5, 3, 9]

# Lista de decimales
lista2 = [1.78, 1.23, 1.43, 1.45]

# Lista de string
lista3 = ["Lunes", "Martes", "Miercoles"]

# Lista de elemento de distintos tipos
lista4 = ["Daniel", 1.73, 18, True]

if __name__ == '__main__':
    # Cantidad de elementos que hay en una lista
    print(len(lista1))
    print(len(lista2))
    print(len(lista3))
    print(len(lista4))
    print()
    lista1[2] = 3
    print()
    print(lista1)
    print()
    problema1.sumar_5_enteros()


