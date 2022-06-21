import requests
from bs4 import BeautifulSoup
import csv

CSV = 'cards.csv'
HOST = 'https://magnit.ru'
URL = 'https://magnit.ru/journals/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='magazine-card')
    cards = []

    for item in items:
        cards.append(
            {
                'title': item.find('p', class_='magazine-card__title').get_text(),
                'link-product': HOST + item.find('a', class_='magazine-card__link').get('href'),
                'data': item.find('p', class_='magazine-card__text').get_text(),
                'card-image': HOST + item.find('div', class_='magazine-card__content').find('img').get('data-src')
            }
        )
    return cards

def save_doc(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter= ';')
        writer.writerow(['Название', 'Ссылка на продукт', 'Дата', 'Изображение'])
        for item in items:
            writer.writerow([item['title'], item['link-product'], item['data'], item['card-image']])



#html = get_html(URL)
#print(get_content(html.text))

def parser():
    html = get_html(URL)
    cards = []
    if html.status_code == 200:
        cards.extend(get_content(html.text))
        save_doc(cards, CSV)
    else:
        print('Error')

parser()