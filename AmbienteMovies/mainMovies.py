"""
PROGRAMACION FUNCIONAL
Sanchez Hernandez Jose Eduardo
Santibañez Garcia Luis Diego
Hernandez Rosario Christian de Jesus
"""

from functionMovies import *

if __name__ == '__main__':
    my_tuple = read_csv('./Movies.csv')

    print(Movies1(my_tuple))

    # print(Movies2(my_tuple))

    # print(Movies3(my_tuple))

    # print(Movies4(my_tuple))

    #my_fun = Movies5('Drama,Romance')
    #print(my_fun(my_tuple))

    #my_fun = Movies6(my_tuple)
    #print(my_fun('Excelente'))
    #print(my_fun('Buena'))
    #print(my_fun('Mala'))

    # my_fun = Movies7("8.5","2000")
    # print(my_fun(my_tuple))

    # my_fun = Movies8(my_tuple)
    # print(my_fun())

    # my_fun = Movies9()
    # c = map(my_fun,my_tuple)
    # print(list(c))

    # my_fun = Movies10(my_tuple)
    # print(my_fun())
