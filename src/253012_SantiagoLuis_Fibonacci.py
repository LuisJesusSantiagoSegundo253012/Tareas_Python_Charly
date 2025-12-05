print("\n Fibonacci Serie \n")
# PORTADA
# Nombre: Santiago Segundo Luis Jesus
# Matrícula: 2530120
# Grupo: 1-2 IM

# RESUMEN EJECUTIVO
"""
El código solicita al usuario la cantidad de términos que 
desea generar de la serie Fibonacci y valida que dicho valor 
sea un número entero entre 1 y 50. Si la entrada es correcta, 
el programa construye la secuencia empezando por 0 y 1, 
calculando cada nuevo término como la suma de los dos anteriores
hasta completar la cantidad solicitada. 
Si la entrada no es válida, muestra un mensaje de error. 
Este programa ilustra el uso de validación de datos, 
manejo de excepciones y generación iterativa de una secuencia numérica.
"""

"""
Descripción:
El programa genera una serie Fibonacci con la cantidad de 
términos indicada por el usuario.
Primero valida que la entrada sea un número entero y 
que esté dentro del rango permitido
(1 a 50). Luego construye la secuencia usando un ciclo while 
y muestra los términos en pantalla.

Entradas:
- n_input (texto con el número de términos solicitado)

Salidas:
- "Fibonacci series: <términos>"

Validaciones:
- El valor debe convertirse correctamente a entero.
- Debe estar entre 1 y 50.
"""

n_input = input("Enter the number of terms: ")  # Solicitar número de términos

try:
    n = int(n_input)  # Convertir a entero

    if n < 1 or n > 50:  # Validar rango permitido
        print("Error: Invalid input")
    else:
        print("Fibonacci series:", end=" ")  # Encabezado sin salto de línea

        a = 0  # Primer término de Fibonacci
        b = 1  # Segundo término

        if n == 1:
            print(a)  # Si solo se necesita un término
        else:
            print(a, b, end=" ")  # Imprimir los dos primeros términos
            count = 2  # Contador de términos ya mostrados

            while count < n:  # Generar siguientes términos
                c = a + b  # Siguiente número de la serie
                print(c, end=" ")  # Mostrar término
                a = b  # Avanzar valores
                b = c
                count += 1  # Aumentar contador
except Exception:
    print("Error: Invalid input")

# Casos de prueba
# Normal: n="7" → 0 1 1 2 3 5 8
# Borde: n="1" → 0
# Error: n="0" → Error: Invalid input
# Error: n="abc" → Error: Invalid input

## Conclusion

"""
El uso de un bucle facilitó generar la serie de 
manera ordenada y automática, sin tener que calcular 
cada valor manualmente. 
Manejar correctamente los casos especiales 
n = 1 y n = 2 es importante para evitar errores 
y asegurar que la serie inicie con valores válidos.
Además, esta misma lógica puede reutilizarse en 
otros programas que necesiten construir secuencias, 
realizar cálculos progresivos o generar datos basados en iteraciones.
"""

## Referencias

"""
Wrath of Math. (2022, 6 agosto). 
How to Program Fibonacci Sequence Recursively | Python for Math [Vídeo]. 
YouTube. https://www.youtube.com/watch?v=CsJ82I2I2Mo

Telusko. (2019, 13 marzo). 
#38 Python Tutorial for Beginners | Fibonacci Sequence [Vídeo]. 
YouTube. https://www.youtube.com/watch?v=7Sv4NmvdHcw

Coding with Lau. (2022, 18 octubre). 
PYTHON: Generar serie de Fibonacci de N numeros  - 2 formas [Vídeo]. 
YouTube. https://www.youtube.com/watch?v=ewleSsSN3YY

Coding with Lau. (2022b, octubre 18). 
PYTHON: Generar serie de Fibonacci de N numeros  - 2 formas [Vídeo]. 
YouTube. https://www.youtube.com/watch?v=ewleSsSN3YY
"""

# Repositorio
# git@github.com:LuisJesusSantiagoSegundo253012/Tareas_Python_Charly.git