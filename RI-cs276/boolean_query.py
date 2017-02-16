# -*- coding: utf-8 -*-
import pickle
import time
from index import *

FILENAME = 'inveted_index'

# Traitement des requêtes boléennes, uniquement sous FNC

def boolean_query():
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
        while query != "":
            if "(" not in query:  # La requête est uniquement constituée de ET
                (query, relevant_docs) = query_without_or(query, cs_index, doc_id_collection, relevant_docs)

            else:  # La requête contient des parenthèses contenant des OU
                (query, relevant_docs) = query_with_or(query, cs_index, doc_id_collection, relevant_docs)

        print(relevant_docs)
        end = time.time()
        print("{} seconds".format(end - beginning))
        # return relevant_docs



def query_with_or(query, index, doc_id_collection, relevant_docs):
    opening_parenthesis = query.find("(")
    closing_parenthesis = query.find(")")
    litteral = query[opening_parenthesis + 1: closing_parenthesis]

    while litteral != "":
        or_position = litteral.find("OU")
        term = litteral[:or_position] if or_position != -1 else litteral
        if "NON" not in term: # Il n'y a pas de NON avant le mot
            term = term.replace(" ", "")
            if term in index:  # On vérifie si le mot entré est bien dans la collection, sinon on ne le traite pas
                relevant_docs = list(index[term].keys()) if relevant_docs == [] else list(set(relevant_docs) | set(index[term].keys()))
        else: # Il y a NON avant le mot
            term = term.replace("NON", "")
            term = term.replace(" ", "")
            if term in index:  # On vérifie si le mot entré est bien dans la collection
                negation = list(set(doc_id_collection.values()) - set(index[term].keys()))
                relevant_docs = negation if relevant_docs == [] else list(set(relevant_docs) | set(negation))
            else:
                relevant_docs = list(doc_id_collection.values()) 
                # Si le mot n'est pas dans la collection on retourne tous les documents
        litteral = litteral[or_position + 3:] if or_position != -1 else ""

    query = query.replace(query[opening_parenthesis:closing_parenthesis + 1], "") # On efface la parenthèse
    return (query, relevant_docs)


def query_without_or(query, index, doc_id_collection, relevant_docs):
    and_position = query.find("ET")
    term = query[:and_position] if and_position != -1 else query
    try:
        if "NON" not in term:  # Il n'y a pas de NON avant le mot
            term = term.replace(" ", "")
            if relevant_docs == []:
                relevant_docs = list(index[term].keys())
            else:
                relevant_docs = list(set(relevant_docs).intersection(set(index[term].keys())))

        else:  # Si il y a NON avant le mot
            term = term.replace("NON", "")
            term = term.replace(" ", "")
            if relevant_docs == []:
                relevant_docs = list(
                    set(doc_id_collection.values()) - set(index[term].keys())) if term in index else list(
                    doc_id_collection.values())
                #  Si le mot n'est pas dans la collection on envoie tous les docID
            else:
                if term in index:
                    # On vérifie si le mot est bien dans la collection, sinon on ne le traite pas
                    negation = list(set(doc_id_collection.values()) - set(index[term].keys()))
                    relevant_docs = list(set(relevant_docs).intersection(set(negation)))

        query = query[and_position + 3:] if and_position != -1 else ""  # On enlève le mot traité de la requête
    except KeyError:
        # Le cas où le mot recherché n'est pas dans le document, dans ce cas là on envoie une liste vide
        # par exemple "ghbi ET web ET phd" comme requête, ghbi n'est pas dans la collection
        print("Your word was not found")
        relevant_docs = []
        query = ""  # On arrête le traitement de la requête, ça ne sert plus à rien de traiter les autres mots
        return (query, relevant_docs)
    return (query, relevant_docs)


# boolean_query()