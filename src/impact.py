import pandas as pd

def annual_revenue_uplift(
    baseline_cr: float,
    rel_lift: float,
    daily_sessions: int,
    aov: float,
    days: int = 365
) -> float:
    """
    rel_lift is relative (e.g., 0.04 for +4% relative conversion lift)
    """
    incremental_conversions_per_day = daily_sessions * baseline_cr * rel_lift
    return incremental_conversions_per_day * aov * days

def inferred_aov(df: pd.DataFrame) -> float:
    if "order_value" not in df.columns:
        return float("nan")
    purchases = df[df["converted"] == 1]
    if len(purchases) == 0:
        return 0.0
    return purchases["order_value"].mean()
