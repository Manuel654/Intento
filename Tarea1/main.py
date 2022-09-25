import csv
from person import Person
from shop import Shop 
from shop_rented import Rented

file = open('C:/Users/alfre/Desktop/POO/shops.csv')
reader = csv.reader(file)

#Acceder al local
def access():
    print('A que local desea acceder? ')
    i = 1
    for row in reader:
        print(i, row)
        i += 1

#Crear orden de arriendo
#def rent():

#Editar orden de arriendo
#def editar():
#Eliminar orden de arriendo
#def Eliminar():
#Ingresar info


def report():
    #Total de renta cobrada
    #Total de renta pagada
    #Lista de locales arrendados
    #Lista de locales de una categoria
    print('Choose a report: ')


def rent_list(): 
    for row in reader:
        print(row)


def search():
    for row in reader:
        print(row)

def leave():
    exit()
