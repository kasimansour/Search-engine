from index import *
from main_functions import *
import pickle
import time
from math import pow

JSON_FILE = "cacm.json"
COMMON_WORDS_PATH = "common_words"
TOKENS1 = get_tokens(JSON_FILE, 1)
TERMS1 = get_terms(TOKENS1, COMMON_WORDS_PATH)

FILENAME = 'inverted_index'

# Traitement des requêtes vectorielles


def vectorial_query():
    try:
        with open(FILENAME, 'rb') as file:
            pickler = pickle.Unpickler(file)
            cacm_index = pickler.load()
    except IOError:
        with open(FILENAME, 'wb') as file:
            my_pickler = pickle.Pickler(file)
            my_pickler.dump(create_posting_list(JSON_FILE, TERMS1)) #  Si l'index n'existe pas on le crée et le stocke dans un fichier
        with open(FILENAME, 'rb') as file:
            my_pickler = pickle.Unpickler(file)
            cacm_index = my_pickler.load() #  On charge l'index que l'on vient de créer
    except EOFError:
        with open(FILENAME, 'wb') as file:
            my_pickler = pickle.Pickler(file)
            my_pickler.dump(create_posting_list(JSON_FILE, TERMS1)) # Si le fichier index est vide on le recrée
        with open(FILENAME, 'rb') as file:
            my_pickler = pickle.Unpickler(file)
            cacm_index = my_pickler.load() #  On charge l'index que l'on vient de créer

    with open("cacm.json", 'r') as fd:
        data = json.load(fd)
    doc_id_collection = range(1, len(data)) # On crée la liste des docID

    while True:
        query = input("Type your search here...")
        beginning = time.time()
        relevant_docs = [] # La liste à envoyer à la fin
        query_vector = {}
        for term in query.split():
            if binary_search(TERMS1, term) != -1: # on vérifie que le mot en question est bien un terme
            # regarder la définition de binary_search dans index.py
                query_vector[term] = query_vector[term] + 1 if term in query_vector else 1
        similarities = {}
        for doc in doc_id_collection:
            norm_doc = 0
            norm_query = 0
            scalar_product = 0
            for term in query_vector:
                scalar_product += query_vector[term]*cacm_index[term][doc] if doc in cacm_index[term] else 0
                norm_doc += pow(cacm_index[term][doc], 2) if doc in cacm_index[term] else 1
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
