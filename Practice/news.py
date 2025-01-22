#News app
import requests
import os
os.system('cls')

def search_param():
	
	return {
		'q': input('About which topic you want to search: '),
		'qintitle' : input('Anything to look for in tittle, optional: ') or None,
		# 'sources' : input('Sources(not domain) you want to use, optional: ') or None,
		# 'domains' : input('Any specific domain, optional: ') or None,
		# 'exclude_domains' : input('Any specific domain to exclude, optional: ') or None,
		# 'from_param' : input('Start date (from), optional: ') or '2025-01-07',
		# 'to' : input('End date (to), optional: ') or '2025-01-07',
		# 'language' : input('Any specific language, optional: ') or 'en',
		# 'country' : 'in',#input('Any specific country, optional: ') or None,not work
		'category' : None ,
		'sort_by' : 'relevancy',#input('Sort by (relevancy, popularity, publishedAt): ') or 'relevancy',
		'page' : 1,
		'pagesize' : input('Number of articles you want, optional: ') or 12,
		'apiKey' : 'b4b83d6a9f21401181dce9f090a9107f'
       }

def get_news_from_API(url,parameters):
	try:
		news_from_api = requests.get(url, params = parameters)
		news_from_api.raise_for_status()
		return news_from_api
	except requests.exceptions.RequestException as i:
		print('An Eror occurd')
		return None

def print_news(articles):
	available_news_counter = 0
	for i,article in enumerate(articles):
		if article.get('source', {}).get('id') != None and available_news_counter<2:
			print(article.get('source'))
			print(f'Source: {article.get('source', {}).get('name')}')
			print(f'Author: {article.get('author')}')
			print(f'Title: {article.get('title')}')
			print(f'Url: {article.get('url')}')
			available_news_counter+=1
			print()

def main():
	url = ('https://newsapi.org/v2/everything')
	parameters_for_search = search_param()
	# print(parameters_for_search)
	news_from_api = get_news_from_API(url,parameters_for_search)
	# print(news_from_api)
	if news_from_api:#will execute if news_from_api is not None
		news_dict=news_from_api.json()
		# print(len(news_dict['articles']))
		# print(news_dict)
		# print(news_dict['status'])
		# print(news_dict['totalResults'])
		print_news(news_dict['articles'])
	

if __name__=='__main__':
	main()
	

# news=requests.get('https://newsapi.org/v2/everything?q=bitcoin&apiKey=b4b83d6a9f21401181dce9f090a9107f')
# # print(news.content)
# print(news)
# i=1
# for ar in news:
#     if i<2:
#         print(ar)
#         i+=1

# news = news.json()
# print(news['status'])
# print(news['totalResults'])

# artlist = [news['articles']]
# print(artlist[0][1])
# print(artlist[0][2]['source'])
# print(artlist[0][1]['url'])
# # for i in artlist:
# #     print(i)