# ACTIVIDAD04

Documentación de los cambios realizados en el código de la calculadora

1. Validación de entradas del usuario
Cambio: Se añadió la función obtener_numero para validar que el usuario ingrese un número válido
    def obtener_numero(mensaje):
        while True:
            try:
                return float(input(mensaje))
            except ValueError:
                print("Por favor, ingresa un número válido.")

2. Manejo de errores en la división
Cambio: Se reemplazó el mensaje de error en la función division por una excepción ValueError
    def division(a, b):
        if b == 0:
            raise ValueError("Error: No se puede dividir entre cero.")
        return a / b

3. Bucle principal para múltiples operaciones
Cambio: Se añadió un bucle while True en la función main para permitir que el usuario realice varias operaciones sin salir del programa
    while True:
        mostrar_menu()
        operacion = input("Selecciona una operación (1/2/3/4/5): ")

        if operacion == '5':
            print("Saliendo de la calculadora...")
            break

4. Modularización del menú
Cambio: Se extrajo la lógica del menú a una función separada llamada mostrar_menu
    def mostrar_menu():
        print("\nCalculadora Simple")
        print("Operaciones disponibles:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

5. Mejoras en la interfaz de usuario
Cambio: Se añadieron mensajes más descriptivos y una pausa después de cada operación
    print("\n--- Calculadora Simple ---")
    print(f"\n✅ Resultado de la suma: {resultado}")
    input("\nPresiona Enter para continuar...")

6. Comentarios y documentación
Cambio: Se añadieron comentarios detallados en cada función y en partes clave del código
    def suma(a, b):
        """Realiza la suma de dos números."""
        return a + b

7. Manejo de operaciones no válidas
Cambio: Se añadió una validación para asegurar que el usuario seleccione una operación válida (1, 2, 3, 4 o 5)
    if operacion not in ['1', '2', '3', '4']:
        print("Operación no válida. Por favor, selecciona una opción válida.")
        continue
