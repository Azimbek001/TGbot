import datetime
import requests
from bs4 import BeautifulSoup

URL = "https://www.securitylab.ru/news/"

HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image"
             "/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",

    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " 
                 "Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44"
}


def get_url(year, month, day, ordering):
    url = f"https://www.securitylab.ru/news/{year}-{month}-{day}" \
          f"&order={ordering}"
    return url


def get_html(url):
    response = requests.get(url=url, headers=HEADERS)
    return response


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all(
        'a', class_="article-card inline-card", limit=6
    )
    parserd_data = []
    for item in items:
        parserd_data.append({
            "title": item.find('h2').string.replace("\n", ""),
            "link": f"https://www.securitylab.ru{item.get('href')}",
            "description": item.find('p').string.replace("\n", ""),
            "date_from_html": item.find('time').string.replace("\n", "")
        })

    return parserd_data


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        news = []
        for i in range(1, 2):
            html = get_html(f"{URL}page1_{i}.php")
            current_page = get_data(html.text)
            news.extend(current_page)
        return news
    else:
        raise Exception("Ошибка!")