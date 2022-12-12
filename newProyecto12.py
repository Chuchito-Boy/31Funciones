"""
PROGRAMACION FUNCIONAL
Sanchez Hernandez Jose Eduardo
Santibañez Garcia Luis Diego
Hernandez Rosario Christian de Jesus
"""

import csv
from statistics import mean

def read_csv(name_file):
    with open(name_file) as csvfile:
        list_movies=[]
        movies = csv.reader(csvfile,delimiter=',')
        h=next(movies)
        for movie in movies:
            list_movies.append(tuple(movie))
        return tuple(list_movies)

# Funcion que recibe y retorna una tupla de tuplas donde se ordena "Year of Realease" de forma ASCENDENTE
def Movies1(tupla:tuple)->tuple:
    my_list = sorted(tupla, key = lambda x: x[1])
    return tuple(my_list)

# Funcion que recibe y retorna una tupla de tuplas donde se ordena "Duration(Mins)" de forma DESCENDENTE
def Movies2(tupla:tuple)->tuple:
    my_list = sorted(tupla, key = lambda x: int(x[4]), reverse=True)
    return tuple(my_list)

# Funcion que recibe y retorna una tupla de tuplas de todas las peliculas del genero 'Drama,Romance'
def Movies3(genero:str):
    def filtrar_genero(tupla:tuple)->tuple:
        my_list = [i for i in tupla if i[2]==genero]
        return tuple(my_list)
    return filtrar_genero

"""
Funcion que recibe y retorna una tupla de tuplas, donde:
    Si se ingresa "Excelente", se mostraran las peliculas con "Movie Rating">=9
    Si se ingresa "Buena", se mostraran las peliculas con "Movie Rating">=6 y "Movie Rating"<9
    Si se ingresa "Mala", se mostraran las peliculas con "Movie Rating" menor a 6
"""
def Movies4(tupla:tuple):
    list1 = [i for i in tupla if float(i[3])>=9.0]
    list2 = [i for i in tupla if float(i[3])>=6.0 and float(i[3])<9.0]
    list3 = [i for i in tupla if float(i[3])<6.0]
    def agregar_recomendacion(palabra:str)->list:
        if palabra == 'Excelente':
            return tuple(list1)
        if palabra == 'Buena':
            return tuple(list2)
        if palabra == 'Mala':
            return tuple(list3)
    return agregar_recomendacion

# Funcion que recibe y retorna una tupla de tuplas donde se filtra las peliculas que sean del genero Action,Adventure,Drama
def Movies5(tupla: tuple)-> tuple:
    my_list = filter(lambda x: x[2]=="Action,Adventure,Drama", tupla)
    return tuple(my_list)

#Funcion que recibe una tupla de tuplas de todas las peliculas del genero 'Animation,Adventure,Comedy'
# y ademas sean Clasificacion C, y al final retorne las tuplas ordenadas por nombre ascendente
def Movies6(tupla: tuple)-> tuple:
    my_list1 = filter(lambda x: x[2]=="Animation,Adventure,Comedy" and x[6]=="C" , tupla)
    my_list = sorted(my_list1, key = lambda x: x[0])
    return tuple(my_list)

# Funcion que recibe y retorna una tupla de tuplas de todas las peliculas donde el rating sea mayor o igual\
# al que se le manda y ademas el año sea mayor o igual al mandado
def Movies7(rating:str, anio: str):
    def filtrar_pelicula(tupla:tuple)->tuple:
        my_list = [i for i in tupla if i[3]>=rating and i[1]>=anio]
        return tuple(my_list)
    return filtrar_pelicula

# Funcion que recibe y retorna una tupla de tuplas
# donde si al seleccionar la opcion 1 del menu devuelve las peliculas que salieron del 2010 en adelante y clasificacion "A"
# si selecciona la opcion 2 devuelve las peliculas con rating mejor o igual que 6 y del genero  "Action,Adventure,Fantasy"
def Movies8(tupla: tuple):
    list1 = [i for i in tupla if i[1]>="2010" and i[6]=="A"]
    list2 = [i for i in tupla if i[3]>="6" and i[2]=="Action,Adventure,Fantasy"]
    def ordena_por():
        menu = """
             1. Peliculas por año y clasificacion
             2. Peliculas por Rating mejor que 6 y genero "Action,Adventure,Fantasy"
            """
        print(menu)
        opt = int(input("Ingresar opcion: "))

        if opt == 1:
            return tuple(list1)

        if opt == 2:
            return tuple(list2)
    return ordena_por

# Funcion que recibe y retorna una tupla de tuplas donde se agregue un campo extra a cada tupla dependiendo
# de la calificacion 'Movie Rating'.
def Movies9(): 
    def agregar_recomendacion2(tupla:tuple)->tuple:
        list_aux = list(tupla)
        if float(tupla[3])>=9.0:
            list_aux.append('Excelente')
        if float(tupla[3])<9.0 and float(tupla[3])>=6.0:
            list_aux.append('Buena')
        else:
            list_aux.append('Mala')
        return tuple(list_aux)
    return agregar_recomendacion2

#Funcion que recibe y retorna una tupla de tuplas que contenga 'Movie Rating' expresado en
# %, es decir, 9.0 ->90%, 6.2 ->62%, etc) de todas las peliculas de clasificacion 'C'
def Movies10(tupla:tuple):
    list_aux = [(i[3]) for i in tupla if i[6]=="C"]
    def porcentual()->tuple:
        my_list = map(lambda x:str(int(float(x[0])*10))+'%',list_aux)
        return tuple(my_list)    
    return porcentual

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

    # print(Movies5(my_tuple))
    # print(Movies6(my_tuple))

    # my_fun = Movies7("8.5","2000")
    # print(my_fun(my_tuple))

    # my_fun = Movies8(my_tuple)
    # print(my_fun())

    #my_fun = Movies9()
    #c = map(my_fun,my_tuple)
    #print(list(c))

    #my_fun = Movies10(my_tuple)
    #print(my_fun())
