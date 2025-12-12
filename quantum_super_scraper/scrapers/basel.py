import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_basel():
    url = "https://physik.unibas.ch/en/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("article")

    results = []
    for article in articles:
        title_tag = article.find("h3")
        link_tag = article.find("a", href=True)
        date_tag = article.find("time")

        if title_tag and link_tag:
            title = title_tag.get_text(strip=True)
            link = "https://physik.unibas.ch" + link_tag["href"]
            date = date_tag.get_text(strip=True) if date_tag else ""
            results.append({
                "Source": "Uni Basel",
                "Title": title,
                "URL": link,
                "Date": date,
                "Summary": ""
            })

    return pd.DataFrame(results)

