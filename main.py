from src.dataset_operations import reddit_scraper
from src.dataset_operations import load_reddit_dataset
from src.text_editing import component_extraction
#from src.text_editing import co_occurrence_matrix
from src.text_editing import normalizers
from src.metrics import similarity_measures
from src.metrics import text_statistics
from src.text_editing.co_occurrence_matrix_v2 import Coo_Matrix

import os

# settings
subreddit = 'news'
subreddit_data_path = '/data/data_sets/scraped_subreddits'

def scrape_reddit(subreddit, subreddit_data_path):
	subreddit_data_path = os.path.join(os.getcwd(),subreddit_data_path)
	reddit_scraper.save_subreddit_to_dir(subreddit,subreddit_data_path)

def load_dataset(subreddit, subreddit_data_path):
	return load_reddit_dataset.get_document_jsons_list(subreddit, subreddit_data_path)

#
#	test scrape reddit
#
scrape_reddit(subreddit, subreddit_data_path)


#
#	test load reddit dataset documents
#
#all_documents = load_dataset(subreddit, subreddit_data_path)


#
#	test build coocurence matrix
#

# build one large coocurence matrix by stiching documents
#corpus = ''.join([d['text'] for d in all_documents])
#CM = Coo_Matrix(corpus)

# 
# test save coocurence matrix
#

#directory_path = '/data/models'
#model_name = 'model2'
#CM.save(directory_path,model_name)

# 
# test load coocurence matrix
#

#CM = Coo_Matrix()
#CM.load(directory_path + '/' + model_name)



#
#	Find related words
#

"""
print(CM.relative_frequency('donald', 'trump'))
print(CM.relative_frequency('president', 'trump'))
print(CM.relative_frequency('oil', 'trump'))
print(CM.relative_frequency('birth', 'defects'))
print(CM.relative_frequency('people', 'oil'))

print(CM.most_related_word('donald'))
print(CM.rank_most_related_words('donald')[:20])

trump_list = CM.related_words_list_filtered_decending('trump')
print(trump_list[:20])

#
#	Save results
#
import random
import numpy as np

id2w = CM.id2w

n = 150		# sample size
m = 10		# top m most related words
random_indexs = random.sample(range(0, len(id2w)-1), n)
corpus_terms = [id2w[i] for i in random_indexs]

#corpus_terms = ['republican','flynn','trump','2016','lied','biblical','drug','communist','criminal','russia','chinese','inauguration','obama','nuclear','spine','twitter','students','unanimous','hillary','peace','deal', 'clearances','financial','failed','prescription','unprecedented','election','ship','taliban','military']
#corpus_terms = ['republican','ship','drug','communist','taliban','flynn','russia','inauguration','trump','obama','spine','2016','twitter','unprecedented','election','unanimous','hillary','prescription','peace','financial']

# list of lists where the first index is a corpus term and the trailing indexs are its ranked related words
list_of_related_word_lists = []
for t in corpus_terms:
	print('\nterm: %s' % t)
	related_terms = CM.related_words_list_filtered_decending(t)
	for i in range(m):
		print(related_terms[i])
	list_of_related_word_lists.append(related_terms[:m])

np_related_words = np.array(list_of_related_word_lists)

# write randomly sampled related words to file
directory_path = 'results/cooccurence_matrix_related_words'
np_related_words_file_path = directory_path + '/np_related_words_'+ model_name	#np.save appends extension .npy
np.save(np_related_words_file_path, np_related_words)
"""

#corpus_terms = ['donald', 'trump', 'america', 'russia', 'space','cannabis','prescription','court']
#llist = CM.related_words_list_filtered_decending('space')
#print(llist[:5])


#
#	test proper noun retrival and sentence cleaning
#
#raw_sentence = "Donald Trump"
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