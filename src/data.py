import pandas as pd

REQUIRED_COLS = {"variant", "converted"}

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    missing = REQUIRED_COLS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Normalize
    df["variant"] = df["variant"].astype(str).str.upper().str.strip()
    df = df[df["variant"].isin(["A", "B"])].copy()

    df["converted"] = df["converted"].astype(int)

    # Optional columns
    if "order_value" in df.columns:
        df["order_value"] = df["order_value"].fillna(0).astype(float)

    if "bounce" in df.columns:
        df["bounce"] = df["bounce"].fillna(0).astype(int)

    return df
