'''
Archivo que debes crear ➔ modlistas.py

Escribe un programa en Python que modifique la lista mares siguiendo el orden siguiente:
1. Cambia a la vez los valores de los elementos undécimo y duodécimo de la lista mares por los
valores 'del norte' y 'alborán'. Muestra la lista mares
2. En la lista mares, inserta un elemento más con el valor 'báltico'. Muestra la lista mares
3. Borra el quinto elemento de la lista mares. Muestra la lista mares
4. Muestra la longitud de la lista mares
5. Muestra los valores repetidos en la lista mares usando el método correspondiente
6. Elimina el tercer elemento de la lista mares y guárdalo en la variable mar1
7. Elimina el último elemento de la lista mares y guárdalo en la variable mar2
8. Guarda el valor del noveno elemento en la variable mar3
9. Muestra los valores de las variables mar1, mar2 y mar3
10. Elimina el primer elemento de la lista mares con valor 'báltico'. Muestra la lista mares
11. Elimina todos los elementos de la lista mares
12. Ordena por orden alfabético de 'a' a 'z' los elementos de la lista mares1
13. Ordena por orden alfabético de 'z' a 'a' los elementos de la lista mares2

'''

# Creamos la lista mares.
print("")
print("**********************************************************************")
print("Creamos la lista mares")
mares = ['atlántico', 'pacífico', 'indico', 'antártico', 'ártico', 'mediterráneo', 'rojo',
         'caspio', 'adriático', 'golfo de mexico', 'golfo de california', 'golfo de fonseca', 'mar']
print(mares)
print("")
# 1. Cambia a la vez los valores de los elementos undécimo y duodécimo de la lista mares por
# los valores 'del norte' y 'alborán'. Muestra la lista mares
print("")
print("**********************************************************************")
print("1. Cambia los valores de la lista mares")
mares[10] = 'del norte'
mares[11] = 'alboran'
print(mares)
print("")

# 2. En la lista mares, inserta un elemento al final con el valor 'báltico'. Muestra la lista mares.
print("")
print("**********************************************************************")
print("2. Inserta un elemento más en la lista mares")
mares.append('baltico')
print(mares)
print("")

# 3. Borra el quinto elemento de la lista mares. Muestra la lista mares
print("")
print("**********************************************************************")
print("3. Borra el quinto elemento de la lista mares")
del mares[4]
print(mares)
print("")

# 4. Muestra la longitud de la lista mares
print("")
print("**********************************************************************")
print("4. Muestra la longitud de la lista mares")
print(len(mares))
print("")

# 5. Muestra los valores repetidos en la lista mares usando el método correspondiente.
print("")
print("**********************************************************************")
print("5. Muestra los valores repetidos en la lista mares")
print(mares.count('atlántico'))
print("")

# 6. Elimina el tercer elemento de la lista mares y guárdalo en la variable mar1.
print("")
print("**********************************************************************")
print("6. Elimina el tercer elemento de la lista mares y guárdalo en la variable mar1")
mar1 = mares.pop(2)
print(mar1)
print("")

# 7. Elimina el último elemento de la lista mares y guárdalo en la variable mar2.
print("")
print("**********************************************************************")
print("7. Elimina el último elemento de la lista mares y guárdalo en la variable mar2")
mar2 = mares.pop()
print(mar2)
print("")

# 8. Guarda el valor del noveno elemento en la variable mar3.
print("")
print("**********************************************************************")
print("8. Guarda el valor del noveno elemento en la variable mar3")
mar3 = mares[8]
print(mar3)
print("")

# 9. Muestra los valores de las variables mar1, mar2 y mar3.
print("")
print("**********************************************************************")
print("9. Muestra los valores de las variables mar1, mar2 y mar3")
print(mar1, mar2, mar3)
print("")

# 10. Elimina el primer elemento de la lista mares con valor 'báltico'. Muestra la lista mares.
print("")
print("**********************************************************************")
print("10. Elimina el elemento de la lista mares con valor 'báltico'")
print(mares)
#Sacamos la longitud de la lista mares.
longitud = len(mares)
borrar = longitud - 1
mares.pop(borrar)
print(mares)
print("")

# 11. Elimina todos los elementos de la lista mares.
print("")
print("**********************************************************************")
print("11. Elimina todos los elementos de la lista mares")
mares.clear()
print(mares)
print("")

# 12. Ordena por orden alfabético de 'a' a 'z' los elementos de la lista mares1.
print("")
print("**********************************************************************")
print("12. Ordena por orden alfabético de 'a' a 'z' los elementos de la lista mares1")
mares1 = ['atlántico', 'pacífico', 'indico', 'antártico', 'ártico', 'mediterráneo', 'rojo', 'caspio'
    , 'adriático', 'golfo de mexico', 'golfo de california']
mares1.sort()
print(mares1)
print("")

# 13. Ordena por orden alfabético de 'z' a 'a' los elementos de la lista mares2.
print("")
print("**********************************************************************")
print("13. Ordena por orden alfabético de 'z' a 'a' los elementos de la lista mares2")
mares2 = ['atlántico', 'pacífico', 'indico', 'antártico', 'ártico', 'mediterráneo', 'rojo', 'caspio',
          'adriático', 'golfo de mexico', 'golfo de california']
mares2.sort(reverse=True)
print(mares2)
print("")






