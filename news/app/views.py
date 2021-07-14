# importing render
from django.shortcuts import render
#import api
from newsapi import NewsApiClient

# Create your views here.
#defining index function
def index(request):
	newsapi = NewsApiClient(api_key ='7949417f5d8e45c18ddf98510ae4708c')#enter api key
	#get top headlines news
	top = newsapi.get_top_headlines(sources ='the-times-of-india')

	l = top['articles']
	desc =[]
	news =[]
	img =[]

	for i in range(len(l)):
		f = l[i]
		news.append(f['title'])
		desc.append(f['description'])
		img.append(f['urlToImage'])
	mylist = zip(news, desc, img)
	context ={"mylist":mylist}
#rendering template 
	return render(request, 'index.html', context)


	

