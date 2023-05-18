from .hashtable import Hashtable
import re


def first_repeated_word(sentence):
    words = sentence.split()
    hash_table = Hashtable(len(words) * 10)
    for word in words:
        print(word)
        test_word = ''.join(c for c in word if c.isalpha()).lower()
        print(test_word)
        if hash_table.has(test_word):
            return test_word
        else:
            hash_table.set(test_word, word)
    return None
