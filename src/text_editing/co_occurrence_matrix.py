#python 3

#internal
import logging
from collections import Counter
import random
import itertools

#external
import numpy as np
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import sent_tokenize
from nltk import FreqDist
from nltk.util import ngrams

#dir
#from matrix_decomposition import *


"""
	Corpus Manipulation Methods
"""

#set up logger
#filename= __name__ + ".log"
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def word_frequency_dict(corpus):
	""" returns a dictionary of word and their assosiated frequencies """

	logger.info("Creating \'word frequency\'' dictionary from corpus")

	# remove punctuation, convert to lower case, tokenize, cout frequencies
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(corpus.lower())		# tokens = nltk.word_tokenize(corpus.lower()) # without removing punctiation
	fdist = FreqDist(tokens) 						# fdist.keys() fdist.values()
	return dict(fdist)

def word_ids(corpus):
	""" returns a dictionary of key: id, value: word for every unique word in corpus """

	logger.info("Creating \'word id\'' dictionary from corpus")

	# remove punctuation, convert to lower case, tokenize, keep unqiue
	tokenizer = RegexpTokenizer(r'\w+')
	unique_tokens = set(tokenizer.tokenize(corpus.lower()))
	word_ids = {i:word for i,word in enumerate(unique_tokens)}
	return word_ids

def process_text(text):
	""" return list of lowercase alphabetic words from text """
	tokenizer = RegexpTokenizer(r'\w+')
	return tokenizer.tokenize(text.lower())

def ngram_tupples(corpus, n):
	""" Create ngram tupples by sentence. Where n is the distance between words in a sentence. """
	sentences = sent_tokenize(corpus)

	pairs = []
	for s in sentences:
		unique_tokens = process_text(s)
		pairs.extend(ngrams(unique_tokens,n))

	return pairs


def get_unique_words(corpus):
	return list(set(process_text(corpus)))

def w2id_id2w_maps(unique_words):
	""" return both dictonaries for mapping between words and ids """
	id2w = {i:w for i,w in enumerate(unique_words)}
	w2id = {w:i for i,w in id2w.items()}
	return w2id, id2w

def ngram_inc_amt(n):
	""" return float for increment weight of pair occurence n distance appart. \nWeight increment ~ 1/n """
	return 1/float(n**2)

def words2ids(words, w2id):
	""" return list of ids inplace of list of words using w2id dictionary """
	return [w2id[w] for w in words]

def cooccurence_pair_of_distance(sentence_list, d):
	""" return list of unique coocurence pairs of distace d """

	all_ngrams = ngrams(sentence_list,d)

	all_pairs = []
	for t in all_ngrams:
		if len(t) > 1:
			all_pairs.extend(list(itertools.combinations(t, 2)))

	return list(set(all_pairs))

def break_corpus(corpus):
	""" Build Cooccurence Matrix. Return A, n, w2id, id2w """

	unique_words = get_unique_words(corpus)
	n = len(unique_words)
	w2id, id2w = w2id_id2w_maps(unique_words)

	#create empty cooccurence matrix
	#A = np.zeros([n,n],np.float32)
	A = np.ones([n,n],np.float32)

	#compute cooccurence matrix
	sentences = sent_tokenize(corpus)
	for s in sentences:
		s = process_text(s)
		max_distance = len(s) + 1
		s = [w2id[w] for w in s]	#convert words to ids

		for d in range(2,max_distance):
			pairs = cooccurence_pair_of_distance(s, d)

			#update cooccurence matrix for each pair
			for p in pairs:
				A[p[0],p[1]] += ngram_inc_amt(d)
				A[p[1],p[0]] += ngram_inc_amt(d)

	return A, n, w2id, id2w

#
#	Cooccurence Matrix Manipulation methods
#
from src.text_editing import normalizers
def normalize_cooccurence_matrix_words(w2id, id2w):
	""" normalize cooccurence matrix words 
	so it can be used in conjustion with other text mining modules"""
	clean_w2id, clean_id2w = {}, {}
	for k,v in w2id.items():
		clean_word = normalizers.clean_word(k)
		if clean_word == "": clean_word = k
		clean_w2id[clean_word] = v
		clean_id2w[v] = clean_word

	return clean_w2id, clean_id2w


def relative_frequency(w1,w2, A, w2id, id2w):
	""" return relative frequencies between two 
		words in cooccurence matrix. """
	try:
		# format words
		row = w2id[w1]
		col = w2id[w2]
		return A[row,col]
	except: 
		raise Exception('Key Error')
		return None

def mean_relative_frequency(A):
	""" return the mean of all matrix values as a float"""
	means_of_each_col = A.mean(axis=0)	#mean of each row
	mean_of_matrix = means_of_each_col.mean(axis=0)

	return mean_of_matrix

def normalized_relative_frequency(w1,w2, A, w2id, id2w):
	""" return relative frequencies between two 
		words in cooccurence matrix divided by the 
		mean relative_frequency of every matrix value"""
	try:
		# format words
		row = w2id[w1]
		col = w2id[w2]
		return A[row,col]/mean_relative_frequency(A)
	except: 
		raise Exception('Key Error')
		return None

"""
import json

# as requested in comment
exDict = {'exDict': exDict}

with open('file.txt', 'w') as file:
     file.write(json.dumps(exDict))
"""
