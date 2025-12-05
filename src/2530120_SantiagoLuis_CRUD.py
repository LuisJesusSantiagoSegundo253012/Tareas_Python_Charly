print("\n CRUD \n")
# PORTADA
# Nombre: Santiago Segundo Luis Jesus
# Matrícula: 2530120
# Grupo: 1-2 IM

# RESUMEN EJECUTIVO
"""
El programa implementa un sistema CRUD completo para administrar 
artículos mediante un menú interactivo. 
Utiliza un diccionario principal donde cada elemento se 
almacena con un ID único y contiene nombre, precio y cantidad. 
A través del menú, el usuario puede crear nuevos registros con 
validación de datos, consultar artículos por ID, actualizarlos, 
eliminarlos o listar todos los elementos existentes. 
Cada operación está encapsulada en funciones que facilitan 
la organización del código y aseguran que las validaciones 
se apliquen correctamente. 
El programa funciona de forma cíclica hasta que el usuario decide salir.
"""

"""
Descripción:
Este programa implementa un sistema CRUD para administrar artículos en un inventario.
Permite crear, consultar, actualizar, eliminar y listar ítems almacenados en un diccionario,
donde cada artículo contiene nombre, precio y cantidad. El menú principal permite ejecutar
cada operación con validaciones de entrada para evitar datos incorrectos.

Entradas:
- Datos proporcionados por el usuario en cada operación (id, nombre, precio, cantidad).
- Opción del menú principal.

Salidas:
- Mensajes de confirmación o error según la operación.
- Información de ítems al consultarlos o listarlos.

Validaciones:
- Ningún id puede repetirse al crear un ítem.
- Precio y cantidad deben ser numéricos y mayores o iguales a 0.
- El id no puede estar vacío.
- Las opciones del menú deben ser válidas.
"""

# Estructura principal
items = {}  # Diccionario principal: id -> {name, price, quantity}

# -----------------------------
# Funciones CRUD
# -----------------------------

def create_item(data, item_id, name, price, quantity):
    if item_id in data:  # Validar id duplicado
        return False
    data[item_id] = {  # Crear nuevo elemento
        "name": name,
        "price": price,
        "quantity": quantity
    }
    return True

def read_item(data, item_id):
    if item_id in data:  # Validar existencia
        return data[item_id]
    return None  # Si no se encuentra

def update_item(data, item_id, new_name, new_price, new_quantity):
    if item_id not in data:  # Ítem inexistente
        return False
    data[item_id] = {  # Reemplazar valores
        "name": new_name,
        "price": new_price,
        "quantity": new_quantity
    }
    return True

def delete_item(data, item_id):
    if item_id in data:  # Validar existencia
        del data[item_id]  # Eliminar
        return True
    return False

def list_items(data):
    if len(data) == 0:  # No hay ítems
        print("No items found")
    else:
        for iid, info in data.items():  # Recorrer diccionario
            print(f"- ID: {iid}, Name: {info['name']}, Price: {info['price']}, Qty: {info['quantity']}")


# -----------------------------
# Menú principal
# -----------------------------

while True:
    print("\n---- CRUD Menu ----")
    print("1) Create item")
    print("2) Read item by id")
    print("3) Update item by id")
    print("4) Delete item by id")
    print("5) List all items")
    print("0) Exit")

    option = input("Choose an option: ")  # Leer opción

    if option not in ["0", "1", "2", "3", "4", "5"]:  # Validar entrada
        print("Error: invalid input")
        continue

    if option == "0":  # Salir
        print("Exiting program...")
        break

    # CREATE
    if option == "1":
        item_id = input("Enter id: ").strip()  # Leer id
        name = input("Enter name: ").strip()  # Leer nombre
        price_text = input("Enter price: ")  # Leer precio
        quantity_text = input("Enter quantity: ")  # Leer cantidad

        try:
            price = float(price_text)  # Convertir a número
            quantity = int(quantity_text)
        except:
            print("Error: invalid input")
            continue

        if item_id == "" or price < 0 or quantity < 0:  # Validaciones adicionales
            print("Error: invalid input")
            continue

        ok = create_item(items, item_id, name, price, quantity)  # Crear ítem
        if ok:
            print("Item created")
        else:
            print("Error: id already exists")

    # READ
    elif option == "2":
        item_id = input("Enter id: ").strip()  # Leer id
        if item_id == "":
            print("Error: invalid input")
            continue
        result = read_item(items, item_id)  # Buscar artículo
        if result is None:
            print("Item not found")
        else:
            print(result)

    # UPDATE
    elif option == "3":
        item_id = input("Enter id: ").strip()  # Leer id
        new_name = input("Enter new name: ").strip()  # Nuevo nombre
        new_price_text = input("Enter new price: ")  # Nuevo precio
        new_quantity_text = input("Enter new quantity: ")  # Nueva cantidad

        try:
            new_price = float(new_price_text)  # Convertir a float
            new_quantity = int(new_quantity_text)  # Convertir a entero
        except:
            print("Error: invalid input")
            continue

        if item_id == "" or new_price < 0 or new_quantity < 0:  # Validaciones
            print("Error: invalid input")
            continue

        ok = update_item(items, item_id, new_name, new_price, new_quantity)  # Actualizar
        if ok:
            print("Item updated")
        else:
            print("Item not found")

    # DELETE
    elif option == "4":
        item_id = input("Enter id: ").strip()  # Leer id
        if item_id == "":
            print("Error: invalid input")
            continue
        ok = delete_item(items, item_id)  # Eliminar
        if ok:
            print("Item deleted")
        else:
            print("Item not found")

    # LIST
    elif option == "5":
        print("Items list:")  # Mostrar lista
        list_items(items)


# Casos de prueba
# Normal:
#   1) Crear ítem con id="A1", name="Apple", price=10, qty=5 → "Item created"
#   2) Listar → Muestra correctamente el artículo
#
# Borde:
#   - Crear ítem con quantity=0 y price=0 → Permitido (valores no negativos)
#
# Error:
#   - Crear ítem con id vacío → Error: invalid input
#   - Crear ítem con id existente → Error: id already exists
#   - Consultar id inexistente → "Item not found"
#   - Precio no numérico → Error: invalid input

## Conclusion

"""
El uso de funciones simplificó la implementación 
del CRUD al separar cada operación en partes claras 
y reutilizables, lo que hizo el código más ordenado 
y fácil de mantener. Utilizar un diccionario o una 
lista de diccionarios resultó favorecido porque permite 
almacenar datos de forma estructurada y acceder a ellos 
rápidamente mediante claves. 
Durante la validación de entradas surgieron problemas 
como datos vacíos o tipos incorrectos, los cuales resolví 
agregando verificaciones y mensajes de error más claros.
"""

## Referencias

"""
Sin Rueda Tecnológica. (2024, 22 septiembre). 
¿Cómo hacer un CRUD(Guardar, Mostrar, Modificar y Eliminar) 
con Python y SQLite? FÁCIL Y SENCILLO [Vídeo]. 
YouTube. https://www.youtube.com/watch?v=LqApetk4YrU

Programadork100. (2021, 10 enero). como trabajar con un Crud en python 
[Vídeo]. YouTube. https://www.youtube.com/watch?v=7loe8sL3ANc

Cómo crear un CRUD en python. Parte 1: Estructura y clase. (s. f.). 
https://cosasdedevs.com/posts/como-crear-un-crud-en-python-parte-1-estructura-y-clase/

Acsany, P. (2024, 21 mayo). What are CRUD operations? 
https://realpython.com/crud-operations/
G, L. J. C. (s. f.). Aprende Frameworks de Desarrollo Web en Python. 
https://entrenamiento-frameworks-web-python.readthedocs.io/es/latest/leccion6/crud_app.html
"""

# Repositorio
# git@github.com:LuisJesusSantiagoSegundo253012/Tareas_Python_Charly.git