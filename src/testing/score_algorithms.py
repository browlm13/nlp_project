#python 3
"""
	score algorithms

	- using data set and article titles
"""
#internal
import json
import os
import logging

#mylibs
import load_documents
import normalizers as norm
import keywords as key
import similarity_measures as sim

# logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def new_document_info(title='title', text='text', key_words=[], key_phrases=[], key_sentences=[], key_words_score=-1,key_phrases_score=-1,key_sentences_score=-1, total_score=-1, reduced_summary='summary_text'):
	document_score_info={
		'title': title,
		'text': text,
		'key_words': key_words,
		'key_phrases': key_phrases,
		'key_sentences': key_sentences,
		'key_words_score' : key_words_score,
		'key_phrases_score' : key_phrases_score,
		'key_sentences_score' : key_sentences_score,
		'total_score': total_score,
		'reduced_summary':summary_text
	}
	return document_score_info

all_documents = load_documents.get_document_jsons_list()
all_documents_infos =[]
percentage = 0.2

for d in all_documents:

	d_title = d['title']
	d_text = d['text']

	title_words_list = norm.processes_and_tokenize(d['title'])

	key_words_list = key.top_words(d['text'], return_scores=False)
	key_phrase_list = key.top_phrases(d['text'],return_scores=False)
	key_sentence_list = key.top_sentences(d['text'],return_scores=False)

	key_words_score = sim.similarity_score(title_words_list, key_words_list)
	key_phrases_score = sim.similarity_score(title_words_list, key_phrase_list)
	key_sentences_score = sim.similarity_score(title_words_list, key_sentence_list)
	total_score = key_words_score + key_phrases_score + key_sentences_score

	summary_text = key.summary(d['text'],percentage)

	d_info =  new_document_info(title=d_title,text=d_text, key_words=key_words_list, key_phrases=key_phrase_list, key_sentences=key_sentence_list, key_words_score=key_words_score, key_phrases_score=key_phrases_score, key_sentences_score=key_sentences_score, total_score=total_score, reduced_summary=summary_text)

	all_documents_infos.append(d_info)


d_with_max_score = all_documents_infos[0]
for d in all_documents_infos:
	if d['total_score'] > d_with_max_score['total_score']:
		d_with_max_score = d

#print (d_with_max_score['title'])
#print (d_with_max_score['key_words'])
#print (d_with_max_score['key_phrases'])
#print (d_with_max_score['key_sentences'])
#print(d_with_max_score['reduced_summary'])

