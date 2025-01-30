class Llibre:
    def __init__(self, titol, autor, num_pag, en_prestec, estanteria, fila):
        self.titol = titol
        self.autor = autor
        self.num_pag = num_pag
        self.en_prestec = en_prestec
        self.estanteria = estanteria
        self.fila = fila

    # Define como se mostrará un libro cuando se crea
    # Se usa el operador ternario, para mostrar el estado del prestamo
    def __str__(self):
        return (f"Nom: {self.titol}, Autor: {self.autor}, Pàgines: {self.num_pag}, "
                f"En Préstec: {'Sí' if self.en_prestec else 'No'}, "
                f"Estanteria: {self.estanteria}, Fila: {self.fila}")


def mostrar_menu():
    print("\nInventari de la biblioteca CIFP PERE DE SON GALL")
    print(" === 1. Afegir un nou llibre a l'inventari")
    print(" === 2. Eliminar un llibre per títol")
    print(" === 3. Eliminar un llibre per estanteria i fila")
    print(" === 4. Mostrar llibre per títol")
    print(" === 5. Mostrar llibre per autor")
    print(" === 6. Mostrar tota la llista de llibres")
    print(" === 7. Sortir")


def afegir_llibre(inventari):
    titol = input("Títol del llibre: ")
    autor = input("Autor del llibre: ")
    num_pagines = int(input("Num pagines: "))
    en_prestec = input("En prestec (sí/no): ").strip().lower() == "sí"
    estanteria = input("Estanteria del llibre: ")
    fila = input("Fila del llibre: ")
    llibre = Llibre(titol, autor, num_pagines, en_prestec, estanteria, fila)
    inventari.append(llibre)
    print("Llibre afegir correctament.")


def eliminar_llibre_per_titol(inventari):
    nom = input("Nom del llibre: ")
    for llibre in inventari:
        if llibre.titol == nom:
            inventari.remove(llibre)
            print("Llibre eliminada correctamente.")
            return
    print("No s'ha trobat cap llibre amb aquest nom.")


def eliminar_llibre_estanteria_fila(inventari):
    estanteria = input("Estanteria: ")
    fila = input("Fila: ")
    for llibre in inventari:
        if llibre.estanteria == estanteria and llibre.fila == fila:
            inventari.remove(llibre)
            print("Llibre eliminar correctament")
            return
    print("No s'ha trobat cap llibre en aquesta estanteria.")


def mostrar_llibre_titol(inventari):
    nom = input("Títol del llibre: ")
    for llibre in inventari:
        if llibre.nom == nom:
            print(llibre)
            return
    print("No s'ha trobat cap llibre amb aquest nom.")


def mostrar_llibre_autor(inventari):
    autor = input("Nom del autor: ")
    llibres_autor = [llibre for llibre in inventari if llibre.autor == autor]
    if llibres_autor:
        for llibre in llibres_autor:
            print(llibre)
    else:
        print("No s'ha trobat cap llibre amb aquest nom d'autor.")


def mostrar_llista_llibres(inventari):
    if inventari:
        for llibre in inventari:
            print(llibre)
    else:
        print("No hi ha cap llibre afegit.")


def main():
    inventari = []
    while True:
        mostrar_menu()
        opcio = int(input("Escull una opció:"))
        if opcio == 1:
            afegir_llibre(inventari)
        elif opcio == 2:
            eliminar_llibre_per_titol(inventari)
        elif opcio == 3:
            eliminar_llibre_estanteria_fila(inventari)
        elif opcio == 4:
            mostrar_llibre_titol(inventari)
        elif opcio == 5:
            mostrar_llibre_autor(inventari)
        elif opcio == 6:
            mostrar_llista_llibres(inventari)
        elif opcio == 7:
            print("Sortint del programa..")
            break
        else:
            print("Opció no válida.")


if __name__ == "__main__":
    main()
