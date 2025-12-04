print("\n Manejo de Tuplas, listas y diccionarios\n")
# PORTADA
# Nombre: Santiago Segundo Luis Jesus
# Matrícula: 2530120
# Grupo: 1-2 IM

# RESUMEN EJECUTIVO
"""
El manejo de listas, tuplas y diccionarios en Python es fundamental para 
organizar y manipular conjuntos de datos de forma eficiente; las listas 
permiten almacenar múltiples valores que pueden cambiarse, agregarse o 
eliminarse gracias a su naturaleza mutable.
Mientras que las tuplas funcionan de manera similar pero son inmutables, 
lo que las hace ideales para información que no debe modificarse. 
Por otro lado, los diccionarios almacenan pares clave-valor que permiten 
acceder rápidamente a información asociada a una etiqueta, 
siendo una estructura flexible y muy utilizada para representar objetos, 
configuraciones o datos estructurados; dominar estas tres estructuras 
facilita la creación de programas más organizados, eficientes y fáciles 
de mantener dentro del desarrollo en Python.
"""

print("\n Problema 1: Shopping list basics")
# Problema 1.- Shopping list basics (list operations)

"""
problema 1
Descripción:
Este programa recibe una lista de elementos en una sola cadena separada por comas.
Primero elimina espacios innecesarios y convierte la entrada en una lista real.
Luego solicita un nuevo elemento para añadirlo y un elemento para buscar dentro
de la lista. Finalmente muestra la lista actualizada, la cantidad total de
elementos y si el elemento buscado existe. Si falta algún dato necesario, se
reporta un error.
Entradas:
- initial_items_text (string): lista inicial separada por comas.
- new_item (string): elemento a añadir.
- search_item (string): elemento a buscar.
Salidas:
- "Items list: [...]"
- "Total items: <n>"
- "Found item: <true/false>"
Validaciones:
- La lista inicial no puede estar vacía tras strip().
- new_item y search_item no pueden ser cadenas vacías.
"""

initial_items_text = input("Set your first list: ").strip()   # Leer lista inicial eliminando espacios externos

if initial_items_text != "":
    
    # Convertir la cadena separada por comas en lista real, limpiando espacios
    item_list = [x.strip() for x in initial_items_text.split(",")]
    print(f"Items list: {item_list}")

    new_item = input("Set your item to add in the list: ").strip()     # Elemento a agregar
    search_item = input("Set your item that you want to search: ").strip()  # Elemento a buscar

    # Validación de que ambos datos sean válidos
    if new_item != "" and search_item != "":
        
        item_list.append(new_item)     # Añadir nuevo elemento a la lista
        print(f"Items list: {item_list}")

        len_list = len(item_list)      # Número total de elementos
        print(f"Total items: {len_list}")

        found_item = (search_item in item_list)  # Booleano indicando si existe el elemento
        print(f"Found item: {found_item}")

    else:
        print("Item not valid")  # Error si alguno está vacío

else:
    print("Error: You must have at least 1 item")  # Error si la lista inicial está vacía



# Normal:
#   Entrada: "apple, banana, orange"
#   new_item: "grape"
#   search_item: "banana"
#   Salida esperada:
#       Items list: ['apple', 'banana', 'orange']
#       Items list: ['apple', 'banana', 'orange', 'grape']
#       Total items: 4
#       Found item: True

# Borde:
#   Entrada: "  dog  , cat "
#   new_item: "bird"
#   search_item: "lion"
#   Salida esperada:
#       Items list: ['dog', 'cat']
#       Items list: ['dog', 'cat', 'bird']
#       Total items: 3
#       Found item: False

# Error:
#   Entrada: ""
#   Salida esperada:
#       Error: You must have at least 1 item


print("\n Problema 2: Points and distances with tuples")
# Problema 2.- Points and distances with tuples

"""
Descripción:
Usa tuplas para representar dos puntos en un plano 2D: (x1, y1) y (x2, y2). El programa debe:
1) Crear dos tuplas point_a y point_b a partir de entradas numéricas.
2) Calcular la distancia euclidiana entre ambos puntos.
3) Crear una nueva tupla midpoint con el punto medio entre ellos.
Entradas:
- x1, y1, x2, y2 (float; coordenadas de los puntos).
Salidas:
- "Point A:" (x1, y1)
- "Point B:" (x2, y2)
- "Distance:" <distance>
- "Midpoint:" (mx, my)
Validaciones:
- Verificar que las 4 entradas se puedan convertir a float.
- No se requieren restricciones adicionales en el rango.
"""

try:
    x1 = float(input("Set x1: "))
    y1 = float(input("Set y1: "))
    x2 = float(input("Set x2: "))
    y2 = float(input("Set y2: "))
except:
    print("Error: invalid input")
    exit()

# Crear tuplas con las coordenadas
point_a = (x1, y1)
point_b = (x2, y2)

print(f"Point A: {point_a}")
print(f"Point B: {point_b}")

# Calcular distancia euclidiana
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(f"Distance: {distance}")

# Calcular punto medio
midpoint = ((x1 + x2)/2, (y1 + y2)/2)
print(f"Midpoint: {midpoint}")

# Casos de prueba:
# 1) Normal:
# x1=0, y1=0, x2=4, y2=3 → Distance=5, Midpoint=(2, 1.5)

# 2) Borde:
# x1=2.5, y1=2.5, x2=2.5, y2=2.5 → Distance=0, Midpoint=(2.5, 2.5)

# 3) Error:
# x1="hola", y1=3, x2=1, y2=2 → Error: invalid input

print("\n Problema 3: Product catalog with dictionary")
# Problema 3.- Product catalog with dictionary

"""
Descripción:
Este programa administra un diccionario llamado product_prices que contiene
productos y sus precios unitarios. El usuario ingresa un nombre de producto
y una cantidad. El programa:
1) Limpia y normaliza el nombre del producto.
2) Valida que la cantidad ingresada sea un número entero positivo.
3) Verifica si el producto existe en el diccionario.
4) Si existe, muestra su precio unitario, la cantidad y el precio total.
5) Si no existe, muestra un mensaje de error adecuado.

Entradas:
- product_name (string).
- quantity (int).

Salidas:
- Diccionario completo mostrado al inicio.
- "Unit price: <precio>"
- "Quantity: <cantidad>"
- "Total: <precio_total>"
- Mensajes de error cuando corresponda.

Validaciones:
- Validar que quantity pueda convertirse a entero.
- Validar que quantity > 0.
- Validar que el nombre del producto no esté vacío.
- Validar que el producto exista en product_prices.
"""

product_prices={ 
    "game boy": 125,
    "shield" : 92,
    "apple juice" : 12,
}
print(product_prices)  # Muestra el diccionario con los productos disponibles

product_name = input("Set your product name: ")
product_name_low = product_name.lower()  # Convierte a minúsculas
product_name_leng = (product_name_low.strip())  # Quita espacios innecesarios

try:
    quantity = int(input("Set your quantity for shop: "))  # Intenta convertir a entero
except Exception as err:
    quantity = -1  # Marca error asignando valor inválido

# Validación del nombre del producto
if product_name_leng == "":
    print("Error: Num not valid")
else:
    # Validación de la cantidad
    if quantity > 0:

        # Verifica que el producto exista en el diccionario
        if product_name_leng in product_prices:
            unit_price = product_prices[product_name_leng]  # Obtiene precio
            print(f"Unit price: {unit_price}")

            print(f"Quantity: {quantity}")

            total_price = unit_price * quantity  # Calcula total
            print(f"Total: {total_price}")

        else:
            print("Error: product not found")
    else:
        print("Error: Quantity not valid.")

# Casos de prueba

# Normal:
# Comprar 3 "game boy" → debe mostrar unit price 125 y total 375.

# Borde:
# Nombre con espacios: "   shield   " → debe reconocerlo como "shield".

# Error:
# quantity = "abc" → debe marcar "Error: Quantity not valid."

print ("\n Problema 4: Student grades with dict and list")
# Problema 4.- Student grades with dict and list

"""
Descripción:
El programa utiliza un diccionario llamado students donde cada clave es el
nombre de un estudiante y cada valor es una lista con sus calificaciones.
El usuario ingresa el nombre de un estudiante y el programa:
1) Normaliza ese nombre (mayúsculas y espacios).
2) Verifica si el estudiante existe en el diccionario.
3) Si existe, obtiene su lista de calificaciones.
4) Valida que el estudiante tenga calificaciones registradas.
5) Muestra la lista de calificaciones, calcula el promedio y determina
   si el estudiante aprueba (promedio >= 70.0).

Entradas:
- student_name (string).

Salidas:
- Lista de calificaciones del estudiante.
- "Average: <promedio>"
- "Passed: <True/False>"
- Mensajes de error según corresponda.

Validaciones:
- Validar que el nombre ingresado no esté vacío.
- Validar que el estudiante exista en el diccionario.
- Validar que el estudiante tenga al menos una calificación.
"""

students = {
    "FLOR": [70, 50, 100],     # Diccionario con estudiantes y sus calificaciones
    "CORAZON": [20, 50, 60],
    "ANDREU": [50, 40, 100],
}

print(students)  # Muestra todos los estudiantes disponibles

student_name = input("Set the name of the student: ").upper().strip()
# Convierte a mayúsculas y elimina espacios extras

if student_name == "":
    print("Error: student not valid")  # Valida que no sea cadena vacía
else:
    if student_name in students:
        grades = students[student_name]  # Obtiene lista de calificaciones

        if len(grades) == 0:
            print("Error: student has no grades")  # No tiene calificaciones
        else:
            print(f"Grades: {grades}")  # Muestra las calificaciones

            avg = sum(grades) / len(grades)  # Calcula promedio
            print(f"Average: {avg}")

            is_passed = avg >= 70.0  # Determina si aprobó
            print(f"Passed: {is_passed}")
    else:
        print("Error: student not found")  # Estudiante no existe

# Casos de prueba

# Normal:
# student_name = "FLOR" → Grades: [70, 50, 100], Average: 73.33, Passed: True

# Borde:
# student_name = "   corazon   " → Debe reconocerlo como "CORAZON"

# Error:
# student_name = "Pepe" → Error: student not found

    
print("\n Problema 5: Word frecuency counter (list+ dict)")
"""
problema X
Descripción:
El programa recibe una oración en una sola cadena. Primero normaliza el texto
convirtiéndolo a minúsculas y eliminando espacios extra al inicio y al final.
Luego:
1) Separa la oración en palabras usando split().
2) Construye un diccionario donde cada palabra es una clave y su valor es
   la cantidad de veces que aparece.
3) Imprime la lista de palabras.
4) Imprime el diccionario de frecuencias.
5) Identifica la palabra más repetida en la oración y la muestra al final.

Entradas:
- sentence (string; puede tener mayúsculas, minúsculas o espacios extra).

Salidas:
- "Words list: [...]"
- "Frequencies: {...}"
- "Most common word: <word>"

Validaciones:
- sentence no debe estar vacía después de strip().
- Debe contener al menos una palabra válida.
"""


sentence = input("Set your sentence: ").lower().strip()
# Convierte a minúsculas y elimina espacios extra

if sentence != "":
    words_list = sentence.split()              # Separa en palabras por espacio
    print(f"Words list: {words_list}")

    freq_dict = {}                             # Diccionario para contar palabras

    for word in words_list:
        if word:                               # Evita cadenas vacías
            freq_dict[word] = freq_dict.get(word, 0) + 1
            # get(word, 0) devuelve 0 si la palabra no existe aún

    print(f"Frequencies: {freq_dict}")

    if freq_dict:
        max_freq = max(freq_dict.items(), key=lambda item: item[1])
        # max() selecciona la palabra con mayor frecuencia

        most_common_word = max_freq[0]         # La palabra más común

        print(f"Most common word: {most_common_word}")
    else:
        print("Error: nothing to analyze")
else:
    print("Error: sentence not valid.")

# Casos de prueba

# Normal:
# sentence = "hello hello world" → Most common word: "hello"

# Borde:
# sentence = "   Python   python   PYTHON   " → Todas se vuelven "python"

# Error:
# sentence = "     " → Error: sentence not valid.


print("\n Problema 6: Simple contact book dictionary CRUD")
# Problema 6.- Simple contact book dictionary CRUD

"""
Descripción:
Implementa un mini "contact book" usando un diccionario donde:
- clave: nombre del contacto (string)
- valor: número telefónico (string).
El programa debe:
1) Crear un diccionario inicial con algunos contactos.
2) Leer una acción (ADD, SEARCH o DELETE).
3) Ejecutar la acción correspondiente:
   - ADD: solicitar nombre y teléfono, luego guardar o actualizar el contacto.
   - SEARCH: solicitar nombre y mostrar su teléfono si existe.
   - DELETE: solicitar nombre y eliminarlo si existe.
4) Mostrar mensajes indicando el resultado de cada operación.

Entradas:
- action_text (string; "ADD", "SEARCH" o "DELETE").
- name (string; depende de la acción).
- phone (string; solo en "ADD").

Salidas:
- ADD: "Contact saved: name, phone"
- SEARCH: "Phone: <phone>" o "Error: contact not found"
- DELETE: "Contact deleted:" name o "Error: contact not found"

Validaciones:
- action_text debe convertirse a mayúsculas y verificarse contra las opciones válidas.
- name no debe estar vacío después de strip().
- Para ADD: phone no debe estar vacío después de strip().
"""


contacts = { "ANDRUX": "8342736866", "LUIS": "8343549461" }
print(contacts)  # Se muestra la libreta inicial

accion_text = input("'ADD','SEARCH' or DELETE: ").upper()
# Se convierte a mayúsculas para comparación uniforme

if not (accion_text == "ADD" or accion_text == "SEARCH" or accion_text == "DELETE"):
    # Si la acción no es válida, se muestra error
    print("Error: menu not valid.")

elif accion_text == "ADD":
    name = input("Set the name of the contact: ").upper()  # Convertimos a mayúsculas
    phone = input(f"Set the phone number of {name}: ").strip()  # Limpieza mínima

    contacts[name] = phone   # Se guarda o actualiza el contacto
    print(f"Contact saved {name}, {phone}")
    print(contacts)

elif accion_text == "SEARCH":
    name = input("Set the name of the contact: ").upper()

    if name in contacts:  # Se verifica si existe
        print(name)
        phone = contacts[name]
        print(f"Phone: {phone}")
    else:
        print("Error: contact not found")

else:  # DELETE
    name = input("Set the name of the contact to delete: ").upper()

    if name in contacts:
        del_contact = contacts.pop(name)  # Elimina el contacto y devuelve el número
        print(f"Contact deleted: {name}")
        print(contacts)
    else:
        print("Error: contact not found.")

# Casos de prueba

# Normal:
# Acción: ADD, name="ANA", phone="1234567890"
# Resultado: Contact saved ANA, 1234567890

# Borde:
# Acción: SEARCH, name="  luis  " → se convierte a "LUIS" y sí existe

# Error:
# Acción: DELETE, name="PEDRO" → Error: contact not found


## Conclusion
"""
# Las listas convienen cuando necesitamos almacenar colecciones dinámicas de elementos,
# poder agregar, eliminar o reordenar fácilmente. Las tuplas son útiles cuando los
# datos deben permanecer inmutables, como coordenadas o puntos de referencia.
# Los diccionarios permiten búsquedas rápidas por clave, ideal para mapear nombres a
# valores o IDs a objetos. Combinando estructuras, como diccionarios de listas, se
# pueden representar relaciones más complejas, por ejemplo, estudiantes y sus notas.
# Usar la estructura adecuada según el caso mejora la claridad, eficiencia y seguridad
# del código. Además, normalizar y validar entradas sigue siendo fundamental al
# manipular estos tipos de datos.
"""

## Referencias

"""
Commit That Line! (2020, 30 septiembre). 
Listas, Tuples, Sets, Strings y Diccionarios en PYTHON [Vídeo].
YouTube. https://www.youtube.com/watch?v=CCUNuqqn7PQ

BitBoss. (2021, 1 junio). 
Estructuras de datos con Python en 8 minutos: 
Listas, Tuplas, Conjuntos y Diccionarios [Vídeo]. 
YouTube. https://www.youtube.com/watch?v=v25-m1LOUiU 
 
TecnoBinaria. (2020, 10 junio). QUÉ son las LISTAS en PYTHON? 
| Curso de Python Básico #12 [Vídeo]. 
YouTube. https://www.youtube.com/watch?v=lLLr34ZDEJ4

Sergio A. Castaño Giraldo. (2021, 2 junio). 
TUPLAS en Python Tutorial desde Cero 🤓  # 018 [Vídeo]. 
YouTube. https://www.youtube.com/watch?v=fqWj7WCOPsg
 
Sergio A. Castaño Giraldo. (2021b, junio 21). 
Diccionarios en Python Tutorial 📕 [Ejercicios] # 020 [Vídeo]. 
YouTube. https://www.youtube.com/watch?v=niGaBxyJCSs
"""




