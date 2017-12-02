#!/usr/bin/env python

"""
	Keyword selection function performance

	Scorring
"""

# version 1
def similarity_score(a,b):
	""" combine all similarity measures into single score """
	jsc_scaler = 15
	ocs_scaler = 5
	tcss_scaler = 0.05

	jaccard_similarity_coefficient_score = jsc_scaler * jaccard_similarity_coefficient(a,b)
	overlap_coefficient_score = ocs_scaler * overlap_coefficient(a,b)
	total_char_similarity_score = tcss_scaler * total_char_similarity(a,b)
	total_score = jaccard_similarity_coefficient_score + overlap_coefficient_score + total_char_similarity_score
	
	return total_score
# verison 1
def keyword_score(term, tokenized_document, tokenized_documents_list):
	tf_idf_scaler = 2
	term_tf_idf_score = tf_idf(term,tokenized_document,tokenized_documents_list)
	term_similarity_score = similarity_score(term, tokenized_document)
	return tf_idf_scaler*term_tf_idf_score + term_similarity_score

# verison 1
def keyword_scores_for_part_of_speech(pos, tokenized_document, tokenized_documents_list):
	tagged_tokenized_document = pos_tag(tokenized_document)
	filtered_tokens = [term for term, tag in tagged_tokenized_document if tag == pos]
	return list(filtered_tokens)


def word_relatedness_score(word1, word2):
	score = -1
	return score

def sentence_relatedness_score(word, sentence):
	score = -1
	return score


