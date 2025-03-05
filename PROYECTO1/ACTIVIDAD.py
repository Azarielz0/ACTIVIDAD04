# calculadora.py

# Funciones matemáticas básicas
def suma(a, b):
    """Realiza la suma de dos números."""
    return a + b

def resta(a, b):
    """Realiza la resta de dos números."""
    return a - b

def multiplicacion(a, b):
    """Realiza la multiplicación de dos números."""
    return a * b

def division(a, b):
    """Realiza la división de dos números."""
    if b == 0:
        raise ValueError("Error: No se puede dividir entre cero.")
    return a / b

def obtener_numero(mensaje):
    """
    Solicita al usuario un número y valida que sea un valor numérico válido.
    Si el usuario ingresa un valor no válido, se le pide que lo intente nuevamente.
    """
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("¡Error! Por favor, ingresa un número válido.")

def mostrar_menu():
    """
    Muestra el menú de la calculadora con las operaciones disponibles.
    """
    print("\n--- Calculadora Simple ---")
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

def main():
    """
    Función principal que maneja la lógica de la calculadora.
    Permite al usuario realizar múltiples operaciones hasta que decida salir.
    """
    while True:
        mostrar_menu()  # Mostrar el menú de opciones
        operacion = input("Selecciona una operación (1/2/3/4/5): ")

        # Salir del programa si el usuario elige la opción 5
        if operacion == '5':
            print("\n¡Gracias por usar la calculadora! ¡Hasta luego!")
            break

        # Validar que la operación seleccionada sea válida
        if operacion not in ['1', '2', '3', '4']:
            print("\n¡Operación no válida! Por favor, selecciona una opción del 1 al 5.")
            continue

        # Solicitar los números al usuario
        num1 = obtener_numero("Ingresa el primer número: ")
        num2 = obtener_numero("Ingresa el segundo número: ")

        try:
            # Realizar la operación seleccionada
            if operacion == '1':
                resultado = suma(num1, num2)
                print(f"\n✅ Resultado de la suma: {resultado}")
            elif operacion == '2':
                resultado = resta(num1, num2)
                print(f"\n✅ Resultado de la resta: {resultado}")
            elif operacion == '3':
                resultado = multiplicacion(num1, num2)
                print(f"\n✅ Resultado de la multiplicación: {resultado}")
            elif operacion == '4':
                resultado = division(num1, num2)
                print(f"\n✅ Resultado de la división: {resultado}")
        except ValueError as e:
            # Manejar errores, como la división entre cero
            print(f"\n❌ {e}")

        # Pausa antes de continuar
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()