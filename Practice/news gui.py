import sys
import os
# sys.path.append('E://My Programs/Python/Practice')
os.system('cls')
# news = __import__('news')
import news
import tkinter as tk
from PIL import Image,ImageTk

def get_news_from_newsapi(i,parameter):
	url = ('https://newsapi.org/v2/everything')
	
	news_from_api = news.get_news_from_API(url, parameter)
	if news_from_api:
		news_dict=news_from_api.json()
		articles = news_dict['articles']
	for article in articles:
			if article == articles[i]:
				value_to_return =  f'Title: {article.get('title')} \n Authour: {article.get('author')}'
	return value_to_return

m = tk.Tk()
m.title('Hi')#tittle of the window x=124,y=37 max padding x= 578/79 y= 341/342

m.geometry('1280x720')#it set the default size of the window
# m.maxsize(2000,1500)
m.resizable(False,False)#it will stop window from resizing
parameters_for_search = news.search_param()

news_from_Newsapi = str(get_news_from_newsapi(0,parameters_for_search))
news1 = tk.Label(text = news_from_Newsapi, background = 'dark grey', height = 11, width = 58)
news1.place(x = 8, y = 4)

news_from_Newsapi = str(get_news_from_newsapi(1,parameters_for_search))
news2 = tk.Label(text = news_from_Newsapi,  background = 'dark grey', height = 11, width = 58)
news2.place(x= 433, y = 4)

news_from_Newsapi = str(get_news_from_newsapi(2,parameters_for_search))
news3 = tk.Label(text = news_from_Newsapi, background = 'dark grey', height = 11, width = 58 )
news3.place(x = 858, y = 4)

news_from_Newsapi = str(get_news_from_newsapi(3,parameters_for_search))
news4 = tk.Label(text = news_from_Newsapi, background = 'dark grey', height = 11, width = 58)
news4.place(x = 8, y = 182)

news_from_Newsapi = str(get_news_from_newsapi(4,parameters_for_search))
news5 = tk.Label(text = news_from_Newsapi, background = 'dark grey', height = 11, width = 58, )
news5.place(x= 433, y = 182)

news_from_Newsapi = str(get_news_from_newsapi(5,parameters_for_search))
news6 = tk.Label(text = news_from_Newsapi, background = 'dark grey', height = 11, width = 58)
news6.place(x = 858, y = 182)

news_from_Newsapi = str(get_news_from_newsapi(6,parameters_for_search))
news7 = tk.Label(text = news_from_Newsapi, background = 'dark grey', height = 11, width = 58)
news7.place(x = 8, y = 361)

news_from_Newsapi = str(get_news_from_newsapi(7,parameters_for_search))
news8 = tk.Label(text = news_from_Newsapi, background = 'dark grey', height = 11, width = 58)
news8.place(x= 433, y = 361)

news_from_Newsapi = str(get_news_from_newsapi(8,parameters_for_search))
news9 = tk.Label(text = news_from_Newsapi, background = 'dark grey', height = 11, width = 58)
news9.place(x = 858, y = 361)

news_from_Newsapi = str(get_news_from_newsapi(9,parameters_for_search))
news10 = tk.Label(text = news_from_Newsapi, background = 'dark grey', height = 11, width = 58)
news10.place(x = 8, y = 542)

news_from_Newsapi = str(get_news_from_newsapi(10,parameters_for_search))
news11 = tk.Label(text = news_from_Newsapi, background = 'dark grey', height = 11, width = 58)
news11.place(x= 433, y = 542)

news_from_Newsapi = str(get_news_from_newsapi(11,parameters_for_search))
news12 = tk.Label(text = news_from_Newsapi, background = 'dark grey', height = 11, width = 58)
news12.place(x = 858, y = 542)




m.mainloop()