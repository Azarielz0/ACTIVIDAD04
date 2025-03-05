def es_palindromo_recursivo(palabra, inicio, fin):
    if inicio >= fin:  # Caso base: cuando los índices se cruzan o son iguales
        return True
    if palabra[inicio] != palabra[fin]:  # Si los caracteres no coinciden, no es palíndromo
        return False
    return es_palindromo_recursivo(palabra, inicio + 1, fin - 1)  # Llamada recursiva reduciendo los índices

<<<<<<< HEAD
def es_palindromoo(palabra):
=======
def es_palindrom(palabra):
>>>>>>> cdbeb80753039960a96297534c6dc094d1269aa3
    palabra = palabra.lower().replace(" ", "")  # Convertir a minúsculas y eliminar espacios
    return es_palindromo_recursivo(palabra, 0, len(palabra) - 1)  # Llamar a la función recursiva

# Pruebas
<<<<<<< HEAD
print(es_palindromoo("reconocer"))  # True
print(es_palindromoo("python"))     # False
print(es_palindromoo("Anita lava la tina"))  # True (ignora espacios y mayúsculas)
=======
print(es_palindrom("reconocer"))  # True
print(es_palindrom("python"))     # False
print(es_palindrom("Anita lava la tina"))  # True (ignora espacios y mayúsculas)
>>>>>>> cdbeb80753039960a96297534c6dc094d1269aa3
