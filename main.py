
import requests
from bs4 import BeautifulSoup
import pandas as pd
from flask import Flask, render_template

url = "http://www.ynet.co.il/Integration/StoryRss1854.xml"

resp = requests.get(url)
soup = BeautifulSoup(resp.content, features="xml")
items = soup.findAll('item')
news_items = []
for item in items:
    news_item = {}

    news_item['title'] = item.title.text
    news_item['link'] = item.link.text
    news_item['pubDate'] = item.pubDate.text

    news_items.append(news_item)
    print(news_item)
# break


df = pd.DataFrame(news_items, columns=['title', 'link', 'pubDate'])

df.to_csv('data.csv', index=False, encoding='utf-8')

a = pd.read_csv("data.csv", encoding='utf-8')

a.to_html("index.html")


app = Flask(__name__)


@app.route('/')
def Tabel():
    return render_template("index.html")

if __name__ == '__main__':
   # app.run(host="127.0.0.1")
       app.run(host="127.0.0.1", port=6060)



