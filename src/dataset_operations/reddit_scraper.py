#!/usr/bin/env python

"""
Reddit Scraper

requirements: 
	-Newspaper3k, https://github.com/codelucas/newspaper, http://newspaper.readthedocs.io/en/latest/

Notes: 	
	newspaper offers nlp summary
	article.nlp()
	print(article.summary)

"""
#internal
import json, requests
import string
import re
import json
import logging
import os

# mylib
from src.text_editing import component_extraction

# external
from newspaper import Article

# logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def file_title(raw_title, file_prefix='', file_extension='.txt', max_characters=20):

	# Cap Length / Generate Short Title
	if len(raw_title) > max_characters:
		#raw_title = extract(raw_title)[0]		#dependecy try and remove

		title_phrase_list = component_extraction.extract_phrases(raw_title)

		index = 0
		character_count = 0
		while (character_count < max_characters) and (index < len(title_phrase_list)-1):
			character_count += len(title_phrase_list[index]) + 1
			index +=1

		raw_title = ' '.join(title_phrase_list[:index])

		if (len(raw_title) == 0):
			logger.info('error generating title: %s' % directory_path)
			return None

	# Format File Title

	# Remove all non-word characters (everything except numbers and letters)
	free_title = re.sub(r"[^\w\s]", '', raw_title)

	# Replace all runs of whitespace with a single dash
	file_title = file_prefix + '_' + re.sub(r"\s+", '_', free_title) + file_extension

	return file_title


def save_subreddit_to_dir(subreddit, directory_path):

	# clean
	path_to_root = "../.."
	script_dir = os.path.dirname(__file__) 
	rel_path = path_to_root + directory_path 
	abs_file_path = os.path.join(script_dir, rel_path)
	directory_path = abs_file_path

	logger.info('directory_path: %s' % directory_path)
	logger.info('Connecting to subreddit: %s' % subreddit)

	r = requests.get(
	    'http://www.reddit.com/r/{}.json'.format(subreddit),
	    headers={'user-agent': 'Mozilla/5.0'}
	)

	for post in r.json()['data']['children']:
		try:
			title = post['data']['title']
			url = post['data']['url']

			fname = file_title(title, subreddit)

			article = Article(url)
			article.download()
			article.parse()
			text = article.text

			f = {'title': title, 'url':url, 'text':text}

			#file_path = os.path.join(directory_path,fname)
			file_path = directory_path + '/' + fname
			logger.info('Creating File: %s' % (file_path))
			with open(file_path, 'w+') as outfile:
				json.dump(f, outfile)

		except Exception as e:
			logger.info('failure in save_subreddit_to_dir')
			logger.info(e)

	logger.info('Subreddit Scrapping Complete.')

if __name__ == '__main__':
	save_subreddit_to_dir(subreddit, path)



"""
#path = '../../data/data_sets/scraped_subreddits/'
#subreddit = 'worldnews'

#correct
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "../../data/data_sets/scraped_subreddits"
abs_file_path = os.path.join(script_dir, rel_path)
"""


