import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_chalmers():
    url = "https://www.chalmers.se/en/current/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("li", class_="card news-card")

    results = []
    for article in articles:
        title_tag = article.find("span", class_="card__heading")
        link_tag = article.find("a", href=True)
        date_tag = article.find("span", class_="card__time")

        if title_tag and link_tag:
            title = title_tag.get_text(strip=True)
            link = "https://www.chalmers.se" + link_tag["href"]
            date = date_tag.get_text(strip=True) if date_tag else ""
            results.append({
                "Source": "Chalmers University",
                "Title": title,
                "URL": link,
                "Date": date,
                "Summary": ""
            })

    return pd.DataFrame(results)
# chalmers scraper placeholder
