import requests
from parsel import Selector
import time


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(
            url=url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        if response.status_code != 200:
            return None
        return response.text
    except (Exception, requests.exceptions.Timeout):
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    links = selector.css(
        "article .post-inner .cs-overlay-link::attr(href)"
    ).getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    try:
        next_page = selector.css(".pagination .next::attr(href)").get()
        return next_page
    except Exception:
        None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


# text_html = fetch("https://blog.betrybe.com/")
# link = scrape_next_page_link(text_html)
# print(link)
