import pandas as pd
from .ab_testing import ab_test_conversion

def segment_results(df: pd.DataFrame, segment_col: str) -> pd.DataFrame:
    if segment_col not in df.columns:
        raise ValueError(f"Column '{segment_col}' not found in data")

    rows = []
    for seg in sorted(df[segment_col].dropna().unique()):
        sub = df[df[segment_col] == seg].copy()
        res = ab_test_conversion(sub)
        rows.append({
            "segment": seg,
            "n_a": res["n_a"], "n_b": res["n_b"],
            "cr_a": res["cr_a"], "cr_b": res["cr_b"],
            "abs_lift": res["abs_lift"],
            "rel_lift_%": res["rel_lift"] * 100 if res["rel_lift"] != float("inf") else float("inf"),
            "p_value": res["p_value"],
        })

    return pd.DataFrame(rows)
