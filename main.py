#from src.text_editing import component_extraction

#from src.dataset_operations import title_generation
#from src.dataset_operations import tmp_rake_sentence_ranking
from src.dataset_operations import reddit_scraper
from src.dataset_operations import load_reddit_dataset
from src.text_editing import component_extraction
from src.text_editing import co_occurrence_matrix
from src.text_editing import normalizers
from src.metrics import similarity_measures
from src.metrics import text_statistics

import os

# settings
subreddit = 'worldnews'
subreddit_data_path = '/data/data_sets/scraped_subreddits'

def scrape_reddit(subreddit, subreddit_data_path):
	subreddit_data_path = os.path.join(os.getcwd(),subreddit_data_path)
	reddit_scraper.save_subreddit_to_dir(subreddit,subreddit_data_path)

def load_dataset(subreddit, subreddit_data_path):
	return load_reddit_dataset.get_document_jsons_list(subreddit, subreddit_data_path)

#
#	test scrape reddit
#
#scrape_reddit(subreddit, subreddit_data_path)


#
#	test load reddit dataset documents
#
all_documents = load_dataset(subreddit, subreddit_data_path)


#
#	test build coocurence matrix
#

#print(co_occurrence_matrix.word_frequency_dict(all_documents[0]['text']))
# build one large coocurence matrix by stiching documents
#corpus = all_documents[0]['text']
corpus = ''.join([d['text'] for d in all_documents])

A, n, w2id, id2w = co_occurrence_matrix.break_corpus(corpus)
#print (A.shape)
#print (w2id)

#print (w2id)
#relative frequency Solar System
w2id, id2w = co_occurrence_matrix.normalize_cooccurence_matrix_words(w2id,id2w)

#np.save(outfile, x)
#outfile.seek(0) # Only needed here to simulate closing & reopening file
#np.load(outfile)

#print('\n\n')

#print (w2id)

rf = co_occurrence_matrix.relative_frequency('more','and',A, w2id, id2w)
print(rf)
rf = co_occurrence_matrix.normalized_relative_frequency('more','and',A, w2id, id2w)
print(rf)

rf = co_occurrence_matrix.relative_frequency('sun','determin',A, w2id, id2w)
print(rf)
rf = co_occurrence_matrix.normalized_relative_frequency('sun','determin',A, w2id, id2w)
print(rf)
#
#	test proper noun retrival and sentence cleaning
#
#raw_sentence = "Michael Jackson likes to eat at McDonalds"
#token_list = normalizers.processes_and_tokenize(raw_sentence)
#token_set = normalizers.set_clean_tokens(token_list)
#raw_token_list = component_extraction.extract_words(raw_sentence)
#print (raw_token_list)
#proper_nouns_list = component_extraction.remove_proper_nouns_raw_tokens(raw_token_list)
#print(proper_nouns_list)

#
#	test similarity measures
#

#print(similarity_measures.wordnet_similarity('cat','dog'))
#print(similarity_measures.similar('larry', 'shelly'))

#s1 = "the quick brown fox."
#s2 = "fox news often lies"
#s3 = "a quick brown fox"

#oc12 = similarity_measures.overlap_coefficient(s1,s2)
#oc13 = similarity_measures.overlap_coefficient(s1,s3)
#print (oc12)
#print(oc13)