# calculadora.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Error: No se puede dividir entre cero.")
    return a / b

def obtener_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, ingresa un número válido.")

def mostrar_menu():
    print("\nCalculadora Simple")
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        operacion = input("Selecciona una operación (1/2/3/4/5): ")

        if operacion == '5':
            print("Saliendo de la calculadora...")
            break

        if operacion not in ['1', '2', '3', '4']:
            print("Operación no válida. Por favor, selecciona una opción válida.")
            continue

        num1 = obtener_numero("Ingresa el primer número: ")
        num2 = obtener_numero("Ingresa el segundo número: ")

        try:
            if operacion == '1':
                resultado = suma(num1, num2)
            elif operacion == '2':
                resultado = resta(num1, num2)
            elif operacion == '3':
                resultado = multiplicacion(num1, num2)
            elif operacion == '4':
                resultado = division(num1, num2)

            print(f"Resultado: {resultado}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()