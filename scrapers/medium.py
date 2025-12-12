import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_medium():
    query = "quantum startup founder site:medium.com"
    url = f"https://www.google.com/search?q={query}&num=20"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.select("a")
    results = []

    for link in links:
        href = link.get("href", "")
        if "/url?q=" in href and "medium.com" in href:
            actual_url = href.split("/url?q=")[-1].split("&")[0]
            text = link.get_text(strip=True)
            if actual_url and text:
                results.append({
                    "Source": "Medium",
                    "Title": text,
                    "URL": actual_url,
                    "Date": "",
                    "Summary": ""
                })

    return pd.DataFrame(results)

