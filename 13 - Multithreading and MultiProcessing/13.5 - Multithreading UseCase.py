# Real-world Example :- Multithreading for I/O-bound tasks 
# Scenario: Web Scraping:- involves making numerous network requests to fetch web pages. These tasks are I/O bound b/c they spend a lot of time waiting for responses from servers. Multithreading can significantly improve the performance by allowing multiple webpages to be fetched concurrently.


import threading
import time
import requests
from bs4 import BeautifulSoup

urls = [
  'https://docs.langchain.com/oss/python/langchain/overview',
  'https://docs.langchain.com/oss/python/langchain/models',
  'https://docs.langchain.com/oss/python/langgraph/overview'
]

def fetch_content(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  print(f'Fetched character length:{len(soup.text)} characters from {url}')
  
threads = []

for url in urls:
  thread = threading.Thread(target=fetch_content, args=(url,))
  threads.append(thread)
  thread.start()
  
for thread in threads:
  thread.join()
  
print('All webpages scraped')