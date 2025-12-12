import time
import pandas as pd
from scrapers.arxiv import scrape_arxiv
from scrapers.google_news import scrape_google_news
from scrapers.google_search import scrape_google_search
from scrapers.duality import scrape_duality
from scrapers.polsky import scrape_polsky
from scrapers.chalmers import scrape_chalmers
from scrapers.basel import scrape_basel
from scrapers.news_mit import scrape_mit_news
from scrapers.qubitorbit import scrape_qubitorbit
def run_all_scrapers(queries=None):
    all_dfs = []

    print("🔬 Scraping arXiv...")
    try:
        df_arxiv = scrape_arxiv()
        df_arxiv["Source"] = "arXiv"
        all_dfs.append(df_arxiv)
    except Exception as e:
        print("❌ arXiv failed:", e)

    print("📰 Scraping Google News...")
    try:
        df_news = scrape_google_news(queries)
        df_news["Source"] = "Google News"
        all_dfs.append(df_news)
    except Exception as e:
        print("❌ Google News failed:", e)

    print("🌐 Scraping Google Search...")
    try:
        df_search = scrape_google_search(queries)
        df_search["Source"] = "Google Search"
        all_dfs.append(df_search)
    except Exception as e:
        print("❌ Google Search failed:", e)

    print("🚀 Scraping Duality...")
    try:
        df_duality = scrape_duality()
        df_duality["Source"] = "Duality"
        all_dfs.append(df_duality)
    except Exception as e:
        print("❌ Duality failed:", e)

    print("🎓 Scraping Polsky...")
    try:
        df_polsky = scrape_polsky()
        df_polsky["Source"] = "Polsky"
        all_dfs.append(df_polsky)
    except Exception as e:
        print("❌ Polsky failed:", e)

    print("🇸🇪 Scraping Chalmers...")
    try:
        df_chalmers = scrape_chalmers()
        df_chalmers["Source"] = "Chalmers"
        all_dfs.append(df_chalmers)
    except Exception as e:
        print("❌ Chalmers failed:", e)

    print("🇨🇭 Scraping Basel...")
    try:
        df_basel = scrape_basel()
        df_basel["Source"] = "Uni Basel"
        all_dfs.append(df_basel)
    except Exception as e:
        print("❌ Basel failed:", e)

    print("✅ Combining results...")
    if all_dfs:
        combined = pd.concat(all_dfs, ignore_index=True)
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        output_file = f"quantum_leads_{timestamp}.xlsx"
        combined.to_excel(output_file, index=False)
        print(f"💾 Saved to {output_file}")
        return output_file
    else:
        print("❌ No data collected.")
        return None

