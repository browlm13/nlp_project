#python 3

"""
	Load subreddit articles
"""

#internal
import json
import os
import logging

# logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#
#	Data Set Methods
#

def load_scraped_subreddit_document_set(subreddit, directory_path):
	""" loads all json files from dataset matching subreddit format: "subreddit_fname.extension" and returns list of ['title','text'] """
	logger.info('Loading Document Set')

	# clean
	path_to_root = "../.."
	script_dir = os.path.dirname(__file__) 
	rel_path = path_to_root + directory_path 
	abs_file_path = os.path.join(script_dir, rel_path)
	directory_path = abs_file_path
	
	logger.info('directory_path: %s' % directory_path)

	files = [f for f in os.listdir(directory_path) if f.split('_')[0] == subreddit]
	documents = []
	for f in files:
		file_path = directory_path + '/' + f
		with open(file_path) as data_file:    
			document = json.load(data_file)

		documents.append(document)

	logger.info('Document Set Loading Complete')
	
	return documents
	

def get_document_jsons_list(subreddit,  directory_path):
	all_documents = load_scraped_subreddit_document_set(subreddit,directory_path)
	return all_documents

