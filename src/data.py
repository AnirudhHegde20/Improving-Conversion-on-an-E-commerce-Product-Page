import pandas as pd

REQUIRED = {
    "experiment_group",
    "purchase",
    "added_to_cart",
    "device_type",
    "region",
    "time_spent_seconds",
}

def load_data(path_or_buffer) -> pd.DataFrame:
    df = pd.read_csv(path_or_buffer)

    missing = REQUIRED - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Normalize group
    df["experiment_group"] = df["experiment_group"].astype(str).str.upper().str.strip()
    df = df[df["experiment_group"].isin(["A", "B"])].copy()

    # Ensure binary ints
    df["purchase"] = df["purchase"].astype(int)
    df["added_to_cart"] = df["added_to_cart"].astype(int)

    # Normalize categoricals
    df["device_type"] = df["device_type"].astype(str).str.strip()
    df["region"] = df["region"].astype(str).str.strip()

    # Numeric
    df["time_spent_seconds"] = pd.to_numeric(df["time_spent_seconds"], errors="coerce").fillna(0.0)

    return df
