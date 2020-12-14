import os
import re

from greek_stemmer import GreekStemmer

from anonymizer_service.trie_index import prepair_word


class Excluder:
    @classmethod
    def exclude(cls, entities, exclude_array):
        exclude_array = [x[1:-1] for x in exclude_array]
        exclude_array = [x for x in exclude_array if x is not '']
        print(exclude_array)
        entities = [x for x in entities if x[1]]
        print(entities)
        # if exclude_array:
        entities = cls.stemmer_clean(entities, exclude_array)
        entities = cls.regex_clean(entities, exclude_array)
        print(entities)
        return entities

    @staticmethod
    def stemmer_clean(entities, exclude_array):
        stemmer = GreekStemmer()
        exclude_list = exclude_array
        stemmed_excl_list = [stemmer.stem(prepair_word(x).upper()) for x in exclude_list]
        clean_entities = [x for x in entities if stemmer.stem(prepair_word(x[1]).upper()) not in stemmed_excl_list]
        print("~~~~~~~~~~~~~~~~~STEMMER~~~~~~~~~~~~~~~~~")
        print("---stemmed_excl_list---")
        print(stemmed_excl_list)
        print("---clean_entities---")
        print(clean_entities)
        print("~~~~~~~~~~~~~~~~~END OF STEMMER~~~~~~~~~~~~~~~~~")
        return clean_entities

    @classmethod
    def regex_clean(cls, entities, exclude_array):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'regex_exclude_words.txt')
        with open(file_path, 'r') as file_:
            exclude_list = exclude_array + file_.read().splitlines()
        print(exclude_list)
        filtered = [i for i in entities if not any([re.search(patt, i[2]) for patt in exclude_list])]
        return filtered
