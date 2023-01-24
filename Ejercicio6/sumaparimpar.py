'''
Archivo que debes crear ➔ sumaparimpar.py

Genera y muestra los números del 1 al 100 y calcula la suma de todos los números pares, por un
lado, y la suma de los números impares, por otro. Muestra los resultados
'''

# Creamos una lista con los números del 1 al 100.
numeros = [x for x in range(1, 101)]
# Creamos una lista vacía para guardar los números pares.
pares = []
# Creamos una lista vacía para guardar los números impares.
impares = []
# Creamos una variable para guardar la suma de los números pares.
sumapares = 0
# Creamos una variable para guardar la suma de los números impares.
sumaimpares = 0

# Recorremos la lista de números.
for num in numeros:
    # Si el número es par, lo añadimos a la lista de pares.
    if num % 2 == 0:
        pares.append(num)
        # Sumamos el número a la variable sumapares.
        sumapares += num
    # Si el número es impar, lo añadimos a la lista de impares.
    else:
        impares.append(num)
        # Sumamos el número a la variable sumaimpares.
        sumaimpares += num

# Mostramos la lista de números.
print('Esta es la lista de 100 numeros creada con un for en la lista:\n', numeros)
# Mostramos la lista de números pares y la suma de los números pares.
print("")
print('Esta es la lista final de numeros pares:\n', pares)
print('Este es el resltado de la suma de los numeros pares:\n', sumapares)
print("--------------------------------------------------------------------")
# Mostramos la lista de números impares y la suma de los números impares.
print('Esta es la lista final de numeros impares:\n', impares)
print('Este es el resltado de la suma de los numeros pares:\n', sumaimpares)




