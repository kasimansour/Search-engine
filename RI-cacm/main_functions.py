import math
import nltk
import json

import matplotlib.pyplot as plt

from terms import *


def get_tokens(file, n):
    tokens = []

    with open(file) as data_file:
        data = json.load(data_file)

    for i in range(math.ceil(len(data) / n)):
        tokens += nltk.word_tokenize(data[i][".T"]) + nltk.word_tokenize(data[i][".W"]) + nltk.word_tokenize(
            data[i][".K"])

    tokens[:] = [token for token in tokens if (not is_punct_string(token)) and contains_letter(token)]

    return tokens


def get_terms(tokens, common_words_path):
    tokens[:] = [token for token in tokens if is_not_is(token)]
    tokens = remove_All_figures_and_symbols_in_table(tokens)
    tokens = [x.lower() for x in tokens]
    tokens = remove_duplicates(tokens)
    tokens.sort()

    common_words = open(common_words_path, "r+")
    common = common_words.readlines()
    common[:] = [word[:-1] for word in common]
    tokens = remove_common_words(tokens, common)

    # print(tokens[:500])

    return tokens


def get_frequencies_and_ranks(tokens):
    ranking = {}
    for token in tokens:
        if token in ranking:
            ranking[token] += 1
        else:
            ranking[token] = 1

        ordered_list = sorted(ranking.items(), key=lambda x:x[1])
        ordered_list.reverse()
        x = []
        y = []
        xlog = []
        ylog = []
        rank = 1
        value = ordered_list[0][1]
        for i in range(0, len(ordered_list)):
            y.append(ordered_list[i][1])
            ylog.append(log(ordered_list[i][1]))
            if ordered_list[i][1] < value:
                rank += 1
                value = ordered_list[i][1]
            x.append(rank)
            xlog.append(log(rank))
    return y, x, ylog, xlog


def print_frequency_graph(f,r):
    plt.plot(f, r)
    plt.show()

def print_log_frequency_graph(logf, logr):
    plt.plot(logf, logr)
    plt.show()
