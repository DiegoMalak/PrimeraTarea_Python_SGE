'''
Archivo que debes crear ➔ conversortemp.py

Escribe un programa en Python que convierta la temperatura dada en grados Fahrenheit, si se
indica que son grados Celsius, o en grados Celsius, si se indica que son grados Fahrenheit.
'''

# Pedimos al usuario que introduzca la temperatura y la unidad de medida.
temperatura = float(input("Introduce la temperatura: "))
unidad = input("Introduce la unidad de medida (F o C): ")

# Temperatura introducida.
print("Temperatura introducida: ", temperatura, unidad)

# Si la unidad es C (Celsius), convertimos la temperatura a Fahrenheit.
# Si la unidad es F (Fahrenheit), convertimos la temperatura a Celsius.
if unidad == "C":
    temperatura = temperatura * 9 / 5 + 32
    unidad = "F"
else:
    temperatura = (temperatura - 32) * 5 / 9
    unidad = "C"

# Mostramos la temperatura convertida.
print("La temperatura convertida es: ", temperatura, unidad)









