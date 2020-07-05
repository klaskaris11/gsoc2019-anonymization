import os

from greek_stemmer import GreekStemmer

from anonymizer.trie_index import prepair_word


class Excluder:
    stemmer = GreekStemmer()

    @classmethod
    def exclude(cls, entities):
        exclude_list = cls.get_exclude_list()
        entities = [x for x in entities if x[1]]
        clean_entities = [x for x in entities if cls.stemmer.stem(prepair_word(x[1]).upper()) not in exclude_list]
        return clean_entities

    @classmethod
    def get_exclude_list(cls):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'exclude.txt')
        with open(file_path, 'r') as file_:
            exclude_list = file_.read().splitlines()
        stemmed_exclude_list = [cls.stemmer.stem(prepair_word(x).upper()) for x in exclude_list]
        return stemmed_exclude_list
