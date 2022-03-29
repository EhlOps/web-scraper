# scraper.py

import requests
from bs4 import BeautifulSoup
import json

def rss(url):
    #Creates an article list
    article_list = []

    try:
        # Gets data from site as XML
        r = requests.get(url)
        print('Success: ', r.status_code)
        soup = BeautifulSoup(r.content, features='xml')
        
        # Only gets items from  XML
        articles  = soup.findAll('item')

        # Creates and initializes variables for title, link and date published
        for a in articles:
            title = a.find('title').text
            link = a.find('link').text
            published = a.find('pubDate').text

            # Creates a dictionary called 'article'
            article = {
                'title': title,
                'link': link,
                'published': published
            }
            article_list.append(article)

        # Returns the article list
        return save_function(article_list)

    except Exception as e:
        print('Scraping failed, see exception:')
        print(e)

def save_function(article_list):
    with open('articles.txt', 'w') as outfile:
        json.dump(article_list, outfile)

print('Scraping started')
rss('https://news.ycombinator.com/rss')
print('Scraping complete')