#!/usr/bin/env python

"""
	text statistics
"""
def word_frequency_dict(tokens):
	""" returns a dictionary of word and their assosiated frequencies from token list """

	fdist = FreqDist(tokens) 						# fdist.keys() fdist.values()
	return dict(fdist)

def term_fequency(term,tokens):
	term = processes_and_tokenize(term)[0]	#make sure term is in correct form

	tf = tokens.count(term)
	return tf/len(tokens)

def augmented_term_fequency(term,tokens):
	""" returns term frequency in tokens over maximum term frequency of tokens """
	term = processes_and_tokenize(term)[0] #make sure term is in correct form

	max_count = max([tokens.count(t) for t in tokens])
	return tokens.count(term)/max_count

def inverse_document_frequency(term, tokenized_documents_list):
	""" IDF(t) = ln( Number Of Documents / Number Of Documents Containg Term )."""
	term = processes_and_tokenize(term)[0]	#make sure term is in correct form

	num_documents = len(tokenized_documents_list)
	num_documents_with_term = len([document for document in tokenized_documents_list if term in document])
	
	assert num_documents_with_term > 0
	return math.log(num_documents / num_documents_with_term)


def nolog_inverse_document_frequency(term, tokenized_documents_list):
	""" IDF(t) = ln( Number Of Documents / Number Of Documents Containg Term )."""
	term = processes_and_tokenize(term)[0]	#make sure term is in correct form

	num_documents = len(tokenized_documents_list)
	num_documents_with_term = len([document for document in tokenized_documents_list if term in document])
	
	assert num_documents_with_term > 0
	return num_documents / num_documents_with_term

def tf_idf(term, tokenized_document, tokenized_documents_list):
	""" Term Frequency - Inverse Document Frequency : returns tf * idf """
	#return term_fequency(term, tokenized_document) * inverse_document_frequency(term, tokenized_documents_list)
	#return augmented_term_fequency(term, tokenized_document) * inverse_document_frequency(term, tokenized_documents_list)
	return term_fequency(term, tokenized_document) * nolog_inverse_document_frequency(term, tokenized_documents_list)
