import numpy as np
import nltk
#from nltk.tokenize import RegexpTokenizer
#from nltk import FreqDist
from nltk.stem.porter import *
#from nltk.stem import *

#import math
#from nltk.corpus import abc
#from nltk.corpus import brown

from nltk.corpus import stopwords
from nltk.tag import pos_tag

"""
stemmer
stemmer = PorterStemmer()
plurals = ['caresses', 'flies', 'dies', 'mules', 'denied','died', 'agreed', 'owned', 'humbled', 'sized','meeting', 'stating', 'siezing', 'itemization','sensational', 'traditional', 'reference', 'colonizer','plotted']
singles = [stemmer.stem(plural) for plural in plurals]
print(' '.join(singles))
"""


def keyword_score(term, tokenized_document, tokenized_documents_list):
	tf_idf_scaler = 2
	term_tf_idf_score = tf_idf(term,tokenized_document,tokenized_documents_list)
	term_similarity_score = similarity_score(term, tokenized_document)
	return tf_idf_scaler*term_tf_idf_score + term_similarity_score


def keyword_scores_for_part_of_speech(pos, tokenized_document, tokenized_documents_list):
	tagged_tokenized_document = pos_tag(tokenized_document)
	filtered_tokens = [term for term, tag in tagged_tokenized_document if tag == pos]
	return list(filtered_tokens)



from nltk.corpus import wordnet

def synset(word):
	""" returns the first wordnet synset of word or None.
		Not case sensitive. 
		Breaks if there is punctuation. """
	try:
		s = wordnet.synsets(word)
		name = s[0].name()
		return wordnet.synset(name)
	except Exception as e:
		print(e)
		return None

def all_synsets(word):
	""" returns all wordnet synsets of word or None.
		Not case sensitive. 
		Breaks if there is punctuation. """
	try:
		all_s = wordnet.synsets(word)
		return all_s
	except Exception as e:
		print(e)
		return None

def wordnet_similarity(word1,word2):
	""" returns wup similarity between two words, or None. """
	try:
		synset1 = synset(word1)
		synset2 = synset(word2)
		return synset1.wup_similarity(synset2)
	except Exception as e:
		print(e)
		return None

#testing
#print(syns_tag('america'))
#print(synset('america'))
#print(all_synsets('jamaica'))
#print (wordnet_similarity('israel','netanyahu'))


#import wikipedia

def direct_links_all_possible_results(word):
	all_pages = wikipedia.search(word)
	all_links = []
	for page in all_pages:
		all_links.append(page.links())
	return list(set(all_links))

def direct_links_first_result(word):
	first_result_page = wikipedia.search(word)[0]
	return first_result_page.links()



"""
w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01') # n denotes noun
print(w1.wup_similarity(w2))
"""
"""
# Then, we're going to use the term "program" to find synsets like so:
syns = wordnet.synsets("program")



# An example of a synset:
print(syns[0].name())

# Just the word:
print(syns[0].lemmas()[0].name())

# Definition of that first synset:
print(syns[0].definition())

# Examples of the word in use in sentences:
print(syns[0].examples())


# Let's compare the verbs of "run" and "sprint:"
w1 = wordnet.synset('run.v.01') # v here denotes the tag verb
w2 = wordnet.synset('sprint.v.01')
print(w1.wup_similarity(w2))

# Let's compare the noun of "ship" and "boat:"
w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01') # n denotes noun
print(w1.wup_similarity(w2))

# Let's compare the verbs of "sprint" and "sprint:"
w1 = wordnet.synset('sprint.v.01')
w2 = wordnet.synset('sprint.v.01')
print(w1.wup_similarity(w2))

syns = wordnet.synset("america")
print(syns)
"""
"""
prun corpus of non cadidate words

for each candidate word test against similarity scores for each 
other remaining word and if similarities are above a certain level
map to a category and replace occurences with that category

(original_word:string, original_location:location, 
	word_synset:string, similarity_groups:list)
"""