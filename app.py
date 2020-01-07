from flask import Flask,render_template
from newsapi import NewsApiClient
app = Flask(__name__)

app.route('/')
def index():
    return render_template('index.html')
@app.route('/bbc')
def Bbc():
    newsapi = NewsApiClient(api_key="c40d6d5c48504741980b4e27910dd4a4")
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")

    articles = topheadlines['articles']

    news = []
    desc = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)

    return render_template('bbc.html', context = mylist)
