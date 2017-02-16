# -*- coding: utf-8 -*-
import pickle
import time
from index import *

FILENAME = 'inveted_index'
common_words = open('common_words', 'r+').read().split()
# Traitement des requêtes vectorielles


def vectorial_query():
    try:
        with open(FILENAME, 'rb') as file:
            pickler = pickle.Unpickler(file)
            cs_index = pickler.load()
    except IOError:
        with open(FILENAME, 'wb') as file:
            my_pickler = pickle.Pickler(file)
            my_pickler.dump(merge_all()) #  Si l'index n'existe pas on le crée et le stocke dans un fichier
        with open(FILENAME, 'rb') as file:
            my_pickler = pickle.Unpickler(file)
            cs_index = my_pickler.load() #  On charge l'index que l'on vient de créer
    except EOFError:
        with open(FILENAME, 'wb') as file:
            my_pickler = pickle.Pickler(file)
            my_pickler.dump(merge_all()) # Si le fichier index est vide on le recrée
        with open(FILENAME, 'rb') as file:
            my_pickler = pickle.Unpickler(file)
            cs_index = my_pickler.load() #  On charge l'index que l'on vient de créer

    doc_id_collection = doc_identifier() # On crée la liste de docID

    while True:
        query = input("Type your search here...")
        beginning = time.time()
        relevant_docs = [] # La liste à envoyer à la fin
        query_vector = {}
        for term in query.split():
            if term not in common_words: # on vérifie que le mot en question est bien un terme
                query_vector[term] = query_vector[term] + 1 if term in query_vector else 1
        similarities = {}
        for doc in doc_id_collection.values():
            norm_doc = 0
            norm_query = 0
            scalar_product = 0
            for term in query_vector:
                scalar_product += query_vector[term]*cs_index[term][doc] if doc in cs_index[term] else 0
                norm_doc += pow(cs_index[term][doc], 2) if doc in cs_index[term] else 1
                norm_query += pow(query_vector[term], 2)
            similarities[scalar_product/pow(norm_query*norm_doc, 0.5)] = doc

        best_similarities = sorted(similarities.keys()) # Ordonné dans l'ordre décroissant
        best_similarities.reverse() # On ordonne dans l'ordre décroissant
        max_number = 30 if len(best_similarities) > 30 else len(best_similarities)
        for i in range(max_number):
            relevant_docs.append(similarities[best_similarities[i]])
        print(relevant_docs)
        end = time.time()
        print("{} seconds".format(end - beginning))