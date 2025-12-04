print("\n Manejo de números y booleanos \n")
# PORTADA
# Nombre: Santiago Segundo Luis Jesus
# Matrícula: 2530120
# Grupo: 1-2 IM

# RESUMEN EJECUTIVO
"""
El manejo de números y booleanos en Python permite construir programas capaces 
de realizar cálculos precisos y tomar decisiones basadas en datos reales.
Los enteros y flotantes se combinan en operaciones como promedios, razones, 
medidas físicas o evaluaciones financieras, mientras que los booleanos 
surgen de comparaciones que activan condiciones mediante if, utilizando 
operadores lógicos como and, or y not.
Validar rangos, evitar divisiones entre cero y asegurar entradas numéricas 
correctas es esencial para obtener resultados confiables y evitar errores. 
Estos patrones aparecen en problemas cotidianos como cálculos de BMI, nóminas, 
descuentos, préstamos y análisis de riesgo, demostrando la importancia de 
integrar números y lógica booleana en el desarrollo de soluciones robustas 
y funcionales.
"""

print("\n Problema 1: Temperature converter and range flag")
# Problema 1.- Temperature converter and range flag

"""
Descripción:
Este programa solicita una temperatura en grados Celsius y valida que la entrada
pueda convertirse correctamente a número. Después convierte la temperatura a
Kelvin y Fahrenheit. También determina si la temperatura es considerada alta
según un límite predeterminado. Si la entrada es inválida o genera una temperatura
en Kelvin negativa, se muestra un mensaje de error.

Entradas:
- temp_c (float ingresado por el usuario).

Salidas:
- Temperature in Celsius
- Temperature in Kelvin
- Temperature in Fahrenheit
- High temperature: true/false

Validaciones:
- La entrada no debe estar vacía.
- Debe convertirse correctamente a float.
- La temperatura en Kelvin no debe ser negativa.
"""

try:
    # Intentamos convertir la entrada a float; si falla, la temperatura no es válida
    temp_c = float(input("Set your grade: "))
except Exception:
    # Error de conversión: entrada no numérica
    print("Error: Temperature not valid")
    exit()

# Convertimos de Celsius a Kelvin
temp_k = temp_c + 273.15

# Validamos que la temperatura en Kelvin no sea negativa
if temp_k < 0.0:
    print("Error: Temperature not valid")
else:
    # Convertimos Celsius a Fahrenheit
    temp_f = temp_c * 9/5 + 32

    # Evaluamos si es una temperatura alta (>= 30 °C)
    is_high_temperature = (temp_c >= 30.0)

    # Imprimimos todos los resultados
    print(f"Temperature in Celsius: {temp_c}°")
    print(f"Temperature in Kelvin: {temp_k}°")
    print(f"Temperature in Fahrenheit: {temp_f}°")
    print(f"High temperature: {is_high_temperature}")

# Casos de prueba:
# 1) Normal: Entrada → 25 Celsius, Kelvin 298.15, Fahrenheit 77
# 2) Borde: Entrada → -273.15 → -273.15 Celsius, Kelvin 0.0, Fahrenheit: -459.66999999999996
# 3) Error: Entrada → "abc" → Error: Temperature not valid

print("\n Problema 2: Work hours and overtime payment")

# Problema 2.- Work hours and overtime payment
"""
Descripción:
Este programa solicita al usuario las horas trabajadas durante el fin de semana
y la paga por hora. Primero valida que ambas entradas puedan convertirse a número.
Después asegura que las horas no sean negativas y que la paga por hora sea mayor
a cero. Calcula el pago regular hasta 40 horas y un pago adicional (overtime) a
1.5 veces la tarifa por cualquier hora extra. Finalmente muestra si hubo horas
extra y el total a recibir.

Entradas:
- hours_worked (float)
- hourly_rate (float)

Salidas:
- Regular pay
- Overtime pay
- Total pay
- Has overtime: true/false

Validaciones:
- Ambas entradas deben poder convertirse a float.
- hours_worked no puede ser negativo.
- hourly_rate debe ser mayor que cero.
"""

try:
    # Intentamos convertir ambas entradas a número
    hours_worked = float(input("How many hours do you work in the weekend? "))
    hourly_rate = float(input("How much they pay you per hour? "))
except:
    # Si no es posible convertir a float, entrada inválida
    print("Error: invalid input")
    exit()

# Validamos que las horas sean >= 0 y la tarifa > 0
if hours_worked < 0 or hourly_rate <= 0:
    print("Error: invalid input")
else:
    # Las primeras 40 horas se pagan normal
    regular_hours = min(hours_worked, 40)

    # Las horas por encima de 40 se consideran overtime
    overtime_hours = max(0, hours_worked - 40)

    # Cálculo del pago normal
    regular_pay = regular_hours * hourly_rate

    # Cálculo del pago overtime con factor 1.5
    overtime_pay = overtime_hours * hourly_rate * 1.5

    # Pago total sumando regular + overtime
    total_pay = regular_pay + overtime_pay

    # Bandera booleana que indica si hubo horas extra
    has_overtime = (hours_worked > 40)

    # Mostramos todos los resultados
    print(f"Regular pay: {regular_pay}")
    print(f"Overtime pay: {overtime_pay}")
    print(f"Total pay: {total_pay}")
    print(f"Has overtime: {has_overtime}")

# Casos de prueba:
# 1) normal:
# horas_worked = 45, hourly_rate = 10 → regular=400, 
# overtime=75, total=475, has_overtime=True

# 2) borde:
# horas_worked = 40, hourly_rate = 10 → regular=400, 
# overtime=0, total=400, has_overtime=False

# 3) error:
# horas_worked = -5, hourly_rate = 10 → Error: invalid input
    

print("\n Problema 3: Discount eligibility with booleans")
# Problema 3.- Discount eligibility with booleans

"""
problema 3
Descripción:
Este programa determina si una compra es elegible para descuento. Primero valida
que el total de compra sea un número válido y no negativo. Luego solicita dos
respuestas tipo YES/NO para saber si el usuario es estudiante o adulto mayor,
normalizando el texto a mayúsculas para hacer una comparación correcta. El
descuento se aplica si la persona es estudiante, adulto mayor o si la compra
supera los $1000. Finalmente calcula el total con o sin descuento según
corresponda y muestra los resultados.

Entradas:
- purchase_total (float): monto total de la compra.
- is_student_text (string): "YES" o "NO" indicando si es estudiante.
- is_senior_text (string): "YES" o "NO" indicando si es adulto mayor.

Salidas:
- "Discount eligible: <true/false>"
- "Final total: <valor>"

Validaciones:
- purchase_total debe convertirse a float y ser >= 0.
- is_student_text e is_senior_text deben ser "YES" o "NO" (se normalizan con .upper()).
"""

try:
    # Se intenta leer el total de compra y convertirlo a número
    purchase_total = float(input("Set your total purchase: "))
except:
    # Si la conversión falla, se marca error
    print("Error: invalid input")
    exit()

# Validación: el total no puede ser negativo
if purchase_total < 0:
    print("Error: invalid input")
    exit()

# Se leen las respuestas y se normalizan a mayúsculas
is_student_text = input("Are you a student? (YES|NO): ").upper()
is_senior_text = input("Are you a senior? (YES|NO): ").upper()

# Validación de respuestas permitidas
if is_student_text not in ["YES", "NO"] or is_senior_text not in ["YES", "NO"]:
    print("Error: invalid input")
    exit()

# Conversión a booleanos
is_student = (is_student_text == "YES")
is_senior = (is_senior_text == "YES")

# Lógica del descuento
discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
print(f"Discount eligible: {discount_eligible}")

# Aplicación del descuento si corresponde
if discount_eligible:
    final_total = purchase_total * 0.9   # 10% descuento
else:
    final_total = purchase_total

print(f"Final total: {final_total}")

# 1) normal:
# purchase_total = 1200, student=NO, senior=NO → eligible=True, final_total=1080

# 2) borde:
# purchase_total = 999.99, student=NO, senior=NO → eligible=False, 
# final_total=999.99

# 3) error:
# purchase_total = -50 → Error: invalid input

print("\n Problema 4: Basic statistics of three integers")
# Problema 4.- Basic statistics of three integers
"""
problema 4
Descripción:
Este programa solicita tres números enteros y realiza varios cálculos básicos:
la suma de los tres valores, su promedio, el valor máximo y mínimo entre ellos,
y un booleano indicando si todos son números pares. Primero valida que los tres
valores ingresados puedan convertirse correctamente a enteros. Finalmente muestra
todos los resultados en pantalla.

Entradas:
- n1 (int): primer número entero.
- n2 (int): segundo número entero.
- n3 (int): tercer número entero.

Salidas:
- "Sum: <valor>"
- "Average: <valor>"
- "Max: <valor>"
- "Min: <valor>"
- "All even: <true/false>"

Validaciones:
- Los tres valores deben poder convertirse a enteros.
"""

try:
    # Intentamos convertir cada entrada en un número entero
    n1 = int(input("Set your first number (n1): "))
    n2 = int(input("Set your second number (n2): "))
    n3 = int(input("Set your third number (n3): "))
except:
    # Si hay cualquier error en la conversión, se marca como entrada inválida
    print("Error: number not valid")
    exit()

# Cálculo de la suma
sum_value = n1 + n2 + n3

# Cálculo del promedio (float)
average_value = sum_value / 3

# Máximo y mínimo usando funciones integradas
max_value = max(n1, n2, n3)
min_value = min(n1, n2, n3)

# Booleano: True si todos son pares, False si al menos uno no lo es
all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

# Impresión de resultados
print(f"Sum: {sum_value}")
print(f"Average: {average_value}")
print(f"Max: {max_value}")
print(f"Min: {min_value}")
print(f"All even: {all_even}")

# 1) normal:
# n1=4, n2=8, n3=6 → Sum=18, Average=6.0, Max=8, Min=4, All even=True

# 2) borde:
# n1=5, n2=2, n3=8 → mezcla de pares e impares, All even=False

# 3) error:
# n1="hola", n2=5, n3=3 → Error: number not valid

print("\n Problema 5: Loan eligibility")
# Problema 5.- Loan eligibility (income and debt ratio)

"""
problema 5
Descripción:
Este programa solicita el ingreso mensual, la deuda mensual y el puntaje crediticio
de una persona. Primero intenta convertir cada entrada a su tipo correspondiente:
dos valores flotantes y un entero. Después valida que los valores ingresados tengan
sentido (ingreso mayor a cero, deuda no negativa y puntaje crediticio no negativo).
Luego calcula la razón deuda–ingreso dividiendo el total de deuda mensual entre
el ingreso mensual. Finalmente determina si la persona es elegible para crédito
verificando tres condiciones: ingreso mínimo de 8000, razón deuda–ingreso menor
o igual a 0.4 y puntaje crediticio de al menos 650.

Entradas:
- monthly_income (float): ingreso mensual.
- monthly_debt (float): deuda mensual.
- credit_score (int): puntaje crediticio.

Salidas:
- "Debt ratio: <valor>"
- "Eligible: <true/false>"

Validaciones:
- monthly_income debe ser mayor que 0.
- monthly_debt debe ser mayor o igual que 0.
- credit_score debe ser mayor o igual que 0.
"""

try:
    # Se solicita el ingreso mensual y se convierte a float
    monthly_income = float(input("Set your monthly income: "))
    # Se solicita la deuda mensual y se convierte a float
    monthly_debt = float(input("Set your monthly debt: "))
    # Se solicita el puntaje crediticio y se convierte a entero
    credit_score = int(input("Set your credit score: "))
except:
    # Si ocurre un error al convertir cualquier entrada, se notifica e interrumpe el programa
    print("Error: invalid input.")
    exit()

# Validaciones para evitar datos imposibles o incorrectos
if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
    print("Error: invalid input.")
    exit()

# Cálculo de la razón deuda–ingreso
debt_ratio = monthly_debt / monthly_income
print(f"Debt ratio: {debt_ratio}")

# Determinación de elegibilidad con base en tres criterios
eligible = (monthly_income >= 8000.0) and (debt_ratio <= 0.4) and (credit_score >= 650)
print(f"Eligible: {eligible}")

# 1) normal:
# monthly_income=9000, monthly_debt=2000, credit_score=700
# Debt ratio=0.222..., Eligible=True

# 2) borde:
# monthly_income=8000, monthly_debt=3200, credit_score=650
# Debt ratio=0.4, Eligible=True

# 3) error:
# monthly_income=-5000, monthly_debt=1000, credit_score=700
# Error: invalid input.

print("\n Problema 6: Body Mass Index and category flag")
# Problema 6.- Body Mass Index (BMI) and category flag

"""
problema 6
Descripción:
Este programa calcula el Índice de Masa Corporal (BMI) a partir del peso en kilogramos
y la estatura en metros ingresados por el usuario. Primero intenta convertir ambas
entradas a valores flotantes; si falla, se considera entrada inválida. Luego valida
que el peso y la estatura sean mayores que cero. Una vez validados, calcula el BMI
usando la fórmula peso / (estatura^2) y redondea el resultado a dos decimales.
Finalmente determina si la persona está bajo de peso, en rango normal o con sobrepeso
según los rangos estándar de BMI.

Entradas:
- weight_kg (float): peso en kilogramos.
- height_m (float): estatura en metros.

Salidas:
- "BMI: <valor_redondeado>"
- "Underweight: <true/false>"
- "Normal: <true/false>"
- "Overweight: <true/false>"

Validaciones:
- weight_kg > 0
- height_m > 0
"""

try:
    # Se pide el peso y se intenta convertir a número flotante
    weight_kg = float(input("Set your weight in KG: "))
    # Se pide la estatura y se intenta convertir a número flotante
    height_m = float(input("Set your height in m: "))
except:
    # Si alguna conversión falla, no se puede seguir
    print("Error: invalid input.")
    exit()

# Validación: peso y estatura deben ser mayores que cero
if weight_kg <= 0 or height_m <= 0:
    print("Error: invalid input.")
    exit()

# Cálculo del BMI usando la fórmula: peso / (estatura^2)
bmi = weight_kg / (height_m * height_m)

# Redondeo del BMI a dos decimales para una salida más clara
bmi_round = round(bmi, 2)
print(f"BMI: {bmi_round}")

# Clasificación según el valor del BMI
is_underweight = (bmi < 18.5)
print(f"Underweight: {is_underweight}")

is_normal = (18.5 <= bmi < 25)
print(f"Normal: {is_normal}")

is_overweight = (bmi >= 25)
print(f"Overweight: {is_overweight}")

# 1) normal:
# weight_kg=70, height_m=1.75 → BMI≈22.86, Underweight=False, Normal=True, Overweight=False

# 2) borde:
# weight_kg=50, height_m=1.70 → BMI≈17.30, Underweight=True, Normal=False, Overweight=False

# 3) error:
# weight_kg=-60, height_m=1.70 → Error: invalid input.


# CONCLUSIÓN
"""
En estos ejercicios se observa cómo los números enteros y flotantes se combinan 
para resolver problemas reales, permitiendo cálculos como promedios, razones,
porcentajes o índices. Las comparaciones generan valores booleanos que sirven
para activar decisiones mediante estructuras if, haciendo el programa flexible.
También se refuerza la importancia de validar rangos y evitar errores como 
divisiones entre cero o valores negativos imposibles. Además, el uso de and, or 
y not permite diseñar condiciones complejas que modelan reglas del mundo real.
Estos mismos patrones se aplican en programas de nómina, sistemas de descuentos,
análisis de crédito, cálculo de BMI y en muchos otros procesos numéricos.
"""

# Referencias
"""
BitBoss. (2023, 2 agosto). APRENDE TIPOS, VARIABLES y OPERADORES 
en PYTHON como NUNCA TE LO HAN EXPLICADO [Vídeo]. 
YouTube. https://www.youtube.com/watch?v=numQzIgpOo0

Aprende computación. (2021, 12 marzo). 
Python desde cero: 8️⃣ Números enteros (Integers) en Python [Vídeo]. 
YouTube. https://www.youtube.com/watch?v=td-y3drboV8

Computando Codigo. (2020, 24 enero). 
¿ Qué son los Booleanos en python? 
- (true, false, and, or, not) - 07 - Curso Python [Vídeo]. 
YouTube. https://www.youtube.com/watch?v=0wtQJX_YlGU

Código Espinoza - Automatiza tu Vida. (2025, 11 marzo). 
✅ Booleanos y Operadores Lógicos en Python 🚀 
| Curso Completo para Principiantes [Vídeo]. 
YouTube. https://www.youtube.com/watch?v=iLXQTqcqGVo

Aprende computación. (2021a, marzo 11). 
Variables Booleanas en Python 🐍🟢🔴
- Curso Python Desde Cero Gratis [Vídeo]. 
YouTube. https://www.youtube.com/watch?v=VJadt5X0uzE
"""
# Repositorio
# git@github.com:LuisJesusSantiagoSegundo253012/Tareas_Python_Charly.git