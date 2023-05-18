from tech_news import database


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
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    data = []
    all_news = database.find_news()
    for news in all_news:
        if str(category).lower() in str(news["category"]).lower():
            x = {"title": news["title"], "url": news["url"]}
            data.append(tuple(x.values()))
    return data


# print(search_by_title("notícia bacana 2"))
