import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from src.data import load_data
from src.data import load_data


st.set_page_config(page_title="A/B Test Dashboard", layout="wide")

st.title("E-commerce Product Page A/B Test Dashboard")
st.caption("Conversion, add-to-cart, time spent, segmentation, and revenue impact based on your synthetic dataset.")

default_path = Path("data/processed/ab_test_data.csv")

with st.sidebar:
    st.header("Data")
    uploaded = st.file_uploader("Upload CSV (optional)", type=["csv"])
    st.info("If no upload, the app uses data/processed/ab_test_data.csv")

if uploaded is not None:
    df = load_data(uploaded)
else:
    if not default_path.exists():
        st.error("Dataset not found. Place it at data/processed/ab_test_data.csv or upload it.")
        st.stop()
    df = load_data(str(default_path))

st.success(f"Loaded {len(df):,} rows")
st.write("Columns:", list(df.columns))
st.markdown("Use the pages in the sidebar to view results.")
