from flask import Flask,render_template
from newsapi import NewsApiClient
app = Flask(__name__)

app.route('/')
def index():
    return render_template('index.html')
@app.route('/bbc')
def Bbc():
    newsapi = NewsApiClient(api_key="40d18f3377d342d4a16854c146595ff9")
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")

    articles = topheadlines['articles']

    news = []
    desc = []
    img = []
    date=[]
    urls=[]

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        date.append(myarticles['publishedAt'])
        urls.append(myarticles['url'])

    mylist = zip(news, desc, img,date,urls)

    return render_template('bbc.html', context = mylist)

app.route('/')
def index():
    return render_template('index.html')
@app.route('/ansa')
def Ansanews():
    newsapi = NewsApiClient(api_key="40d18f3377d342d4a16854c146595ff9")
    topheadlines = newsapi.get_top_headlines(sources="ansa")

    articles = topheadlines['articles']

    news = []
    desc = []
    img = []
    date=[]
    urls=[]

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        date.append(myarticles['publishedAt'])
        urls.append(myarticles['url'])

    mylist = zip(news, desc, img,date,urls)

    return render_template('ansa.html', context = mylist)

if __name__ == "__main__":
    app.run(debug = True)
