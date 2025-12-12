import pandas as pd
from bs4 import BeautifulSoup
from scrapers.http import fetch_html


def _clean_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text(" ", strip=True)


def scrape_duality():
    """Fetch Duality Accelerator news posts (includes Photon Queue example)."""

    base_url = "https://www.dualityaccelerator.com"
    api_url = f"{base_url}/wp-json/wp/v2/posts"

    results = []

    try:
        # Pull the latest 100 posts to include archived announcements.
        raw = fetch_html(api_url, params={"per_page": 100})
        posts = pd.read_json(raw)
        for _, row in posts.iterrows():
            title = _clean_html(row.get("title", {}).get("rendered", ""))
            link = row.get("link", "")
            desc = _clean_html(row.get("excerpt", {}).get("rendered", ""))
            date = row.get("date", "")

            if title and link:
                results.append({
                    "Source": "Duality",
                    "Name / Title": title,
                    "Description": desc,
                    "URL": link,
                    "Published": date,
                })

    except Exception:
        # Fall back to simple HTML scrape if the API is unavailable.
        news_html = fetch_html(f"{base_url}/news")
        soup = BeautifulSoup(news_html, "html.parser")
        cards = soup.select(".et_pb_post")

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
                    "Published": date,
                })

    return pd.DataFrame(results)
