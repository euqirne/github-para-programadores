#Para prueba GIT
# Iterar sobre diferentes estructuras de datos usando ciclos FOR
#Iterar sobre un string
# for letra in "Este es un texto nuevo":
#     print(letra)

#Iterar sobre una lista
# lenguajes = ['Python', 'Java', 'C++', 'JavaScript', 'PHP']
# for elemento in lenguajes:
#     print(elemento)

#Instrucciones para modificar el flujo del ciclo
#BREAK: haremos que el ciclo se rompa con la primera iteración
# lenguajes = ['Python', 'Java', 'C++', 'JavaScript', 'PHP']
# for elemento in lenguajes:
#     print(elemento)
#     break

#Romper el ciclo si el elemento actual es C++
# lenguajes = ['Python', 'Java', 'C++', 'JavaScript', 'PHP']
# for elemento in lenguajes:
#     print(elemento)
#     if elemento == 'C++':
#         break

#CONTINUE: pasar al siguiente elemento de la lista cuando se cumpla una condición (omitir elemento)
#lenguajes = ['Python', 'Java', 'C++', 'JavaScript', 'PHP']
# for elemento in lenguajes:
#     if elemento == 'C++':
#         continue
#     print(elemento)

# for elemento in lenguajes:
#     if elemento == 'C++' or elemento == 'PHP':
#         continue
#     print(elemento)

#Iterar sobre números consecutivos
# for numero in range(5):
#     print(numero)

#Si se quiere especificar el límite inferior y/o superior
# for numero in range(1, 6):
#     print(numero)

#Cambiar el valor de aumento del rango (por defecto es 1)
# for numero in range(1, 120, 2):
#     print(numero)

#Disminuir el valor, hacerlo en forma descendente
# for numero in reversed(range(1, 200)):
#     print(numero)

#Otra forma de iterar sobre listas
# lenguajes = ['Python', 'Java', 'C++', 'JavaScript', 'PHP']
# for index in range(len(lenguajes)):
#     print("Indice:", index)
#     print("Elemento:", lenguajes[index])

#Iterar sobre diccionarios
# lenguaje = {
#         "nombre": "Python",
#         "creador": "Guido Van Rossum"
#         }

#Imprimir llaves
# for elemento in lenguaje.keys():
#     print(elemento)

#Imprimir valores
# for elemento in lenguaje.values():
#     print(elemento)

#Imprimir llave + valor (como tupla)
# for elemento in lenguaje.items():
#     print(elemento)

#Imprimir llave + valor de forma separada (no en tupla)
# for llave, valor in lenguaje.items():
#     print(llave, valor)

#Ejercicios prácticos con FOR
#Ejercicio 1: Sumar todos los números de una lista
# números = [1, 2, 3, 4, 5]
# suma = 0
# for número in números:
#     suma += número
# print(f"La suma de los números es {suma}")

#Ejercicio 2: Encontrar el número más grande en una lista
# números = [10, 20, 30, 40, 60, 55]
# máximo = números[0]
# for número in números:
#     if número > máximo:
#         máximo = número
# print("El número más grande es {máximo}")

#Ejercicio 3: Contar las vocales en una cadena
# cadena = input('Ingrese una cadena de texto: ')
# vocales = 'aeiouAEIOU'
# contador = 0
# for letra in cadena:
#     if letra in vocales:
#         contador += 1
# print(f'Hay {contador} vocales en la cadena')

#Ejercicio 4: Imprimir una tabla de multiplicar
# número = 5
# for i in range(1, 11):
#     print(f"{número} x {i} = {número * i}")

#Ejercicio 5: Generar una lista de los primeros 10 números cuadrados
# cuadrados = []
# for i in range(1, 11):
#     cuadrados.append(i**2)
# print(cuadrados)

#Ejercicio 6: Invertir una cadena
# cadena = 'Python'
# cadena_invertida = ""
# for letra in cadena:
#     cadena_invertida = letra + cadena_invertida
# print(f"La cadena invertida es: {cadena_invertida}")

#Ejercicio 7: Filtrar números pares de una lista
números = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
for número in números:
    if número % 2 == 0:
        pares.append(número)
print(f"Números pares: {pares}")