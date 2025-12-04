# PORTADA
# Nombre: Santiago Segundo Luis Jesus
# Matrícula: 2530120
# Grupo: 1-2 IM

# RESUMEN EJECUTIVO

"""
Un string en Python es un tipo de dato inmutable utilizado para almacenar
texto. Al ser inmutables, cualquier modificación genera una nueva cadena.
Entre las operaciones más comunes están: concatenar, obtener longitud,
extraer subcadenas mediante slicing, buscar patrones y reemplazar texto.
Validar y normalizar la entrada (por ejemplo, correos, nombres o
contraseñas) es fundamental para evitar errores y asegurar consistencia.
Este documento contiene seis problemas relacionados con manipulación de
cadenas: su descripción, entradas, salidas, validaciones y casos de prueba,
además del código correspondiente haciendo uso correcto de métodos de
string.
"""

# Problema 1: Full name (name + initials)
print("\n Problem 1: Full name")

"""
Descripción:
El programa recibe el nombre completo de una persona en una sola cadena.
Primero normaliza el texto eliminando espacios extra y aplicando el
formato adecuado de mayúsculas/minúsculas. Después muestra el nombre en
Title Case y produce las iniciales formadas por cada palabra del nombre.
Entradas:
    - full_name (string; puede venir en mayúsculas, minúsculas o mezclado, con
     espacios extra).
Salidas:
    - "Formatted name: <Name In Title Case>"
    - "Initials: <X.X.X.>"
Validaciones:
    - full_name no debe estar vacío después de strip().
    - Debe contener al menos dos palabras.
    - No se aceptan cadenas que sean solo espacios.
"""

# Codigo
full_name = input("Enter your full name: ")

# Normalizar el texto
name = full_name.strip()

# Validar que no esté vacío
if name == "":
    print("Error: name cannot be empty.")
else:
    parts = name.split()  # Separa palabras quitando espacios extra

    # Validar que tenga al menos dos palabras
    if len(parts) < 2:
        print("Error: please enter at least first name and last name.")
    else:
        # Formatear en Title Case
        formatted_name = " ".join(p.capitalize() for p in parts)

        # Crear iniciales
        initials = ".".join(p[0].upper() for p in parts) + "."

        print("Formatted name:", formatted_name)
        print("Initials:", initials)
# Casos de prueba:
# 1) Normal: "Luis Jesus Santiago Segundo" → "Luis Jesus Santiago Segundo", "L.J.S.S."
# 2) Borde: " Andreu Gallegos " → "Andreu Gallegos", "A.G."
# 3) Error: "LuisJesus" → Error: please enter at least first name and last name

print("\n Problem 2: Simple email validator")
# Problema 2
"""
Descripción:
Este programa verifica si una cadena corresponde a un correo electrónico
con formato básico válido. Revisa que haya exactamente un '@', que después
de este exista al menos un punto y que no existan espacios en blanco.
Si es válido, también muestra el dominio (todo lo que sigue al '@').

Entradas:
        - email_text (string).
Salidas:
    - "Valid email: true" o "Valid email: false"
    - Si es válido: "Domain: <domain_part>"
Validaciones:
    - email_text no debe estar vacío tras strip().
    - Debe tener exactamente un '@'.
    - Debe tener al menos un punto después del '@'.
    - No debe contener espacios.
"""
# Codigo
email_text = input("Enter your email: ")
email = email_text.strip()
if email == "": 
    print("Valid email: false") # Se comprueba que no haya espacios en blanco
else:
        if email.count("@") != 1: # Contamos cuantos @ hay en el correo
            print("Valid email: false") # Si hay mas de un @ es falso
        else:
            
            local, domain = email.split("@", 1) # Separamos lo que esta atras del @ 
            # (Incluido el @) del correo

            # Especificamos que si el local y el dominio esta vacio
            # Entonces esta mal
            if local == "" or domain == "" or "." not in domain:
                print("Valid email: false")
            # Si el email no contiene un "." entinces tambien es invalido 
            else:
                # Si pasa todas las validaciones, esta bien hecho
                print("Valid email: true")
                print("Domain:", domain)

# Casos de prueba:
#   Normal: "2530120@upv.edu.mx" → válido: true → dominio: "upv.edu.mx"
#   Borde: "a@b.co" → valido: true → dominio: "b.co"
#   Error: "user@@mail.com" → valido: false 

print("\n Problem 3: Palindrome checker")
# Problema 3
"""
Descripcion:
Este programa determina si una frase es un palíndromo, es decir, si se lee
igual de izquierda a derecha y de derecha a izquierda. Para ello, ignora
espacios, mayúsculas y minúsculas. También puede mostrar la frase ya
normalizada para mayor claridad.

Entradas:
- phrase (string).

Salidas:
- "Is palindrome: true" o "Is palindrome: false"
- (Opcional) versión normalizada de la frase.

Validaciones:
- phrase no debe estar vacía después de strip().
- Tras remover espacios, debe tener al menos 3 caracteres para evaluar.
"""

phrase = input("Enter your phrase: ")
palindrome_phrase = phrase.strip()

# Validar que no esté vacía
if palindrome_phrase == "":
    print("Palindrome is: false")
else:
    # Quitar espacios internos y poner en minúsculas
    palindrome = palindrome_phrase.lower().replace(" ", "")

    # Validar la longitud mínima
    if len(palindrome) < 3:
        print("Palindrome is: false")
    else:
        # Invertir el texto
        reversed_text = palindrome[::-1]

        # Comparar original normalizado con el invertido
        if palindrome == reversed_text:
            print("Palindrome is: true")
        else:
            print("Palindrome is: false")
# Casos de prueba:
#   Normal: "Oxxo" → Palindrome is: true
#   Borde: "Hola mundo" → Palindorme is: false
#   Error: " " → Palindrome is: false

print("\n Problem 4: ")
# Problema 4
"""
Descripcion:
Este programa toma una oración, elimina espacios al principio y al final,
luego separa las palabras. Después muestra el número de palabras, la primera,
la última, la palabra más corta y la más larga, evaluadas por longitud.

Entradas:
- sentence (string).

Salidas:
- "Word count: <n>"
- "First word: <...>"
- "Last word: <...>"
- "Shortest word: <...>"
- "Longest word: <...>"

Validaciones:
- La oración no debe quedar vacía tras strip().
- Después de split(), debe haber al menos una palabra válida.
"""
sentence = input("Enter a sentence: ")

# Normalizar: quitar espacios al inicio y final
text = sentence.strip()

# Validar que no esté vacía
if text == "":
    print("Sentence is empty.")
else:
    # Separar las palabras por espacios
    words = text.split()

    # Validar que haya al menos una palabra
    if len(words) == 0:
        print("Sentence is invalid.")
    else:
        # Contar las palabras
        count = len(words)

        # Primera y última palabra
        first_word = words[0]
        last_word = words[-1]

        # Buscar palabra más corta y más larga
        shortest = min(words, key=len)
        longest = max(words, key=len)

        # Mostrar resultados
        print("Word count:", count)
        print("First word:", first_word)
        print("Last word:", last_word)
        print("Shortest word:", shortest)
        print("Longest word:", longest)

# Casos de prueba:
#   Normal: "hola mundo en python" → 4, hola, python, en, python
#   Borde: "   solo   " → 1, solo, solo, solo, solo
#   Error: " " → sentence is empty

print("\n Problema 5")
# Problema 5
"""
Descripcion:
Este programa clasifica una contraseña como weak, medium o strong según
criterios básicos de seguridad. Analiza longitud y presencia de distintos
tipos de caracteres: mayúsculas, minúsculas, dígitos y símbolos.

Reglas:
- Weak: longitud < 8 o contiene únicamente minúsculas o es demasiado simple.
- Medium: longitud >= 8 y tiene mezcla básica de letras o dígitos.
- Strong: longitud >= 8 y contiene al menos una mayúscula, una minúscula,
  un dígito y un símbolo no alfanumérico.

Entradas:
- password_input (string).

Salidas:
- "Password strength: weak"
- "Password strength: medium"
- "Password strength: strong"

Validaciones:
- No permitir contraseña vacía.
- Revisar longitud con len().
"""

password_input = input("Enter a password: ")

# Validar que no esté vacía
if password_input.strip() == "":
    print("Please, set a correct pasword")  # contraseña vacía se considera débil
else:
    password = password_input  # no quitamos espacios internos por si cuentan

    # Banderas para verificar contenido
    has_upper = False   # tiene mayúsculas
    has_lower = False   # tiene minúsculas
    has_digit = False   # tiene números
    has_symbol = False  # tiene símbolos

    # Recorrer carácter por carácter
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():  # no es letra ni número → símbolo
            has_symbol = True

    length = len(password)

    # Reglas:
    # Weak: longitud < 8 o falta casi todo (muy simple)
    if length < 8 or (has_lower and not has_upper and not has_digit and not has_symbol):
        print("Password strength: weak")

    # Strong: longitud >= 8 y tiene MAY, min, dígito y símbolo
    elif length >= 8 and has_upper and has_lower and has_digit and has_symbol:
        print("Password strength: strong")

    # Si no es weak ni strong → medium
    else:
        print("Password strength: medium")

# Casos de prueba:
#   Normal: "vida" → weak
#   Borde: "!234Abc5" → strong
#   Error: " " → Please, set a correct pasword

print("\n Problema 6")
"""
Descripcion:
Este programa genera una etiqueta de producto con el formato:
Product: <NAME> | Price: $<PRICE>
y debe garantizar que la cadena final tenga exactamente 30 caracteres.
Si es más corta, se rellena con espacios; si es más larga, se recorta.

Entradas:
- product_name (string).
- price_value (string o número convertible a string).

Salidas:
- "Label: <exactly 30 characters>"

Validaciones:
- product_name no debe quedar vacío tras strip().
- price_value debe convertirse a número positivo.
"""

# Pedir entradas
product_name = input("Enter product name: ")
price_value = input("Enter price: ")

# Normalizar nombre y validar que no esté vacío
name = product_name.strip()
if name == "":
    print('Error: product name cannot be empty.')
else:
    # Intentar convertir el precio a número positivo
    try:
        price_num = float(price_value)
        if price_num <= 0:
            raise ValueError("non-positive")
    except:
        print('Error: price must be a positive number.')
    else:
        # Formatear precio con 2 decimales (estándar)
        price_str = f"{price_num:.2f}"

        # Construir etiqueta base
        label_base = f"Product: {name} | Price: ${price_str}"

        # Asegurar que la etiqueta tenga exactamente 30 caracteres
        if len(label_base) < 30:
            label = label_base.ljust(30)   # rellenar con espacios al final
        else:
            label = label_base[:30]       # recortar a 30 caracteres

        # Mostrar la etiqueta entre comillas para ver espacios
        print('Label: "' + label + '"')

# Casos de prueba:
#   Normal: "Pan, 20" →  Label: "Product: Pan | Price: $20.00  "
#   Borde: "Pera, -1" → Error: price must be a positive number.
#   Error: "" → Error: product name cannot be empty.

## Conclusion

"""
El manejo de strings es fundamental para procesar correctamente 
entradas y salidas, ya que casi toda la información ingresada 
por el usuario llega como texto. Funciones como lower(), strip() y split() 
permiten limpiar, normalizar y dividir datos para analizarlos sin errores. 
Usar join() facilita reconstruir cadenas cuando se requiere
un formato específico. La normalización es indispensable para 
comparar valores sin que mayúsculas, espacios o variaciones 
afecten el resultado. Además, crear buenas validaciones evita 
datos basura y previene fallas en la ejecución. Finalmente,
trabajar con slices refuerza el entendimiento de que los strings son inmutables,
obligándonos a generar nuevas cadenas cada vez que aplicamos transformaciones.
"""
# Referencias
"""
Nikorasu Def. (2023, 9 abril). 
CURSO de Python (desde cero) visual studio code - 
Strings #3 [Vídeo]. YouTube. https://www.youtube.com/watch?v=Pr-9wkSJDJk

Programa Resuelto. (2020, 14 enero). Strings en Python 
| Introducción a las cadenas de texto en Python 
| CURSO DE PYTHON 2021 | #5 [Vídeo]. 
YouTube. https://www.youtube.com/watch?v=yT0jixU3M2c

La Geekipedia De Ernesto. (2019, 30 julio). 
Curso Python 3 desde cero #4 
| Manipulación de cadenas de caracteres (Strings) [Vídeo]. 
YouTube. https://www.youtube.com/watch?v=1CDE1pdVDGw

Aprende a Programar. (2023, 20 julio). 
✅ Curso Maestro de Python: Métodos para Cadenas de Texto en Python 
😎 #4 [Vídeo]. 
YouTube. https://www.youtube.com/watch?v=hcn4Zc1T43A

Byspel - Iván L. (2021, 15 septiembre). 
🔴 Variables de tipo String en Python 🐍 String Python tutorial 
| Buscar valor en String Python [Vídeo]. 
YouTube. https://www.youtube.com/watch?v=y11tDlvDtzk

"""