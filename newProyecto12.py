"""
PROGRAMACION FUNCIONAL
Sanchez Hernandez Jose Eduardo
Santibañez Garcia Luis Diego
Hernandez Rosario Christian de Jesus
"""

import csv

def read_csv(name_file):
    with open(name_file) as csvfile:
        list_movies=[]
        movies = csv.reader(csvfile,delimiter=',')
        h=next(movies)
        for movie in movies:
            list_movies.append(tuple(movie))
        return tuple(list_movies)

#Funcion que recibe y retorna una tupla de tuplas donde se ordena "Year of Realease" de forma ASCENDENTE
def Movies1(tupla:tuple)->tuple:
    my_list = sorted(tupla, key = lambda x: x[1])
    return tuple(my_list)

#Funcion que recibe y retorna una tupla de tuplas donde se ordena "Duration(Mins)" de forma DESCENDENTE
def Movies2(tupla:tuple)->tuple:
    my_list = sorted(tupla, key = lambda x: int(x[4]), reverse=True)
    return tuple(my_list)

#Funcion que recibe y retorna una tupla de tuplas de todas las peliculas del genero 'Drama,Romance'
def Movies3(genero:str):
    def filtrar_genero(tupla:tuple)->tuple:
        my_list = [i for i in tupla if i[2]==genero]
        return tuple(my_list)
    return filtrar_genero

def Movies4(tupla:tuple):
    list1 = [i for i in tupla if float(i[3])>=9.0]
    list2 = [i for i in tupla if float(i[3])>=6.0 and float(i[3])<9.0]
    list3 = [i for i in tupla if float(i[3])<6.0]
    def agregar_recomendacion(palabra:str)->list:
        if palabra == 'Excelente':
            return list1
        if palabra == 'Buena':
            return list2
        if palabra == 'Mala':
            return list3
    return agregar_recomendacion


if __name__ == '__main__':
    my_tuple = read_csv('./movies.csv')

    #print(Movies1(my_tuple))

    #print(Movies2(my_tuple))

    #my_fun = Movies3('Drama,Romance')
    #print(my_fun(my_tuple))

    #my_fun = Movies4(my_tuple)
    #print(my_fun('Excelente'))
    #print(my_fun('Buena'))
    #print(my_fun('Mala'))
