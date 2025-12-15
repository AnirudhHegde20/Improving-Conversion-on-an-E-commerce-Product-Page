def annual_revenue_uplift(daily_sessions: int, baseline_purchase_rate: float, rel_lift: float, aov: float, days: int = 365) -> float:
    """
    rel_lift: relative lift in purchase rate (e.g., 0.25 means +25% relative)
    """
    incremental_purchases_per_day = daily_sessions * baseline_purchase_rate * rel_lift
    return incremental_purchases_per_day * aov * days
