
"""
	Wikipedia Anaylisis
"""

import wikipedia

def direct_links_all_possible_results(word):
	all_pages = wikipedia.search(word)
	all_links = []
	for page in all_pages:
		all_links.append(page.links())
	return list(set(all_links))

def direct_links_first_result(word):
	first_result_page = wikipedia.search(word)[0]
	return first_result_page.links()