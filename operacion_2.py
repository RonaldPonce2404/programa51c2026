# Programa básico de suma y resta
# Autor: Raymer
# Descripción: Solicita dos números al usuario y muestra su suma y resta

def suma(a, b):
    """
    Esta función recibe dos números y retorna su suma.
    """
    return a + b


def resta(a, b):
    """
    Esta función recibe dos números y retorna su resta.
    """
    return a - b


# Entrada de datos
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Procesamiento
resultado_suma = suma(num1, num2)
resultado_resta = resta(num1, num2)

# Salida de resultados
print("La suma es:", resultado_suma)
print("La resta es:", resultado_resta)