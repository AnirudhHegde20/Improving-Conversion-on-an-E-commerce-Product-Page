import pandas as pd

def rate(series: pd.Series) -> float:
    return float(series.mean()) if len(series) else 0.0

def purchase_rate(df: pd.DataFrame) -> float:
    return rate(df["purchase"])

def add_to_cart_rate(df: pd.DataFrame) -> float:
    return rate(df["added_to_cart"])

def avg_time_spent(df: pd.DataFrame) -> float:
    return float(df["time_spent_seconds"].mean()) if len(df) else 0.0
def aov_from_data(df: pd.DataFrame) -> float:
    if "order_value" not in df.columns:
        return float("nan")
    purchases = df[df["purchase"] == 1]
    if len(purchases) == 0:
        return 0.0
    return float(purchases["order_value"].mean())
