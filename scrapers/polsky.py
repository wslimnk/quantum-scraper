import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_polsky():
    url = "https://polsky.uchicago.edu/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("div", class_="news-item")

    results = []
    for article in articles:
        title_tag = article.find("h3")
        link_tag = article.find("a")
        date_tag = article.find("span", class_="date")

        if title_tag and link_tag:
            title = title_tag.get_text(strip=True)
            link = link_tag["href"]
            date = date_tag.get_text(strip=True) if date_tag else ""
            results.append({
                "Source": "Polsky Center",
                "Title": title,
                "URL": link,
                "Date": date,
                "Summary": ""
            })

    return pd.DataFrame(results)

