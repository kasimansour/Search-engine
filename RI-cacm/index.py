from bisect import bisect_left
import json
import time
import pickle

def create_dict_terms_termsid(terms):
    ret = {}
    i = 1
    for term in terms:
        ret[term] = i
        i += 1
    return ret


def parsing(file, terms):
    # term_id = create_dict_terms_termsid(terms)
    with open(file, 'r') as fd:
        data = json.load(fd)
        tuples = []
        for doc in data:
            body = doc['.K'] + doc['.W'] + doc['.T'] # Seul le contenu de .K .W et .T nous intéresse
            for word in body.split():
                if binary_search(terms, word) != -1: # On vérifie que le mot est bien un terme (il appartient à l'ensemble des terms)
                    tuples.append((word, doc['.I']))
    return tuples

def create_posting_list(file, terms):
    begin = time.time()
    l = parsing(file, terms)
    print("Creating posting list")
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
    with open('inverted_index', 'wb') as file:
        my_pickler = pickle.Pickler(file)
        my_pickler.dump(posting_list)
    end = time.time()
    print("Done in {} seconds".format(end - begin))

def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1)
