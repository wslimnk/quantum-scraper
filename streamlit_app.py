import streamlit as st
import pandas as pd
from io import BytesIO
from main import run_scraper, smart_queries
import datetime

st.set_page_config(page_title="Quantum Startup Super Scraper", layout="wide")

st.title("🧠 Quantum Startup Super Scraper")
st.markdown("Find stealth quantum startups from university spinouts, incubator blogs, and deep web articles.")

st.markdown("""Click the button below to run all scrapers (arXiv, Google News/Search, university blogs) and automatically save a spreadsheet with the combined leads.""")

# When the button is clicked
if st.button("🔍 Run Scraper"):
    with st.spinner("Scraping sources..."):
        leads_df, output_file = run_scraper(queries=smart_queries())

        if isinstance(leads_df, pd.DataFrame) and not leads_df.empty:
            st.success(f"✅ {len(leads_df)} potential leads found.")
            st.dataframe(leads_df)

            buffer = BytesIO()
            leads_df.to_excel(buffer, index=False, engine="openpyxl")
            buffer.seek(0)

            st.download_button(
                label="⬇️ Download Excel",
                data=buffer,
                file_name=output_file or "quantum_leads.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
        else:
            st.warning("⚠️ No new leads found or invalid format.")

