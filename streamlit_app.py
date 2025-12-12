import streamlit as st
from main import run_scraper

st.set_page_config(page_title="Quantum Startup Super Scraper", layout="wide")

st.title("🧠 Quantum Startup Super Scraper")
st.markdown("Find stealth quantum startups from university spinouts, incubator blogs, and deep web articles.")

if st.button("🔍 Run Scraper"):
    with st.spinner("Scraping sources..."):
        leads = run_scraper()
        if not leads.empty:
            st.success(f"✅ {len(leads)} potential leads found.")
            st.dataframe(leads)
        else:
            st.warning("⚠️ No new leads found.")