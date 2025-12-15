import streamlit as st
from src.data import load_data
from src.segmentation import segment_results

st.title("Segmentation")

df = load_data("data/processed/ab_test_data.csv")

segment_col = st.selectbox("Segment by", ["device_type", "region"])
metric_col = st.selectbox("Metric", ["purchase", "added_to_cart"])

seg = segment_results(df, segment_col, metric_col)

st.dataframe(seg, use_container_width=True)

st.divider()
st.markdown("""
**How to use this:**
- Look for segments with meaningful lift + low p-value  
- Real rollouts are often phased (example: ship on Mobile first)  
""")
