import requests


DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}


def fetch_html(url, *, params=None, timeout=15):
    """Return response text with proxy usage disabled for consistency."""

    session = requests.Session()
    session.trust_env = False  # ignore proxy settings that can block scraping
    response = session.get(url, params=params, headers=DEFAULT_HEADERS, timeout=timeout)
    response.raise_for_status()
    return response.text
