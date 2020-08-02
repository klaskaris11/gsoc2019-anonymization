import os
import re

from greek_stemmer import GreekStemmer

from anonymizer.trie_index import prepair_word


class Excluder:
    @classmethod
    def exclude(cls, entities):
        entities = [x for x in entities if x[1]]
        entities = cls.stemmer_clean(entities)
        entities = cls.regex_clean(entities)
        return entities

    @staticmethod
    def stemmer_clean(entities):
        stemmer = GreekStemmer()
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'stemmer_exclude_words.txt')
        with open(file_path, 'r') as file_:
            exclude_list = file_.read().splitlines()
        stemmed_excl_list = [stemmer.stem(prepair_word(x).upper()) for x in exclude_list]
        clean_entities = [x for x in entities if stemmer.stem(prepair_word(x[1]).upper()) not in stemmed_excl_list]
        return clean_entities

    @classmethod
    def regex_clean(cls, entities):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'regex_exclude_words.txt')
        with open(file_path, 'r') as file_:
            exclude_list = file_.read().splitlines()
        filtered = [i for i in entities if not any([re.search(patt, i[2]) for patt in exclude_list])]
        return filtered
