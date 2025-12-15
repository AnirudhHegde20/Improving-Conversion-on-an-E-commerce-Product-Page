import streamlit as st
from src.data import load_data
from src.ab_testing import ab_test_binary_metric

st.title("A/B Test Results")

df = load_data("data/processed/ab_test_data.csv")

metric = st.selectbox("Choose metric", ["purchase", "added_to_cart"])
res = ab_test_binary_metric(df, metric)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Rate (A)", f"{res['rate_a']*100:.2f}%")
c2.metric("Rate (B)", f"{res['rate_b']*100:.2f}%")
c3.metric("Lift (pp)", f"{res['abs_lift']*100:.2f}")
c4.metric("p-value", f"{res['p_value']:.4f}")

st.divider()
st.subheader("Decision helper")
min_rel_lift = st.slider("Minimum relative lift to ship (%)", 0.0, 50.0, 2.0, 0.5)
alpha = st.selectbox("Significance level (alpha)", [0.10, 0.05, 0.01], index=1)

rel_lift_pct = (res["rel_lift"] * 100) if res["rel_lift"] != float("inf") else 0.0
ship = (rel_lift_pct >= min_rel_lift) and (res["p_value"] <= alpha)

if ship:
    st.success(f"Recommendation: SHIP for metric='{metric}' (relative lift={rel_lift_pct:.2f}%, p={res['p_value']:.4f})")
else:
    st.warning(f"Recommendation: HOLD (relative lift={rel_lift_pct:.2f}%, p={res['p_value']:.4f})")
