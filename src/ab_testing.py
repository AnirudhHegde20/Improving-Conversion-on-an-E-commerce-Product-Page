import math
import pandas as pd
from scipy import stats

def ztest_proportions(success_a: int, n_a: int, success_b: int, n_b: int):
    # Two-proportion z-test (two-sided)
    p1 = success_a / n_a
    p2 = success_b / n_b
    p_pool = (success_a + success_b) / (n_a + n_b)

    se = math.sqrt(p_pool * (1 - p_pool) * (1/n_a + 1/n_b))
    if se == 0:
        return 0.0, 1.0

    z = (p2 - p1) / se
    p_value = 2 * (1 - stats.norm.cdf(abs(z)))
    return z, p_value

def ab_test_conversion(df: pd.DataFrame):
    a = df[df["variant"] == "A"]
    b = df[df["variant"] == "B"]

    n_a, n_b = len(a), len(b)
    s_a, s_b = int(a["converted"].sum()), int(b["converted"].sum())

    cr_a = s_a / n_a if n_a else 0
    cr_b = s_b / n_b if n_b else 0

    abs_lift = cr_b - cr_a
    rel_lift = (abs_lift / cr_a) if cr_a > 0 else float("inf")

    z, p = ztest_proportions(s_a, n_a, s_b, n_b)

    return {
        "n_a": n_a, "n_b": n_b,
        "success_a": s_a, "success_b": s_b,
        "cr_a": cr_a, "cr_b": cr_b,
        "abs_lift": abs_lift,
        "rel_lift": rel_lift,
        "z_stat": z,
        "p_value": p,
    }
