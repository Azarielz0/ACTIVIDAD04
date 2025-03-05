def es_palindromo_recursivo(palabra, inicio, fin):
    if inicio >= fin:  # Caso base: cuando los índices se cruzan o son iguales
        return True
    if palabra[inicio] != palabra[fin]:  # Si los caracteres no coinciden, no es palíndromo
        return False
    return es_palindromo_recursivo(palabra, inicio + 1, fin - 1)  # Llamada recursiva reduciendo los índices

def es_palindromoo(palabra):
    palabra = palabra.lower().replace(" ", "")  # Convertir a minúsculas y eliminar espacios
    return es_palindromo_recursivo(palabra, 0, len(palabra) - 1)  # Llamar a la función recursiva

# Pruebas
print(es_palindromoo("reconocer"))  # True
print(es_palindromoo("python"))     # False
print(es_palindromoo("Anita lava la tina"))  # True (ignora espacios y mayúsculas)
