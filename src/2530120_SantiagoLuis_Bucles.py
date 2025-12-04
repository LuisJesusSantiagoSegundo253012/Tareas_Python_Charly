print("\nListas, tuplas y diccionarios")

# PORTADA
# Nombre: Santiago Segundo Luis Jesus
# Matrícula: 2530120
# Grupo: 1-2 IM

# RESUMEN EJECUTIVO
"""
Los bucles en programación permiten repetir acciones: 
el for se usa para recorrer secuencias como listas o cadenas. 
Mientras que el while se emplea cuando la cantidad de repeticiones 
depende de una condición, como en menús o lecturas con centinela. 
Los contadores incrementan un valor fijo en cada ciclo y los acumuladores 
suman valores variables. 
Es fundamental definir correctamente la condición de salida para evitar 
ciclos infinitos. Este enfoque incluye la planificación de 
entradas y salidas, validaciones y la elección adecuada de 
bucles según la tarea.
"""

print("\n Problema 1: sum of range with for")
# Problema 1.- sum of range with for
"""
Descripción:
El programa solicita un número entero n como límite superior y calcula:
1) La suma de todos los números del 1 hasta n.
2) La suma de todos los números pares dentro de ese rango.
Primero valida que la entrada pueda convertirse a entero y que sea mayor o 
igual a 1.
Luego recorre el rango utilizando un ciclo for y realiza los cálculos.
Entradas:
- n (int): límite superior del rango, mayor o igual a 1.
Salidas:
- "Sum 1..n: <total_sum>"
- "Sum of even numbers: <even_sum>"
Validaciones:
- n debe ser un número entero válido.
- n debe ser mayor o igual a 1.
"""

# Código comentado

try:
    # Intento de conversión a entero
    n = int(input("Set your superior limit range: "))
except:
    # Error si no es un entero
    print("Error: Number not valid, try again.")
    exit()

 # Error si el valor es menor que 1
if n < 1:
    print("Error: invalid input") 
else:
    total_sum = 0 # Inicializa suma total
    even_sum = 0  # Inicializa suma de pares

    for i in range(1, n + 1):   # Recorre del 1 hasta n
        total_sum += i   # Suma total
        if i % 2 == 0:    # Verifica si es par
            even_sum += i      # Suma de pares

    print(f"Sum 1..n: {total_sum}")    # Muestra suma total
    print(f"Sum of even numbers: {even_sum}")     # Muestra suma de pares

# Casos de prueba

# Normal:
# n = 5 → Sum 1..n: 15, Sum of even numbers: 6

# Borde:
# n = 1 → Sum 1..n: 1, Sum of even numbers: 0

# Error:
# n = -3 → Error: invalid input

print("\n Problema 2: Multiplicator table with for")
# Problema 2.- Multiplicator table with for

"""
Descripción:
El programa solicita un número entero "base" y un límite "m" para 
generar la tabla de multiplicar.
Valida que ambas entradas sean enteros válidos y que m sea mayor o igual a 1.
Luego utiliza un ciclo for para multiplicar la base por los números 
del 1 hasta m y muestra cada resultado.
Entradas:
- base (int): número del cual se desea la tabla de multiplicar.
- m (int): límite superior de la tabla (cantidad de multiplicaciones).
Salidas:
- "<base> x <i> = <resultado>" para cada i desde 1 hasta m.
Validaciones:
- base debe ser un número entero válido.
- m debe ser un número entero mayor o igual a 1.
"""

# Intento de convertir entradas a enteros
try:
    base = int(input("Set your base multiplication: ")) # Base de la tabla
    # Límite superior
    m = int(input("Set your limit digit to the multiplications: "))  
except:
    print("Error: Invalid input.")  # Error si no se puede convertir
    exit()

# Validación del límite
if m < 1:
    print("Error: Invalid input")  # Error si m < 1
    exit()

# Generación de la tabla de multiplicar
for i in range(1, m + 1):   # Recorre del 1 hasta m
    mult_num = base * i    # Calcula la multiplicación
    print(f"{base} x {i} = {mult_num}")         # Imprime resultado

# Casos de prueba

# Normal:
# base = 5, m = 10 → imprime 5 x 1 = 5, 5 x 2 = 10, ..., 5 x 10 = 50

# Borde:
# base = 3, m = 1 → imprime 3 x 1 = 3

# Error:
# base = "hola", m = 5 → Error: Invalid input

print("\n Problema 3: Average of numbers with while and sentinel")
# Problema 3.- Average of numbers with while and sentinel

"""
Descripción:
El programa permite al usuario ingresar números flotantes de manera 
repetida hasta que se ingresa un valor centinela (35.0).
Acumula la suma y la cantidad de números ingresados y calcula el 
promedio al final.
Valida que cada entrada sea un número flotante; si no lo es, 
solicita el dato nuevamente sin sumar ni contar.
Entradas:
- number (float): números que el usuario ingresa.
Salidas:
- "Count: <cantidad de números ingresados>"
- "Average: <promedio de los números ingresados>"
Validaciones:
- Verificar que cada entrada sea convertible a float.
- Controlar que si no se ingresa ningún número antes del centinela, 
se muestre un error y el promedio sea 0.
"""

# Valor centinela que detiene el ciclo
sentinel_value = 35.0
count = 0         # Contador de números válidos ingresados
total_sum = 0.0      # Suma acumulada

while True:
    try:
        # Intento de conversión a float
        number = float(input("Set the number: ")) 
    except:
        # Mensaje de error para entrada no numérica
        print("Invalid input, try again.")
        continue            

    if number == sentinel_value:
        # Se ingresó el valor centinela, finalizamos el ciclo
        if count == 0:
            print("Error: no data")  # No se ingresó ningún número válido
            average_value = 0.0
        else:
            average_value = total_sum / count # Cálculo del promedio
        print(f"Count: {count}")
        print(f"Average: {average_value}")
        break
    else:
        total_sum += number  # Acumulamos la suma
        count += 1     # Incrementamos contador

# Casos de prueba

# Normal:
# Entrada: 10, 20, 30, 35 → Count=3, Average=20.0

# Borde:
# Entrada: 35 → Error: no data, Average=0.0

# Error:
# Entrada: "hola", 10, 35 → Ignora "hola", Count=1, Average=10.0

print("\n Problema 4: Password attempts with while")
# Problema 4.- Password attempts with while
"""
Descripción:
El programa simula un sistema de login donde el usuario debe 
ingresar la contraseña correcta para acceder.
Permite un máximo de intentos definidos por MAX_ATTEMPTS. 
Cada intento incorrecto disminuye el número de intentos disponibles.
Si se alcanza el límite de intentos sin ingresar la contraseña 
correcta, se bloquea la cuenta.
Entradas:
- user_password (string): contraseña ingresada por el usuario.
Salidas:
- "Login success" si la contraseña es correcta.
- "Try again." y "Attempts left: <n>" para intentos incorrectos.
- "Account locked" si se exceden los intentos permitidos.
Validaciones:
- Comparación exacta de la contraseña ingresada con la almacenada.
- Control de número máximo de intentos.
"""

# Credenciales y configuración
USER = "Elwicho890"          # Nombre de usuario
PASSWORD = "Elwishin890"     # Contraseña correcta
MAX_ATTEMPTS = 5             # Máximo de intentos
attempts = 0                 # Contador de intentos

# Bucle principal de login
while attempts < MAX_ATTEMPTS:
    # Solicitar contraseña
    user_password = input(f"Set the password for {USER}: ")

    if user_password == PASSWORD:
        # Contraseña correcta
        print("Login success")
        break
    else:
        # Contraseña incorrecta
        attempts += 1
        print("Try again.")
        print(f"Attempts left: {MAX_ATTEMPTS - attempts}")

else:
    # Se ejecuta si el bucle termina sin break
    print("Account locked")

# Casos de prueba

# Normal:
# Entrada: "Elwishin890" → Login success

# Borde:
# Entrada: 4 intentos incorrectos + 1 correcto → Login success en último intento

# Error:
# Entrada: 5 intentos incorrectos → Account locked
        
print("\n Problema 5: Simple menu with while")
# Problema 5.- Simple menu with while

"""
EDescripción:
El programa implementa un menú interactivo utilizando un diccionario 
para las opciones.
Permite mostrar un saludo, consultar el valor actual de un contador, 
incrementarlo o salir del programa.
Cada opción está asociada a un número entero y se valida que la 
entrada del usuario sea correcta.
Entradas:
- option (int): número de la opción seleccionada por el usuario.
- confirm (string): confirmación de salida ("yes" o "no").
Salidas:
- "Hello!" si se elige opción 1.
- "Counter: <valor>" si se elige opción 2.
- "Counter incremented" si se elige opción 3.
- Mensajes de error si la opción no es válida.
- "Bye!" al salir del programa.
Validaciones:
- option debe ser un número entero que exista en el menú.
- confirm se normaliza a minúsculas y se valida.
"""

# Definición del menú usando diccionario
menu = {
    1: "Show greeting",
    2: "Show current counter value",
    3: "Increment counter",
    0: "Exit"
}

counter_value = 0  # Inicialización del contador

# Bucle principal del menú
while True:
    print("\nMenu:")
    for key, value in menu.items():
        print(f"{key}) {value}")  # Mostrar opciones disponibles

    try:
        # Entrada de opción
        option = int(input("Set the number where do you want to go: "))
    except:
        print("Error: invalid option")
        continue  # Volver al menú

    if option == 1:
        print("Hello!")  # Saludo
    elif option == 2:
        print(f"Counter: {counter_value}")  # Mostrar valor actual del contador
    elif option == 3:
        counter_value += 1  # Incrementar contador
        print("Counter incremented")
    elif option == 0:
        confirm = input("Are you sure you want to exit? [yes/no]: ").strip().lower()
        if confirm == "yes":
            print("Bye!")
            break  # Salir del bucle
        else:
            print("Cancelled")
    else:
        print("Error: invalid option")  # Opción no válida

# Casos de prueba

# Normal:
# option=1 → Muestra "Hello!"
# option=3 → Incrementa contador y muestra "Counter incremented"
# option=2 → Muestra "Counter: 1"

# Borde:
# option=0, confirm="no" → Muestra "Cancelled" y vuelve al menú

# Error:
# option=9 → Muestra "Error: invalid option"


print("\n Problema 6: Patter printing with nested loops")
# Problema 6.- Patter printing with nested loops

"""
Descripción:
El programa genera un patrón de asteriscos en dos fases: creciente y decreciente.
Primero solicita un número entero positivo n, luego imprime n líneas con 
asteriscos incrementando de 1 hasta n, y finalmente imprime el patrón invertido
de n hasta 1. Esto sirve para ilustrar el control de bucles y repetición de caracteres.
Entradas:
- n (int): número de asteriscos de la línea más larga.
Salidas:
- Patrón creciente de asteriscos.
- Patrón decreciente de asteriscos.
Validaciones:
- n debe ser un número entero mayor que 0.
"""

# Entrada del número de asteriscos
try:
    n = int(input("Set the number of asterisks: "))  # Convertir a entero
except:
    print("Error: invalid input.")  # Error si no es un entero
    exit()

if n < 1:
    print("Error: invalid input.")  # Validación de rango
else:
    # Patrón creciente
    for i in range(1, n + 1):
        print("*" * i)  # Repetición de asteriscos

    print()  # Línea en blanco opcional

    # Patrón decreciente
    for i in range(n, 0, -1):
        print("*" * i)  # Repetición de asteriscos

# Casos de prueba

# Normal:
# n=4 → imprime patrón creciente: 1*,2*,3*,4* y decreciente:4*,3*,2*,1*

# Borde:
# n=1 → imprime solo un asterisco en ambas fases

# Error:
# n=-3 → "Error: invalid input."


"""
En conclusión, comprender cuándo usar for y while, 
así como la función de contadores y acumuladores, es esencial 
para controlar la repetición de tareas de manera eficiente y segura, 
evitando errores como ciclos infinitos. Además, el uso de bucles 
anidados amplía las posibilidades de generar estructuras complejas, 
demostrando que dominar estas herramientas es clave para resolver 
problemas de programación de forma ordenada y efectiva.
"""

"""
References:
1) Python documentation - Learning_about_strings.py
2) Python web - https://docs.python.org/es/3/using/cmdline.html
3) Curso completo de python desde cero - https://www.youtube.com/watch?v=Kp4Mvapo5kc&t=1s
4) Curso de python para principiantes - https://www.youtube.com/watch?v=chPhlsHoEPo&t=775s
5) El tutorial de Python - https://docs.python.org/es/3/tutorial/
"""

# Repositorio
# git@github.com:LuisJesusSantiagoSegundo253012/Tareas_Python_Charly.git