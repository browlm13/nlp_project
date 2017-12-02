#!/usr/bin/env python

"""
	text component extraction

sources : 
https://github.com/csurfer/rake-nltk/blob/master/rake_nltk/rake.py,
https://gist.github.com/alexbowe/879414
http://alexbowe.com/au-naturale/

papers:
	1.) title: Automatic keyphrase extraction from scientific articles
		authors: Su Nam Kim • Olena Medelyan • Min-Yen Kan • Timothy Baldwin
"""

#internal
import string
import operator
import re
import copy

#import similarity_measures as sim

#external
import numpy as np
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import *
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk import FreqDist

def get_proper_nouns_sentence(raw_sentence):
	""" Returns list of proper nouns, and must accept an unstemmed sentence string
		not converted to lower case """

	assert type(raw_sentence) == str
	tagged_token_list = pos_tag(raw_sentence.split())
	proper_nouns_list = [word for word, pos in tagged_token_list if pos == 'NNP']
	return proper_nouns_list

def remove_proper_nouns_sentence(raw_sentence): 
	""" Returns list of sentence tokens with proper nouns removed, and must accept an unstemmed sentence string
		not converted to lower case """

	assert type(raw_sentence) == str
	tagged_token_list = pos_tag(raw_sentence.split())
	token_list = [word for word, pos in tagged_token_list if pos != 'NNP']
	return token_list

def get_proper_nouns_raw_tokens(raw_tokens):
	""" Returns list of proper nouns, and must accept an unstemmed list of tokens
		not converted to lower case """

	assert type(raw_tokens) == list
	tagged_token_list = pos_tag(raw_tokens)
	proper_nouns_list = [word for word, pos in tagged_token_list if pos == 'NNP']
	return proper_nouns_list

def remove_proper_nouns_raw_tokens(raw_tokens): 
	""" Returns list of tokens with proper nouns removed, and must accept an unstemmed list of tokens
		not converted to lower case """

	assert type(raw_tokens) == list
	tagged_token_list = pos_tag(raw_tokens)
	token_list = [word for word, pos in tagged_token_list if pos != 'NNP']
	return token_list

def remove_scores(list_of_tupples):
	""" Remove key (word,phrase,senence) scores. """
	return [i[0] for i in list_of_tupples]

def is_punctuation(word):
	""" Return True if word is composed entirly of punctuation and whitespace """
	if set(word) < set(string.punctuation + string.whitespace):
		return True
	return False

def is_stopword(word):
	""" Return True of word is in stop word list """
	stop_words = nltk.corpus.stopwords.words()
	return word in stop_words

def break_word(word, marker):
	""" Seperate phrases based on break_words, return marker if word is break_word, otherwise return word """
	if is_stopword(word) or is_punctuation(word):
		return marker
	return word

def extract_sentences(document):
	""" Extract sentences from raw document and return list """
	sentences = nltk.sent_tokenize(document.lower())
	return sentences

def extract_words(sentence):
	""" Extract words from raw document and return list """
	words = nltk.word_tokenize(sentence)
	return words

def extract_phrases(document):
	""" Exctract non stop words and phrases from document and return list of words and phrases"""
	marker = '|'
	sentences = extract_sentences(document)

	phrase_list = []
	for sentence in sentences:
		sentence = extract_words(sentence)
		phrase_list += [break_word(w,marker) for w in sentence]

	phrase_list = ' '.join(phrase_list).split(marker)
	return list([p.strip() for p in phrase_list if is_punctuation(p) == False])