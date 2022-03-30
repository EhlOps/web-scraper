# tasks.py

from time import time
from celery import Celery

import requests
from bs4 import BeautifulSoup
import json

from datetime import datetime

from celery.schedules import crontab

# Defining app name
app = Celery('tasks')

# Save function from scraper.py
@app.task
def save_function(article_list):
    
    # Timestamp and filename
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    filename = 'articles-{}.json'.format(timestamp)

    with open(filename, 'w') as outfile:
        json.dump(article_list, outfile)

# RSS function from scraper.py
@app.task
def rss():
    #Creates an article list
    article_list = []

    try:
        # Gets data from site as XML
        r = requests.get('https://news.ycombinator.com/rss')
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
                'published': published,
                'created_at': str(datetime.now()),
                'source': 'HackerNews RSS'
            }
            article_list.append(article)

        # Returns the article list
        return save_function(article_list)

    except Exception as e:
        print('Scraping failed, see exception:')
        print(e)

# Scheduled task execution
app.conf.beat_schedule = {
    'scraping-task-one-min': {
        'task': 'tasks.rss',
        'schedule': crontab()
    }
}