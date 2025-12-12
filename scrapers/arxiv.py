import feedparser
import pandas as pd

def scrape_arxiv():
    base_url = "http://export.arxiv.org/api/query?"
    query = "quantum startup OR quantum spin-off"
    url = f"{base_url}search_query=all:{query}&start=0&max_results=30&sortBy=submittedDate&sortOrder=descending"

    feed = feedparser.parse(url)
    entries = feed.entries

import requests
import pandas as pd
from bs4 import BeautifulSoup

def scrape_arxiv():
    url = "http://export.arxiv.org/api/query"
    params = {
        "search_query": "all:quantum AND startup",
        "start": 0,
        "max_results": 20,
        "sortBy": "lastUpdatedDate",
        "sortOrder": "descending"
    }

    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.content, "xml")

    results = []
    for entry in soup.find_all("entry"):
      import requests
import pandas as pd
from bs4 import BeautifulSoup

def scrape_arxiv():
    url = "http://export.arxiv.org/api/query"
    params = {
        "search_query": "all:quantum AND startup",
        "start": 0,
        "max_results": 20,
        "sortBy": "lastUpdatedDate",
        "sortOrder": "descending"
    }

    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.content, "xml")

    results = []
    for entry in soup.find_all("entry"):
        title = entry.title.text.strip()
        summary = entry.summary.text.strip().replace("\n", " ")
        published = entry.published.text.strip()
        link = entry.id.text.strip()

        results.append({
            "Source": "arXiv",
            "Name / Title": title,
            "Description": summary,
            "URL": link,
            "Published": published
        })

    return pd.DataFrame(results)
