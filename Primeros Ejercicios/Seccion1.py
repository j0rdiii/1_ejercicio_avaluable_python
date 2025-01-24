#Ejercicio 1
print('Hola mundo')

#Ejercicio 2
numero1 = 5
numero2 = 8

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(suma, resta, multiplicacion, division)

#Ejercicio 3
numero_secreto = 6
adivinanza = int(input("Ingresa un numero: "))
if adivinanza < numero_secreto:
    print("Es mayor")
elif adivinanza > numero_secreto:
    print("Es menor")
else:
    print("Correcto")

#Ejercicio 4
lista = [4, 10, 520, 7]
lista.append(100)
lista.sort()
print(lista)

#Ejercicio 5
for numero in lista:
    print("Mi numero es un ", numero)