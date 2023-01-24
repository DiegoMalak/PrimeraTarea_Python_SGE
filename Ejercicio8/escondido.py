'''
Archivo que debes crear ➔ escondido.py

Escribe un programa en Python que permita calcular el número que esconde. El usuario debe
averiguar qué número esconde el programa. Se pide números al usuario y se le informará de si
el número es más grande o es más pequeño que el número a averiguar. Si lo acierta, se le
informará con el mensaje correspondiente.

Muestra cuántas veces ha introducido un número erróneo el usuario hasta dar con el número
correcto. Una vez descubierto, si lo ha acertado en el primer intento, se mostrará el mensaje
“¡Enhorabuena! Lo has acertado a la primera”, si el número de veces es mayor que 3, se mostrará el
mensaje: “Por fin lo has acertado. Ha debido ser muy complicado para ti”. En otros casos, se mostrará el
mensaje: “Buen Trabajo! Lo has acertado”.
'''

# Pedimos al usuario que introduzca un número.
num = int(input("Introduce un número: "))
# Inicializamos el contador de intentos.
intentos = 1
# Inicializamos el número a averiguar.
num_a_averiguar = 5
# Mientras el número introducido no sea el número a averiguar, pedimos al usuario que introduzca otro número.
while num != num_a_averiguar:
    # Si el número introducido es mayor que el número a averiguar, mostramos el mensaje 'El número es más pequeño'.
    # Si el número introducido es menor que el número a averiguar, mostramos el mensaje 'El número es más grande'.
    if num > num_a_averiguar:
        print("El número es más pequeño")
    else:
        print("El número es más grande")
    # Pedimos al usuario que introduzca otro número.
    num = int(input("Introduce otro número: "))
    # Incrementamos el contador de intentos.
    intentos += 1
# Si el número de intentos es 1, mostramos el mensaje '¡Enhorabuena! Lo has acertado a la primera'.
# Si el número de intentos es mayor que 3, mostramos el mensaje
# 'Por fin lo has acertado. Ha debido ser muy complicado para ti'.
# En otros casos, mostramos el mensaje 'Buen Trabajo! Lo has acertado'.
if intentos == 1:
    print("¡Enhorabuena! Lo has acertado a la primera")
elif intentos > 3:
    print("Por fin lo has acertado. Ha debido ser muy complicado para ti")
else:
    print("Buen Trabajo! Lo has acertado")
# Mostramos el número de intentos.
print("Número de intentos: " + str(intentos))




