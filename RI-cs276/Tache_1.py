# -*- coding: utf-8 -*-
import os
from math import *
import pickle
import matplotlib.pyplot as plt
from threading import Thread
from multiprocessing.pool import ThreadPool
import time


# Question 1&2 Réunies


def count_one_folder(n): # n est le numéro du dossier
    common_words = open('common_words', 'r+').read().split()
    print("Counting for folder {}".format(n))
    tokens = 0
    words = {} # On le crée pour garder la fréquence des mots, sert à calculer le nombre de termes
    vocab_length = 0
    dirpath = "pa1-data/"
    for filename in os.listdir(dirpath + str(n)):
        opened_file = open(dirpath + str(n) + '/' + filename, 'r')
        document = opened_file.read()
        for word in document.split():
            if type(word) != int:
                tokens += 1
                if word not in common_words:
                    words[word] = words[word] + 1 if word in words else 1
    for word in words:
        if words[word] == 1 :
            vocab_length += 1
    return tokens, vocab_length


def count_n_folders(n): # n est la nombre de documents à parcourir
    result = []
    (T, M) = (0, 0)
    pool = ThreadPool(processes=n)

    for i in range(n):
        async_result = pool.apply_async(count_one_folder,(i,))
        result.append(async_result.get())
    for i in range(n):
        T += result[i][0]
        M += result[i][1]
    return (T, M)

# Question3:Moitié de la Collection

# Question4

# M=k*pow(1000000, b)
# print(M)

# Question5


def frequency(n):
    os.chdir("pa1-data")
    tokens = {}
    folders_reviewed = 0
    for directory in os.listdir(os.getcwd()):
        os.chdir(directory)
        for filename in os.listdir(os.getcwd()):
            opened_file = open(filename, 'r')
            collection = opened_file.read()
            for word in collection.split():
                if type(word) != int:
                    if word in tokens:
                        tokens[word] += 1
                    else:
                        tokens[word] = 1

        folders_reviewed += 1
        if folders_reviewed >= n:
            break
    ordered_list = sorted(tokens.items(), key=lambda x: x[1])
    ordered_list.reverse()
    x = []
    y = []
    rank = 1
    value = ordered_list[0][1]
    for i in range(0, len(ordered_list)):
        y.append(log(ordered_list[i][1]))
        if ordered_list[i][1] < value:
            rank += 1
            value = ordered_list[i][1]
        x.append(log(rank))
    plt.plot(x, y)
    plt.show()


# frequency(10)
