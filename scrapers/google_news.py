from bs4 import BeautifulSoup
import pandas as pd
from scrapers.http import fetch_html


def scrape_google_news(queries=None):
    """Scrape Google search (news vertical) results for quantum startup queries.

    The function now accepts an optional ``queries`` list passed in from the
    Streamlit app. If ``None`` is provided, we fall back to a sensible default
    list that targets accelerators, incubators, and grant/award announcements.
    """

    if not queries:
        queries = [
            "quantum startup accelerator",
            "quantum incubator winner",
            "quantum phd founder",

            "quantum grant prize innovation",
            "quantum AND (incubator OR accelerator OR spin-off OR award OR grant OR prize)",
        ]

    results = []

    for query in queries:
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}&num=10&hl=en"
        try:
            html = fetch_html(url)
        except Exception:
            continue
        soup = BeautifulSoup(html, "html.parser")

        for result in soup.select(".tF2Cxc"):
            title = result.select_one("h3")
            link = result.select_one("a")["href"]
            desc = result.select_one(".VwiC3b")

            if title and link:
                results.append({
                    "Source": "Google News",
                    "Name / Title": title.text,
                    "Description": desc.text if desc else "",
                    "URL": link,
                    "Published": ""
                })

    df = pd.DataFrame(results)
    return df

