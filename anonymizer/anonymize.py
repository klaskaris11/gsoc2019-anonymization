import sys
import getopt
import spacy
from spacy.matcher import Matcher
from termcolor import colored
from anonymizer import matcher_patterns


def entity_type_convertion(data, doc):
    results = []
    for match_id, start, end in data:
        entity_name = doc.vocab.strings[match_id]
        found_by_spacy = True
        span = doc[start:end]
        results.append([entity_name, span, span,
                        start, end, found_by_spacy])
    return(results)


def matches_handler(matcher, doc, i, matches, method='delete'):
    pass


def file_to_text(ifile, format='.txt'):
    try:
        with open(ifile, 'r') as f:
            data = f.read().replace('\n', ' ')
            return data
    except FileNotFoundError as fnf_error:
        exit(fnf_error)


def find_entities(ifile, ofile, method='delete', configuration='conf.json'):

    nlp = spacy.load('el_core_news_sm')
    matcher = Matcher(nlp.vocab)
    data = file_to_text(ifile, '.txt')
    doc = nlp(data)
    data = str(doc)
    '''
        --- ENTITY LIST EXPLANATION ---
        entities = [entity_name, entity_value,
            span/word, start, end, found_by_spacy]

        We will use found_by_spacy bool to access data either via
        doc[start:end] if True else str(doc)[start:end] .

        Span/word is the word just the way it was found into the text
        while entity_value is the value extracted through specific
        algorithms each time.

        Some times these to might have the same value.
    '''
    entities = []

    results = matcher_patterns.vehicle(data=data)
    if results != []:
        entities += results
    # You can pass as argument the match handler. This one will
    # delete be default the recognised entities in the text
    results = matcher_patterns.phone_number(data=data)
    if results != []:
        entities += results
    matches = matcher(doc)
    results = entity_type_convertion(matches, doc)
    if results != []:
        entities += results
    results = matcher_patterns.identity_card(data=data)
    if results != []:
        entities += results
    results = matcher_patterns.iban(data=data)
    if results != []:
        entities += results
    results = matcher_patterns.afm(data=data)
    if results != []:
        entities += results
    results = matcher_patterns.amka(data=data)
    if results != []:
        entities += results
    results = matcher_patterns.brand(data=data)
    if results != []:
        entities += results
    results = matcher_patterns.address(data=data)
    if results != []:
        entities += results
    results = matcher_patterns.name(data=data)
    if results != []:
        entities += results
    # Display
    for element in entities:
        print('[', colored(element[0], 'yellow'), ',', colored(
            element[1], 'blue'), ',', colored(element[2], 'cyan'), ']')