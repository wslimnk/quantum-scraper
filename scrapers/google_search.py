import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def scrape_google_search(queries=None):
    """Scrape standard Google results for quantum startup discovery queries.

    Accepts an optional ``queries`` list. If none is provided we fall back to a
    curated set that targets accelerators, university spinouts, and awards.
    """

    if not queries:
        queries = [
            "quantum startup site:dualityaccelerator.com",
            "quantum site:polsky.uchicago.edu",
            "quantum spin-off site:unibas.ch",
            "quantum incubator site:chalmers.se",
            "quantum phd founder site:medium.com",
            "quantum AND (accelerator OR incubator OR phd OR spin-off)",
            "quantum + recently launched startup",
            "quantum university lab commercialization",
            "quantum site:news.mit.edu",
            "quantum grant OR prize",
            "quantum AND startup AND (ETH OR Zurich OR EPFL OR Imperial OR TU Munich OR Delft)",
            "quantum site:qubitorbit.com",
            "quantum site:cam.ac.uk",
            "quantum site:ox.ac.uk",
            "quantum startup site:linkedin.com",
            "quantum early-stage university startup",
            "quantum award startup site:edu",
            "quantum innovation challenge winner",
        ]

    results = []

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    for query in queries:
        print(f"🔍 Scraping: {query}")
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}&num=10&hl=en"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        for result in soup.select(".tF2Cxc"):
            title = result.select_one("h3")
            link = result.select_one("a")["href"]
            desc = result.select_one(".VwiC3b")

            if title and link:
                results.append({
                    "Source": "Google Search",
                    "Name / Title": title.text.strip(),
                    "Description": desc.text.strip() if desc else "",
                    "URL": link.strip(),
                    "Published": ""
                })

        time.sleep(2)  # avoid being blocked

    df = pd.DataFrame(results)
    return df


