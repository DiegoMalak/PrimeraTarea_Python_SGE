'''
Archivo que debes crear --> listas.py

Escribe un programa en Python que cree una lista NO protegida llamada mares1 con 6
posiciones (mediterraneo, cantabrico, baltico, adriatico, tirreno, egeo).
Crea otra lista llamada mares2 con 6 posiciones (rojo, muerto, caspio, negro, arabigo, sulu).
Se creará también una lista nueva llamada mares que tenga 12 posiciones que serán las 6
posiciones de mares 1 más las 6 posiciones de mares2.
El programa debe mostrar la siguiente información:

1. La longitud de la lista mares1.
2. Los valores de todas las posiciones de la lista mares1.
3. La longitud de la lista mares2.
4. Los valores de todas las posiciones de la lista mares2.
5. La longitud de la lista mares.
6. Los valores de todas las posiciones de la lista mares.
7. Los valores de las posiciones 1, 2 y 3 de la lista mares1.
8. El índice o posicion del mar 'egeo' en la lista mares1.
9. Los valores de las posiciones 4, 5 y 6 de la lista mares2.
10. El índice o posicion del mar 'caspio' en la lista mares2.
11. El índice o posicion del mar 'caspio' en la lista mares.
'''

# Creamos una lista con los mares1.
mares1 = ['mediterraneo', 'cantabrico', 'baltico', 'adriatico', 'tirreno', 'egeo']
# Creamos una lista con los mares2.
mares2 = ['rojo', 'muerto', 'caspio', 'negro', 'arabigo', 'sulu']
# Creamos una lista con los mares.
mares = mares1 + mares2

# 1. La longitud de la lista mares1.
print("La longitud de la lista mares1 es: ", len(mares1))
# 2. Los valores de todas las posiciones de la lista mares1.
print("Los valores de todas las posiciones de la lista mares1 son: ", mares1)
# 3. La longitud de la lista mares2.
print("La longitud de la lista mares2 es: ", len(mares2))
# 4. Los valores de todas las posiciones de la lista mares2.
print("Los valores de todas las posiciones de la lista mares2 son: ", mares2)
# 5. La longitud de la lista mares.
print("La longitud de la lista mares es: ", len(mares))
# 6. Los valores de todas las posiciones de la lista mares.
print("Los valores de todas las posiciones de la lista mares son: ", mares)
# 7. Los valores de las posiciones 1, 2 y 3 de la lista mares1.
print("Los valores de las posiciones 1, 2 y 3 de la lista mares1 son: ", mares1[0:3])
# 8. El índice o posicion del mar 'egeo' en la lista mares1.
print("El indice o posicion del mar 'egeo' en la lista mares1 es: ", mares1.index('egeo'))
# 9. Los valores de las posiciones 4, 5 y 6 de la lista mares2.
print("Los valores de las posiciones 4, 5 y 6 de la lista mares2 son: ", mares2[3:6])
# 10. El índice o posicion del mar 'caspio' en la lista mares2.
print("El indice o posicion del mar 'caspio' en la lista mares2 es: ", mares2.index('caspio'))
# 11. El índice o posicion del mar 'caspio' en la lista mares.
print("El indice o posicion del mar 'caspio' en la lista mares es: ", mares.index('caspio'))







