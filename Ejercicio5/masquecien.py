'''
Archivo que debes crear ➔ masquecien.py

Escribe un programa en Python que pida al usuario dos números.
Si la suma de ambos números es mayor que 100 se mostrará el resultado de la suma y el
mensaje: 'La suma supera la centena'. De lo contrario se mostrará el resultado de la suma y el
mensaje ‘el resultado de la suma no supera la centena’.
'''

# Pedimos al usuario que introduzca dos números.
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
# Calculamos la suma de los dos números.
suma = num1 + num2
# Si la suma es mayor que 100, mostramos el mensaje 'La suma supera la centena'.
# Si la suma es menor o igual que 100, mostramos el mensaje 'el resultado de la suma no supera la centena'.

if suma > 100:
    print("La suma supera la centena")
else:
    print("El resultado de la suma no supera la centena")




