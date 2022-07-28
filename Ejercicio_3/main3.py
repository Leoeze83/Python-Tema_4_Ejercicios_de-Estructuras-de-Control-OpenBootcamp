"""
Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.

"""
print("Programa que muestra el orden inverso de una lista de numeros. Luego de introducir el dato solicitado, presione Enter ")
print()
primer = int(input("Inicia en: "))
ultimo = int(input("Finaliza en: "))
listaOrdenada = [primer]

listaInversa = []


def crearLista2(primer, ultimo):
    i = primer
    while i < ultimo:
        i = i + 1
        listaOrdenada.append(i)
    print("Su lista de numeros es: ", listaOrdenada)


def listaInvertida(listaOrdenada):
    listaInversa = list(reversed(listaOrdenada))
    print("Su lista en orden inverso: ", listaInversa)


crearLista2(primer, ultimo)
listaInvertida(listaOrdenada)
