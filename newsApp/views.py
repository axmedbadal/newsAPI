from django.shortcuts import render
from newsapi import NewsApiClient
from newsapi import NewsApiClient

def index(request):
    newsApi = NewsApiClient(api_key='d84daa343f0f4f169b125e6af6300c75') 
    headLines = newsApi.get_top_headlines(sources='ign')
    articles = headLines['articles']
    desc = []
    news = [ ]
    img = []
    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
    mylist = zip(news,desc,img)

    return render(request,"main/index.html",context={'mylist':mylist})
        