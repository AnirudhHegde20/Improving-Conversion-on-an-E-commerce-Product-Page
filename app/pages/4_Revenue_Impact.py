import streamlit as st
from src.data import load_data
from src.ab_testing import ab_test_binary_metric
from src.impact import annual_revenue_uplift
from src.metrics import aov_from_data



st.title("Revenue Impact")

df = load_data("data/processed/ab_test_data.csv")
res = ab_test_binary_metric(df, "purchase")

st.subheader("Inputs")
daily_sessions = st.number_input("Daily product page sessions", min_value=1000, max_value=5000000, value=40000, step=1000)
aov = st.number_input("Assumed Average Order Value (AOV) $", min_value=1.0, max_value=10000.0, value=75.0, step=1.0)

baseline = res["rate_a"]
rel_lift = res["rel_lift"] if res["rel_lift"] != float("inf") else 0.0

uplift = annual_revenue_uplift(
    daily_sessions=int(daily_sessions),
    baseline_purchase_rate=float(baseline),
    rel_lift=float(rel_lift),
    aov=float(aov),
    days=365
)

st.divider()
st.metric("Estimated annual revenue uplift", f"${uplift:,.0f}")
st.caption("Assumes the observed lift holds after rollout. In real deployments, ship gradually and monitor.")
default_aov = aov_from_data(df)
if default_aov == 0.0 or default_aov != default_aov:  # handles 0 or nan
    default_aov = 75.0

aov = st.number_input("Average Order Value (AOV) $", min_value=1.0, max_value=10000.0, value=float(default_aov), step=1.0)