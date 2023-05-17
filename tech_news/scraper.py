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
    s = Selector(html_content)
    reading_time = s.css(".meta-reading-time::text").get()
    summary = Selector(s.css(".entry-content p").get())
    summary = summary.xpath("string()").get().replace("\xa0", "")

    post = {}
    post["url"] = s.css("head > link[rel=canonical]::attr(href)").get()
    post["title"] = s.css("h1::text").get().replace('\xa0', "").rstrip()
    post["timestamp"] = s.css(".post-meta .meta-date::text").get()
    post["writer"] = s.css(".meta-author a::text").get()
    post["reading_time"] = int(reading_time.split(" ")[0])
    post["summary"] = summary.rstrip()
    post["category"] = s.css(".category-style > .label::text").get()
    return post


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
