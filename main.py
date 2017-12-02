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
#model_name = 'model1'
#CM.save(directory_path,model_name)

# 
# test load coocurence matrix
#

directory_path = '/data/models'
model_name = 'model1'
CM = Coo_Matrix()
CM.load(directory_path + '/' + model_name)


#
#	Save results
#

print(CM.relative_frequency('donald', 'trump'))
print(CM.relative_frequency('president', 'trump'))
print(CM.relative_frequency('oil', 'trump'))
print(CM.relative_frequency('birth', 'defects'))
print(CM.relative_frequency('people', 'oil'))

print(CM.most_related_word('donald'))
print(CM.rank_most_related_words('donald')[:20])


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