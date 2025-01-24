class Llibre:
    def __init__(self, titol, autor, num_pag, en_prestec, estanteria, fila):
        self.titol = titol
        self.autor = autor
        self.num_pag = num_pag
        self.en_prestec = en_prestec
        self.estanteria = estanteria
        self.fila = fila

    def __str__(self):
        return(f"Nom: {self.titol}, Autor: {self.autor}, Pàgines: {self.num_pag}, "
               f"En Préstec: {'{Sí' if self.en_prestec else 'No'}, "
               f"Estanteria: {self.estanteria}, Fila: {self.fila}")

def mostrar_menu():
    print("\nInventari de la biblioteca CIFP PERE DE SON GALL")
    print("1. Afegir un nou llibre a l'inventari")
    print("2. Eliminar un llibre per títol")
    print("3. Eliminar un llibre per estanteria i fila")
    print("4. Mostrar llibre per títol")
    print("5. Mostrar llibre per autor")
    print("6. Mostrar tota la llista de llibres")
    print("7. Sortir")

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

def eliminar_llibre_titol(inventari):
    nom = input("Nom del llibre: ")
    for llibre in inventari:
        if llibre.titol == nom:
            inventari.remove(llibre)
            print("Llibre eliminada correctamente.")
            return
    print("No s'ha trobat cap llibre amb aquest nom.")

def eliminar_llibre_estanteria_fila(inventari):

def mostrar_llibre(inventari):

def mostrar_llibre_titol(inventari):

def mostrar_llibre_autor(inventari):

def mostrar_llista_llibres(inventari):

def sortir(inventari):

def main():
    inventari = []
    while True:
        mostrar_menu()
        opcio = int(input("Escull una opció:"))
        if opcio == 1:
            afegir_llibre(inventari)
        elif opcio == 2:
            eliminar_llibre_titol(inventari)
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