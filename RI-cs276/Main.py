# -*- coding: utf-8 -*-
from Tache_1 import *
from index import *
from boolean_query import  *
from vectorial_query import *

if __name__ == "__main__":

    # Question 1 ET 2
    # (T, M) = count_n_folders(10)
    # print("Nb de tokens : {0}, taille du vocabulaire : {1}".format(T, M))

    # Question 3 ET 4
    # (T1, M1) = count_n_folders(10)
    # (T2, M2) = count_n_folders(5)
    # print("moitié de la collection, Nb de tokens : {0}, taille du vocabulaire : {1}".format(T2, M2))
    # b = ((log(M2) - log(M1)) / (log(T2) - log(T1)))
    # k=M1*pow(T1, -b)
    # print("Les coefficients de la loi de Heap sont, b : {0} et k : {1}".format(b, k))

    # M = k * pow(1000000, b)
    # print("pour 1 million de tokens : {}".format(M))

    # Question 5
    # frequency(10)

    boolean_query()
    # vectorial_query()