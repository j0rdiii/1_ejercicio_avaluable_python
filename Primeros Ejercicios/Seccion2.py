import re

#Ejercicio 1
cuadrados = [x**2 for x in range(10)]
print(cuadrados)

#Ejercicio 2
texto = "Contacto: jorlum14@gmail.com, jorlaxx21@gmail.com, akdfsflsjflsdkkfj,dfafa fasdf"
correos = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', texto)
print(correos)

#Ejercicio 3
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
fib = fibonacci()
for _ in range(10):
    print(next(fib))

#Ejercicio 5
try:
    with open('archivo_inexistente.txt', 'r') as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no se encontró.")