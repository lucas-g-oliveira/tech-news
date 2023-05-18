from tech_news import database
from datetime import datetime as time


# Requisito 7
def search_by_title(title):
    data = []
    all_news = database.find_news()
    for news in all_news:
        if str(title).lower() in str(news["title"]).lower():
            x = {"title": news["title"], "url": news["url"]}
            data.append(tuple(x.values()))
    return data


# Requisito 8
def search_by_date(date):
    try:
        d, m, y = [int(i) for i in str(date).split("-")[::-1]]
        param = time(year=y, month=m, day=d).strftime("%d/%m/%Y")
        data = []
        all_news = database.find_news()
        for news in all_news:
            if news["timestamp"] == param:
                x = {"title": news["title"], "url": news["url"]}
                data.append(tuple(x.values()))
        return data
    except Exception:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    data = []
    all_news = database.find_news()
    for news in all_news:
        if str(category).lower() in str(news["category"]).lower():
            x = {"title": news["title"], "url": news["url"]}
            data.append(tuple(x.values()))
    return data


# print(search_by_date("2022-04-07"))
