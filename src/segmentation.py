import pandas as pd
from .ab_testing import ab_test_binary_metric

def segment_results(df: pd.DataFrame, segment_col: str, metric_col: str) -> pd.DataFrame:
    if segment_col not in df.columns:
        raise ValueError(f"Column '{segment_col}' not found")

    rows = []
    for seg in sorted(df[segment_col].dropna().unique()):
        sub = df[df[segment_col] == seg].copy()
        res = ab_test_binary_metric(sub, metric_col)

        rel_lift_pct = res["rel_lift"] * 100 if res["rel_lift"] != float("inf") else float("inf")

        rows.append({
            "segment": seg,
            "n_a": res["n_a"], "n_b": res["n_b"],
            "A_rate": res["rate_a"],
            "B_rate": res["rate_b"],
            "abs_lift_pp": res["abs_lift"] * 100,
            "rel_lift_%": rel_lift_pct,
            "p_value": res["p_value"]
        })

    out = pd.DataFrame(rows)
    return out.sort_values(["p_value", "rel_lift_%"], ascending=[True, False])
