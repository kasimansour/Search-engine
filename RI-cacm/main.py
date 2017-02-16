from main_functions import *
from boolean_query import *
from vectorial_query import *
from index import *
# nltk.download()

# folder_name = "C:\\Users\\RomainT\\Documents\\OSY\\RI Web\\DataNew\\"
JSON_FILE = "cacm.json"
COMMON_WORDS_PATH = "common_words"

if __name__ == "__main__":
    # Question 1
    # tokens1 = get_tokens(file, 1)
    # print(len(tokens1)) #réponse à la question 1

    # Question 2
    # terms1 = get_terms(tokens1, common_words_path)
    # print(len(terms1)) #réponse à la question 2

    # Question 3
    # tokens2 = get_tokens(file, 2)
    # terms2 = get_terms(tokens2, common_words_path)

    # print(len(tokens2))
    # print(len(terms2)) #réponse à la question 3

    # b, k = heap_law(len(tokens1), len(terms1), len(tokens2), len(terms2))
    # print(b)
    # print(k)

    # Question 4
    # nb_de_termes = 1000000
    # print(heap_law_reciproque(nb_de_termes, b, k))

    # Question 5
    # f, r, logf, logr = get_frequencies_and_ranks(tokens1)
    # print_frequency_graph(f,r)
    # print_log_frequency_graph(logf, logr)

    # Index

    # parsing(file, terms1)
    # create_posting_list(file, terms1)
    boolean_query()
    #vectorial_query()

