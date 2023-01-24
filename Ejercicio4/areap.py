'''
Archivo que debes crear ➔ areap.py

Escribe un programa en Python que calcule el área y el perímetro de un rectángulo pidiendo al
usuario que introduzca la base y la altura del mismo (con decimales).
'''

# Pedimos al usuario que introduzca la base y la altura del rectángulo.
base = float(input("Introduce la base del rectángulo: "))
altura = float(input("Introduce la altura del rectángulo: "))

# Calculamos el área y el perímetro del rectángulo.
area = base * altura
perimetro = 2 * (base + altura)

# Mostramos el área y el perímetro del rectángulo.
print("El área del rectángulo es: ", area)
print("El perímetro del rectángulo es: ", perimetro)


