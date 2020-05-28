import urllib
import requests
from bs4 import BeautifulSoup


USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0"
headers = {"user-agent":USER_AGENT}

query = f"glassdoor.com Seaboard reviews".replace(' ', '+')
# query2 = f"indeed facebook reviews".replace(' ', '+')
URL = f"https://google.com/search?q={query}&lr=lang_en&hl=en" #https://sites.google.com/site/tomihasa/google-language-codes

url = requests.get(URL, headers=headers)
soup = BeautifulSoup(url.content, "html.parser")

for g in soup.find_all('div', class_='rc'): #loop through every google search result
    # link_and_title = g.find_all('a', limit=1) #get the first link within current search result
    rating_and_reviews = g.find_all('div', class_="dhIWPd f") #get the first link within current search result
    if rating_and_reviews:
        print(rating_and_reviews[0].text)
    # if link_and_title:
    #     link = link_and_title[0]['href'] #get the href of the first list item
    #     title = g.find('h3').text #get the title
    #     print(link, title, rating_and_reviews)