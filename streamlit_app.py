import streamlit as st
import pandas as pd   # ⬅️ THIS LINE WAS MISSING
from main import run_scraper
import datetime


st.set_page_config(page_title="Quantum Startup Super Scraper", layout="wide")

st.title("🧠 Quantum Startup Super Scraper")
st.markdown("Find stealth quantum startups from university spinouts, incubator blogs, and deep web articles.")

import pandas as pd  # Add this at the top if missing

if isinstance(leads, pd.DataFrame) and not leads.empty:
    st.success(f"✅ {len(leads)} potential leads found.")
    st.dataframe(leads)
else:
    st.warning("⚠️ No new leads found or invalid format.")
