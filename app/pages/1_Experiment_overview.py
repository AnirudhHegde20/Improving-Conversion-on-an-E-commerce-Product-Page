import streamlit as st
from src.data import load_data
from src.metrics import purchase_rate, add_to_cart_rate, avg_time_spent

st.title("Overview")

df = load_data("data/processed/ab_test_data.csv")
a = df[df["experiment_group"] == "A"]
b = df[df["experiment_group"] == "B"]

c1, c2, c3 = st.columns(3)
c1.metric("Total sessions", f"{len(df):,}")
c2.metric("Groups", "A / B")
c3.metric("Overall purchase rate", f"{purchase_rate(df)*100:.2f}%")

st.subheader("Key metrics by group")

colA, colB = st.columns(2)
with colA:
    st.write("### Control (A)")
    st.write(f"Purchase rate: **{purchase_rate(a)*100:.2f}%**")
    st.write(f"Add-to-cart rate: **{add_to_cart_rate(a)*100:.2f}%**")
    st.write(f"Avg time spent: **{avg_time_spent(a):.2f}s**")

with colB:
    st.write("### Treatment (B)")
    st.write(f"Purchase rate: **{purchase_rate(b)*100:.2f}%**")
    st.write(f"Add-to-cart rate: **{add_to_cart_rate(b)*100:.2f}%**")
    st.write(f"Avg time spent: **{avg_time_spent(b):.2f}s**")

st.divider()
st.subheader("What this simulates")
st.markdown("""
- **Primary outcome:** Purchase (conversion)  
- **Secondary funnel:** Add to cart  
- **Engagement proxy:** Time spent  
- **Segments available:** Device type and region  
""")
