import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_qubitorbit():
    url = "https://qubitorbit.com/category/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("div", class_="td-module-container")

    results = []
    for article in articles:
        title_tag = article.find("h3")
        link_tag = article.find("a")
        date_tag = article.find("time")

        if title_tag and link_tag:
            title = title_tag.get_text(strip=True)
            link = link_tag["href"]
            date = date_tag.get_text(strip=True) if date_tag else ""
            results.append({
                "Source": "QubitOrbit",
                "Title": title,
                "URL": link,
                "Date": date,
                "Summary": ""
            })

    return pd.DataFrame(results)

