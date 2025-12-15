import math
import pandas as pd
from scipy import stats

def ztest_proportions(success_a: int, n_a: int, success_b: int, n_b: int):
    p1 = success_a / n_a
    p2 = success_b / n_b
    p_pool = (success_a + success_b) / (n_a + n_b)

    se = math.sqrt(p_pool * (1 - p_pool) * (1/n_a + 1/n_b))
    if se == 0:
        return 0.0, 1.0

    z = (p2 - p1) / se
    p_value = 2 * (1 - stats.norm.cdf(abs(z)))
    return z, p_value

def ab_test_binary_metric(df: pd.DataFrame, col: str):
    a = df[df["experiment_group"] == "A"]
    b = df[df["experiment_group"] == "B"]

    n_a, n_b = len(a), len(b)
    s_a, s_b = int(a[col].sum()), int(b[col].sum())

    r_a = s_a / n_a if n_a else 0.0
    r_b = s_b / n_b if n_b else 0.0

    abs_lift = r_b - r_a
    rel_lift = (abs_lift / r_a) if r_a > 0 else float("inf")

    z, p = ztest_proportions(s_a, n_a, s_b, n_b)

    return {
        "metric": col,
        "n_a": n_a, "n_b": n_b,
        "success_a": s_a, "success_b": s_b,
        "rate_a": r_a, "rate_b": r_b,
        "abs_lift": abs_lift,
        "rel_lift": rel_lift,
        "z_stat": z,
        "p_value": p
    }
