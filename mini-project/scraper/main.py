import requests
from bs4 import BeautifulSoup
import json


url='http://quotes.toscrape.com'
articles_data=[]
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features='html.parser')
    articles = soup.find_all('div', class_='quote')
    for article in articles:
        title=article.get_text()
        description=article.find('span', class_='text').get_text()
        link=article.find('a')['href']
        print(description)
        print(link)
        print(title)
        articles_data.append({
        'title': title,
        'description': description,
        'link': link
        })
else:
    print('erreur de connexion au site web')

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(articles_data, f, ensure_ascii=False, indent=4)
print('les donnees ont ete enregistre dans le fichier data.json')
