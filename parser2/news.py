import datetime
import requests
from pprint import pprint
from bs4 import BeautifulSoup


def get_url(year, month, day, ordering):
    url = f"https://ru.sputnik.kg/news/" \
          f"{year}-{month}-{day}" \
          f"&order={ordering}"
    return url


def get_html(url):
    response = requests.get(url=url)
    return response


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all(
        "div",
        class_="list__item  ",
        limit=5
    )
    parserd_data = []
    for item in items:
        parserd_data.append({
            "title": item.find("div", class_="list__content").string.replace("\n", ""),
            "url": item.find("a", class_="list__title").get("href"),
            "time": item.find("span", class_="date").getText().strip(),
            "image": item.find("img").get("src").replace("small", "big")
        })

    return parserd_data


def parser():
    current_date = datetime.datetime.now()
    url = get_url(current_date.year, current_date.month, current_date.day, "time")
    html = get_html(url)
    parsed_data = get_data(html.text)
    return parsed_data