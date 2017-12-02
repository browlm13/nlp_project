#python 3

#internal
from difflib import SequenceMatcher

#mylib
#import normalizers as norm
from src.text_editing import normalizers as norm

#external
from nltk.corpus import wordnet

"""
		similarity measures

			Jaccard index / Intersection over Union / Jaccard similarity coefficient

			Overlap Coefficient  - the overlap between two sets, and is defined as the size of the intersection divided by the smaller of the size of the two sets:
"""

def jaccard_similarity_coefficient(a, b):
	""" compute jaccard index after processing (tokenize sentence, convert to lower, stem, remove stop words, numbers, punctuation)"""
	a_words, b_words = map(norm.set_clean_tokens, [a,b])

	intersection = set.intersection(a_words, b_words)
	union = set.union(a_words, b_words)

	#try to compute jaccard index
	try: jaccard_index = len(intersection)/len(union)
	except: pass

	#empty sets
	if len(a_words) == 0 or len(b_words) == 0:
		jaccard_index = 0

	return jaccard_index

def overlap_coefficient(a, b):
	""" compute overlap_coefficient after processing (tokenize sentence, convert to lower, stem, remove stop words, numbers, punctuation)"""
	a_words, b_words = map(norm.set_clean_tokens, [a,b])

	intersection = set.intersection(a_words, b_words)
	length_a_words, length_b_words = len(a_words), len(b_words)

	#empty sets
	if length_a_words == 0 or length_b_words == 0: return 0

	#try to compute overlap_coefficient
	try: overlap_coefficient = len(intersection)/min(length_a_words,length_b_words)
	except: overlap_coefficient = 0

	return overlap_coefficient


"""
	Wordnet Similarity
"""

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

"""
	character similarity
"""

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def total_char_similarity(a,b):
	""" compute similarity score of characters for 
		each word in cartesian product"""

	a_words, b_words = map(norm.set_clean_tokens, [a,b])

	total_score = 0
	for ai in a_words:
		for bi in b_words:
			total_score += similar(ai, bi)
	return total_score

