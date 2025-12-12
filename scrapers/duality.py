import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_duality():
    base_url = "https://www.dualityaccelerator.com"
    news_url = base_url + "/news"
    response = requests.get(news_url)
    soup = BeautifulSoup(response.text, "html.parser")

    cards = soup.select(".et_pb_post")

    results = []

    for card in cards:
        title_tag = card.select_one("h2 a")
        desc_tag = card.select_one(".post-content p")
        date_tag = card.select_one(".published")

        if title_tag:
            title = title_tag.text.strip()
            link = title_tag["href"]
            desc = desc_tag.text.strip() if desc_tag else ""
            date = date_tag.text.strip() if date_tag else ""

            results.append({
                "Source": "Duality",
                "Name / Title": title,
                "Description": desc,
                "URL": link,
                "Published": date
            })

    return pd.DataFrame(results)
# duality scraper placeholder
