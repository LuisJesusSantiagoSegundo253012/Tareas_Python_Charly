print("\n Funciones\n")

# PORTADA
# Nombre: Santiago Segundo Luis Jesus
# Matrícula: 2530120
# Grupo: 1-2 IM

# RESUMEN EJECUTIVO
"""
Las funciones en programación permiten organizar 
el código en bloques reutilizables que realizan 
tareas específicas, haciendo los programas más 
claros, eficientes y fáciles de mantener. 
Al separar la lógica en funciones, se evita repetir código, 
se facilita la detección de errores y se mejora la estructura 
general del programa.
Además, las funciones pueden recibir datos mediante 
parámetros y devolver resultados, lo que permite crear 
soluciones más flexibles y modularizadas. 
En conjunto, usar funciones promueve buenas prácticas de 
diseño y una programación más ordenada y profesional.
"""

print("\n Problema 1: Rectangle area and perimeter")
# Problema 1.- Rectangle area and perimeter (basic functions)
"""
Descripción:
El programa calcula el área y el perímetro de un rectángulo usando dos funciones:
- calculate_area(): recibe ancho y altura y devuelve el área.
- calculate_perimeter(): recibe ancho y altura y devuelve el perímetro.
Primero se solicitan los valores width y height, se convierten a float 
y se validan.
Si son válidos, se llaman las funciones y se muestran los resultados.

Entradas:
- width (float): ancho del rectángulo.
- height (float): altura del rectángulo.

Salidas:
- "Area:" <valor_del_area>
- "Perimeter:" <valor_del_perimetro>

Validaciones:
- Ambos valores deben convertirse correctamente a float.
- width > 0 y height > 0.
"""

# Función que calcula el área
def calculate_area(width, height):
    return width * height  # área = base * altura

# Función que calcula el perímetro
def calculate_perimeter(width, height):
    return 2 * (width + height)  # perímetro = 2*(base + altura)


width_text = input("Enter width: ")   # Pedimos el ancho
height_text = input("Enter height: ") # Pedimos la altura

# Intentamos convertirlos a número
try:
    width = float(width_text)   # Conversión de ancho
    height = float(height_text) # Conversión de altura
except:
    print("Error: invalid input")  # Si falla la conversión
    exit()

# Validaciones
if width <= 0 or height <= 0:
    print("Error: invalid input")  # Rango inválido
else:
    area_value = calculate_area(width, height)  # Llamada a función del área
    perimeter_value = calculate_perimeter(width, height)  # Llamada a función del perímetro

    print("Area:", area_value)         # Mostrar área
    print("Perimeter:", perimeter_value)  # Mostrar perímetro

# Casos de prueba

# Normal:
# width=5, height=3 → Area: 15, Perimeter: 16

# Borde:
# width=0.5, height=0.5 → válido, calcula valores pequeños

# Error:
# width=-2, height=3 → "Error: invalid input"


print("\n Problema 2: Grade classifier")
# Problema 2.- Grade classifier (function with return string)

"""
Descripción:
Crea una función llamada classify_grade(score) que 
reciba una calificación numérica
y regrese una letra según su rango:
A (90-100), B (80-89), C (70-79), D (60-69) y F (<60).
El programa principal debe leer un valor, validarlo y mostrar la categoría.

Entradas:
- score (float; entre 0 y 100)

Salidas:
- "Score: <score>"
- "Category: <grade_letter>"

Validaciones:
- score debe poder convertirse a número.
- Debe estar en el rango 0-100. Si no, mostrar error.
"""

# Función que clasifica una calificación numérica
def classify_grade(score):
    if score >= 90:        # A partir de 90
        return "A"
    elif score >= 80:      # 80–89
        return "B"
    elif score >= 70:      # 70–79
        return "C"
    elif score >= 60:      # 60–69
        return "D"
    else:
        return "F"         # Menor a 60

score_text = input("Enter score (0-100): ")  # Se pide la calificación

try:
    score = float(score_text)  # Intentamos convertir
except:
    print("Error: invalid input")
    exit()

# Validamos rango
if score < 0 or score > 100:
    print("Error: invalid input")
else:
    grade_letter = classify_grade(score)  # Llamamos la función
    print("Score:", score)                # Mostramos valores
    print("Category:", grade_letter)

# Casos de prueba
# Normal: score = 95 → Category: A
# Borde: score = 15 → Category: F
# Error: score = 120 → Error: invalid input

print("\n Problema 3: List statistics function")
# Problema 3.- List statistics function (min, max, average)

"""
Descripción:
El programa recibe una lista de números escrita en }
una sola línea, separados por comas.
Después convierte cada valor a float, valida que todos 
sean números y utiliza la función
summarize_numbers() para calcular el mínimo, máximo y promedio de la lista.
Finalmente, muestra estos tres valores en pantalla.

Entradas:
- numbers_text (string con números separados por comas)

Salidas:
- "Min: <valor>"
- "Max: <valor>"
- "Average: <valor>"

Validaciones:
- La cadena no debe estar vacía después de aplicar strip().
- Cada elemento separado por comas debe poder convertirse a float.
- La lista resultante debe tener al menos un número.
"""

# Función que resume valores numéricos
def summarize_numbers(numbers_list):
    result = {}
    result["min"] = min(numbers_list) # Obtiene el valor mínimo
    result["max"] = max(numbers_list)  # Obtiene el valor máximo
    
    # Calcula promedio
    result["average"] = sum(numbers_list) / len(numbers_list) 
    return result

 # Entrada del usuario
numbers_text = input("Enter numbers separated by commas: ")

if numbers_text.strip() == "":  # Validación de cadena vacía
    print("Error: invalid input")
    exit()

parts = numbers_text.split(",") # Separar por comas
numbers_list = []  # Lista donde se guardarán números

for item in parts:
    item = item.strip()  # Limpieza de espacios
    try:
        num = float(item) # Intento de conversión a número
    except:
        print("Error: invalid input")   # Si falla, error
        exit()
    numbers_list.append(num)  # Agregar número válido a la lista

if len(numbers_list) == 0:   # Validación de lista vacía
    print("Error: invalid input")
    exit()

data = summarize_numbers(numbers_list)   # Llamada a la función

print("Min:", data["min"])     # Imprime el mínimo
print("Max:", data["max"])              # Imprime el máximo
print("Average:", data["average"])  # Imprime el promedio

# Casos de prueba
# Normal: "1, 2, 3, 4" → Min: 1, Max: 4, Average: 2.5
# Borde: "5" → Min: 5, Max: 5, Average: 5
# Error: "3, a, 5" → Error: invalid input

print("\n Problema 4: Apply discount list")
# Problema 4.- Apply discount list (pure function)

"""
Descripción:
El programa recibe una lista de precios separados por comas 
y una tasa de descuento.
Primero valida que todos los precios sean numéricos y 
mayores que cero, y que la tasa
de descuento esté dentro del rango 0 a 1.
 Luego utiliza la función apply_discount()
para generar una nueva lista con los precios rebajados.

Entradas:
- prices_text (string con precios separados por comas)
- discount_text (tasa de descuento entre 0 y 1)

Salidas:
- "Original prices: [...]"
- "Discounted prices: [...]"

Validaciones:
- La lista de precios no debe estar vacía.
- Cada precio debe poder convertirse a float y ser mayor que 0.
- La tasa de descuento debe ser un float entre 0 y 1.
"""

# Función que aplica un descuento a cada precio
def apply_discount(prices_list, discount_rate):
    discounted = []  # Lista donde se almacenan precios con descuento
    for price in prices_list:  # Recorrer cada precio
        discounted.append(price * (1 - discount_rate))  # Aplicar descuento
    return discounted  # Regresar la lista final

prices_text = input("Enter prices separated by commas: ")  # Entrada de precios
discount_text = input("Enter discount rate (0 to 1): ")  # Entrada del descuento

if prices_text.strip() == "":  # Validar cadena vacía
    print("Error: invalid input")
    exit()

parts = prices_text.split(",")  # Separar precios por coma
prices_list = []  # Lista para guardar precios válidos

for item in parts:
    item = item.strip()  # Eliminar espacios extra
    try:
        num = float(item)  # Convertir a número
    except:
        print("Error: invalid input")
        exit()
    if num <= 0:  # Validar que el precio sea mayor que 0
        print("Error: invalid input")
        exit()
    prices_list.append(num)  # Agregar precio válido a la lista

try:
    discount_rate = float(discount_text)  # Convertir tasa de descuento
except:
    print("Error: invalid input")
    exit()

if discount_rate < 0 or discount_rate > 1:  # Validar rango de descuento
    print("Error: invalid input")
    exit()

# Aplicar descuento
discounted_prices = apply_discount(prices_list, discount_rate)

print("Original prices:", prices_list)  # Mostrar lista original
print("Discounted prices:", discounted_prices)  # Mostrar lista con descuento

# Casos de prueba
# Normal: prices="100, 50, 30", discount="0.2" → [100,50,30] → [80,40,24]
# Borde: prices="10", discount="0" → [10] → [10]
# Error: prices="10, -5, 2" → Error: invalid input

print("\n Problema 5: Greeting function with default parameters")
# Problema 5.- Greeting function with default parameters

"""
Descripción:
El programa solicita un nombre y un título opcional. 
Primero verifica que el nombre no
esté vacío. Luego utiliza la función greet() 
para construir un mensaje de saludo que
combina el título (si existe) con el nombre ingresado. 
Finalmente imprime el saludo generado.

Entradas:
- name_text (nombre ingresado por el usuario)
- title_text (título opcional)

Salidas:
- "Greeting: <mensaje_generado>"

Validaciones:
- El nombre no debe estar vacío.
"""

# Función que construye el saludo
def greet(name, title=""):
    name = name.strip()  # Quitar espacios del nombre
    title = title.strip()  # Quitar espacios del título
    if title == "":  # Si no hay título
        full_name = name  # Usar solo nombre
    else:
        full_name = title + " " + name  # Combinar título y nombre
    return "Hello, " + full_name + "!"  # Regresar el saludo

name_text = input("Enter name: ")  # Solicitar nombre
title_text = input("Enter title (optional): ")  # Solicitar título opcional

if name_text.strip() == "":  # Validar nombre vacío
    print("Error: invalid input")
    exit()

greeting_message = greet(name_text, title=title_text)  # Generar saludo

print("Greeting:", greeting_message)  # Mostrar saludo final

# Casos de prueba
# Normal: name="Luis", title="Dr." → Greeting: Hello, Dr. Luis!
# Borde: name="  Flor  ", title="  " → Greeting: Hello, Flor!
# Error: name="   ", title="Lic." → Error: invalid input

print("\n Problema 6: Factorial function")
# Problema 6.- Factorial function (iterative or recursive)

"""
Descripción:
El programa calcula el factorial de un número entero utilizando la función factorial().
Primero valida que el usuario ingrese un número entero válido y que este se encuentre
en el rango permitido (0 a 20). Luego llama a la función para obtener el factorial y
muestra el resultado final.

Entradas:
- n_text (texto con el número ingresado por el usuario)

Salidas:
- "n: <valor>"
- "Factorial: <resultado>"

Validaciones:
- El valor debe convertirse correctamente a entero.
- Debe estar en el rango 0 a 20.
"""

# Función que calcula el factorial de un número
def factorial(n):
    result = 1  # Acumulador del factorial
    for i in range(1, n + 1):  # Recorrer desde 1 hasta n
        result = result * i  # Multiplicar acumulador por i
    return result  # Regresar factorial final

n_text = input("Enter n: ")  # Solicitar número al usuario

try:
    n = int(n_text)  # Convertir a entero
except:
    print("Error: invalid input")
    exit()

if n < 0 or n > 20:  # Validar rango
    print("Error: invalid input")
    exit()

fact_value = factorial(n)  # Calcular factorial

print("n:", n)  # Mostrar valor original
print("Factorial:", fact_value)  # Mostrar resultado

# Casos de prueba
# Normal: n="5" → Factorial = 120
# Borde: n="0" → Factorial = 1
# Error: n="-3" → Error: invalid input
# Error: n="25" → Error: invalid input


## Conclusion

"""
En conclusión, el uso de funciones facilita organizar 
el código en partes claras y reutilizables, evitando 
repeticiones innecesarias. 
Aprendí que devolver valores con return es más útil que 
solo imprimir, porque permite usar esos resultados en otros cálculos o procesos. 
Además, los parámetros y valores por defecto hacen 
el código más flexible y adaptable a distintas situaciones 
sin tener que reescribirlo.
"""

## Referencias

"""
BitBoss. (2024, 4 enero). 
APRENDE FUNCIONES en PYTHON: 
def, pass, sintaxis, None, return vs print, argumentos, scope y más [Vídeo]. 
YouTube. https://www.youtube.com/watch?v=9k91jETchkI

Commit That Line! (2020b, octubre 18). 
Las FUNCIONES en PYTHON | ¿Para qué sirven y cómo se usan? [Vídeo]. 
YouTube. https://www.youtube.com/watch?v=hLRoDs4wNCU

Code Hive. (2022, 21 julio). 
Funciones en Python | Parámetros y Return (Ejemplos) [Vídeo]. 
YouTube. https://www.youtube.com/watch?v=g78juF9pB_w

La Geekipedia De Ernesto. 
(2023, 20 diciembre). 
CURSO Fundamentos de Funciones en PYTHON (curso de programación) [Vídeo]. 
YouTube. https://www.youtube.com/watch?v=Db43XBXlk7c

Nikorasu Def. (2023b, abril 15). 
CURSO de Python (desde cero) visual studio code - Funciones y Clases #7 [Vídeo]. 
YouTube. https://www.youtube.com/watch?v=eVdoWDVgCIY
"""

# Repositorio
# git@github.com:LuisJesusSantiagoSegundo253012/Tareas_Python_Charly.git