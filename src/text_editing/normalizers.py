#!/usr/bin/env python

"""
	Normalize and clean text methods
"""
import logging
import string
import math

import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from nltk import FreqDist
from nltk.tag import pos_tag

# logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def is_stopword(word):
	""" Return True of word is in stop word list """
	stop_words = nltk.corpus.stopwords.words('english')
	return word in stop_words

def is_punctuation(word):
	return len(word) == 1 and word in string.punctuation

def is_number(word):
	try:
		float(word)
		return True
	except ValueError:
		logger.debug('ValueError is_number')
 
	try:
		import unicodedata
		unicodedata.numeric(word)
		return True
	except (TypeError, ValueError):
		logger.debug('ValueError is_number')
	 
	return False

def is_shorter(word,n=3):
	if len(word) < n:
		return True
	return False

def stem(word):
	ps = PorterStemmer()
	return ps.stem(word)

def clean_word(raw_word):
	""" Takes string converts to lower case, stems 
	and returns empty string if word is stop word, 
	punctation or is less than 3 characters long """

	raw_word = raw_word.lower()
	if is_stopword(raw_word) or is_punctuation(raw_word) or is_shorter(raw_word) or is_number(raw_word):
		word = ""
	else:
		word = stem(raw_word)
	return word

def remove_short_and_stopwords(token_list):
	filtered_token_list = []
	for t in token_list:
		if is_stopword(t) or is_punctuation(t) or is_shorter(t) or is_number(t):pass
		else: filtered_token_list.append(t)
	return filtered_token_list


def set_clean_raw_text(raw_text):
	""" tokenize sentence, convert to lower, stem, remove stop words, numbers, punctuation"""
	logger.debug('Cleaning Text')

	#tokenize and lower sentence
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(raw_text.lower())		# tokens = nltk.word_tokenize(corpus.lower()) # without removing punctiation

	#remove stop words
	tokens = [w for w in tokens if not is_stopword(w)]

	#remove punctuation
	tokens = [w for w in tokens if not is_punctuation(w)]

	#remove short 
	tokens = [w for w in tokens if not is_shorter(w)]

	#remove number
	tokens = [w for w in tokens if not is_number(w)]

	#stem words
	tokens = map(stem, tokens)

	logger.debug('Cleaning Text Complete')
	return set(tokens)

def set_clean_tokens(raw_token_list):
	""" clean tokenized sentence, convert to lower, stem, remove stop words, numbers, punctuation"""
	logger.debug('Cleaning Text')

	clean_tokens = []
	for t in raw_token_list:
		clean_token = clean_word(t)
		if clean_token != "":
			clean_tokens.append(clean_token)

	return set(clean_tokens)

def processes_and_tokenize(raw_document):
	""" remove punctuation, convert to lower case, and return list of tokens """
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(raw_document.lower())		# tokens = nltk.word_tokenize(corpus.lower()) # without removing punctiation

	#remove stop words
	stop_words = set(nltk.corpus.stopwords.words('english'))
	#stop_words = set(stopwords.words('english'))
	filtered_tokens = [w for w in tokens if not w in stop_words]
	return filtered_tokens

