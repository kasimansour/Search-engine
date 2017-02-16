# -*- coding: utf-8 -*-
import os
import pickle
from threading import Thread
import time


# CREATION DE L'INDEX INVERSE


def doc_identifier():
    print("Attributing IDs to docs...", end="")
    doc_collection = {}
    id_to_attribute = 1
    for directory in os.listdir("pa1-data"):
        for filename in os.listdir("pa1-data/" + directory):
            doc_collection[filename] = id_to_attribute
            id_to_attribute += 1
    print("Done")
    return doc_collection


# def inverse_index():
#     os.chdir("/home/kasi/PycharmProjects/RI-cs276")
#     common_words = open('common_words', 'r+').read().split()
#     index = {}
#     os.chdir("/home/kasi/PycharmProjects/RI-cs276/pa1-data")
#     for dir in os.listdir(os.getcwd()):
#         os.chdir("/home/kasi/PycharmProjects/RI-cs276/pa1-data/" + dir)
#         for filename in os.listdir(os.getcwd()):
#             opened_file = open(filename, 'r')
#             collection = opened_file.read()
#             for word in collection.split():
#                 if word not in common_words:
#                     if word in index:
#                         file_in_postings = False
#                         for doc in index[word]:
#                             if doc.get(doc_id[filename])!= None:
#                                 doc[doc_id[filename]] += 1
#                                 file_in_postings = True
#                         if file_in_postings == False:
#                             posting = {doc_id[filename]: 1}
#                             index[word].append(posting)
#                     else:
#                         posting = {doc_id[filename]:1}
#                         index[word] = []
#                         index[word].append(posting)
#             print('Done')
#     return index

# inverse_index()


def parsing(n, doc_id_collection): # n est le numéro du dossier à traiter
    print("Creating docID-term pairs for bloc {}...".format(n))
    # os.chdir("/home/kasi/PycharmProjects/RI-cs276")
    common_words = open('common_words', 'r+').read().split()
    term_doc_id_tuples = []
    for filename in os.listdir("pa1-data/{}".format(n)):
        opened_file = open("pa1-data/{0}/{1}".format(n, filename), 'r')
        collection = opened_file.read()
        for word in collection.split():
            if word not in common_words: # On vérifie que le mot est bien un terme
                term_doc_id_tuples.append((word, doc_id_collection[filename]))
    return term_doc_id_tuples


def create_posting_list(n, doc_id_collection): # n est le numéro du dossier à traiter
    l = parsing(n, doc_id_collection)
    print("Creating posting lists for bloc {}...".format(n))
    l.sort()
    posting_list = {}
    a = {l[0][1]: 1}
    posting_list[l[0][0]] = a
    for i in range(1, len(l)):
        if l[i][0] == l[i - 1][0]:
            if l[i][1] == l[i - 1][1]:
                a = posting_list[l[i][0]]
                a[l[i][1]] += 1
                posting_list[l[i][0]] = a
            else:
                a = posting_list[l[i][0]]
                a[l[i][1]] = 1
                posting_list[l[i][0]] = a
        else:
            a = {l[i][1]: 1}
            posting_list[l[i][0]] = a

    # os.chdir("/home/kasi/PycharmProjects/RI-cs276/RI-Web")
    with open('RI-Web/{}'.format(n), 'wb') as file:
        my_pickler = pickle.Pickler(file)
        my_pickler.dump(posting_list)


def treat_ten_blocks():
    doc_id_collection = doc_identifier()
    threads = []
    for i in range(10):
        t = Thread(target=create_posting_list, args=(i, doc_id_collection))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()


def merge_two_blocks(b1, b2):
    merged = {}
    while b1 != {}:
        x = b1.popitem()
        if x[0] in b2:
            merged[x[0]] = x[1]
            merged[x[0]].update(b2[x[0]])
            del b2[x[0]]
        else:
            merged[x[0]] = x[1]
    merged.update(b2)
    return merged


def merge_all():
    beginning = time.time()
    print("Creating the index...")
    treat_ten_blocks()
    print("Merging posting lists...", end="")
    os.chdir("RI-Web")
    inverted_index = {}
    for i in range(10):
        with open('{}'.format(i), 'rb') as fichier:
            my_pickler = pickle.Unpickler(fichier)
            block = my_pickler.load()
        inverted_index = merge_two_blocks(block, inverted_index)
    end = time.time()
    print("Done")
    print("Index created in {} secondes".format(end - beginning))
    return inverted_index


if __name__ == "__main__":
    with open('inveted_index', 'wb') as file:
        my_pickler = pickle.Pickler(file)
        my_pickler.dump(merge_all())
