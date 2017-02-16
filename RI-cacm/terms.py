import string
import re
from math import log, pow, floor


def is_punct_char(char):
    if char in string.punctuation:
        return 1
    else:
        return 0


def is_1_char_string(s):
    if len(s) == 1:
        return True
    else:
        return False


def is_2_char_string(s):
    if len(s) == 2:
        return True
    else:
        return False


def is_punct_string(s):
    if is_1_char_string(s) and is_punct_char(s):
        return True
    elif is_2_char_string(s) and is_punct_char(s[0]) and is_punct_char(s[1]):
        return True
    elif s == "...":
        return True
    else:
        return False


def is_not_is(s):
    if s == "'s" or s == "'S":
        return False
    else:
        return True


def represents_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def contains_letter(s):
    return re.search('[a-zA-Z]', s) is not None


def remove_duplicates(l):
    return list(set(l))


def remove_All_figures_and_symbols(s):
    res = ""
    for char in s:
        if not (char in string.punctuation or char.isdigit()):
            res = res + char
    return res


def remove_All_figures_and_symbols_in_table(table):
    for i in range(len(table)):
        table[i] = remove_All_figures_and_symbols(table[i])
    return table


def remove_common_words(tokens, common_words):
    answer = []
    common = common_words
    while tokens and common:
        if tokens[0] == common[0]:
            del tokens[0]
            del common[0]
        elif tokens[0] < common[0]:
            answer.append(tokens[0])
            del tokens[0]
        else:
            del common[0]
    return answer


def heap_law(t1, m1, t2, m2):
    b = ((log(m2) - log(m1)) / (log(t2) - log(t1)))
    return b, m1 * pow(t1, -b)


def heap_law_reciproque(t, b, k):
    return floor(k * pow(t, b))
