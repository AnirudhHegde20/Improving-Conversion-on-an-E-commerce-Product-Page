import pandas as pd

def conversion_rate(df: pd.DataFrame) -> float:
    return df["converted"].mean()

def bounce_rate(df: pd.DataFrame) -> float:
    if "bounce" not in df.columns:
        return float("nan")
    return df["bounce"].mean()

def aov(df: pd.DataFrame) -> float:
    # AOV among converted purchases
    if "order_value" not in df.columns:
        return float("nan")
    purchases = df[df["converted"] == 1]
    if len(purchases) == 0:
        return 0.0
    return purchases["order_value"].mean()

def add_to_cart_rate(df: pd.DataFrame) -> float:
    # Optional, if you have add_to_cart column (0/1)
    if "add_to_cart" not in df.columns:
        return float("nan")
    return df["add_to_cart"].mean()
