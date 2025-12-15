import numpy as np
import pandas as pd

def generate_ab_test_data(
    n_users=6400,
    control_cr=0.08,       # Baseline purchase conversion rate for Control
    treatment_cr=0.10,     # Purchase conversion rate for Treatment
    seed=42,
    base_aov=75.0          # Baseline AOV (used to calibrate distribution)
):
    """
    Generates synthetic dataset for an e-commerce product page A/B test.

    Columns:
    - user_id
    - experiment_group (A/B)
    - region
    - device_type
    - time_spent_seconds
    - added_to_cart (0/1)
    - purchase (0/1)
    - order_value (float; 0 if purchase=0)
    """
    rng = np.random.default_rng(seed)

    # Assign groups
    groups = rng.choice(['A', 'B'], size=n_users, p=[0.5, 0.5])
    user_ids = np.arange(1, n_users + 1)

    # Region + device
    regions = rng.choice(['North America', 'Europe', 'Asia', 'Other'],
                         size=n_users, p=[0.4, 0.3, 0.2, 0.1])

    devices = rng.choice(['Desktop', 'Mobile', 'Tablet'],
                         size=n_users, p=[0.5, 0.4, 0.1])

    # Time spent (treatment slightly higher)
    time_spent = np.where(
        groups == 'A',
        rng.normal(loc=40, scale=15, size=n_users),
        rng.normal(loc=45, scale=15, size=n_users)
    )
    time_spent = np.clip(time_spent, 0, None).round(2)

    # Funnel: add_to_cart -> purchase
    # Add-to-cart probability is purchase CR + 5pp (simple but realistic)
    add_to_cart = np.zeros(n_users, dtype=int)
    purchase = np.zeros(n_users, dtype=int)

    for i, g in enumerate(groups):
        p_purchase = control_cr if g == 'A' else treatment_cr
        p_atc = min(0.95, p_purchase + 0.05)

        if rng.random() < p_atc:
            add_to_cart[i] = 1
            # Purchase conditional on ATC (ensures purchase <= ATC)
            if rng.random() < (p_purchase / p_atc):
                purchase[i] = 1

    # --- NEW: order_value ---
    # Use lognormal to create right-skew (common for order values)
    # Calibrate so mean is roughly base_aov.
    # For lognormal: mean = exp(mu + sigma^2/2)
    sigma = 0.6
    mu = np.log(base_aov) - (sigma**2) / 2

    # Optional: small multipliers by region/device for realism
    region_multiplier = {
        "North America": 1.05,
        "Europe": 1.00,
        "Asia": 0.95,
        "Other": 0.90
    }
    device_multiplier = {
        "Desktop": 1.02,
        "Mobile": 0.98,
        "Tablet": 1.00
    }

    order_value = np.zeros(n_users, dtype=float)
    purchasers = np.where(purchase == 1)[0]
    if len(purchasers) > 0:
        raw_vals = rng.lognormal(mean=mu, sigma=sigma, size=len(purchasers))

        # Apply multipliers
        for idx, val in zip(purchasers, raw_vals):
            mult = region_multiplier.get(regions[idx], 1.0) * device_multiplier.get(devices[idx], 1.0)
            order_value[idx] = round(val * mult, 2)

    df = pd.DataFrame({
        'user_id': user_ids,
        'experiment_group': groups,
        'region': regions,
        'device_type': devices,
        'time_spent_seconds': time_spent,
        'added_to_cart': add_to_cart,
        'purchase': purchase,
        'order_value': order_value
    })

    return df


# Generate and save
df_ab = generate_ab_test_data(n_users=2000, control_cr=0.08, treatment_cr=0.10, seed=42, base_aov=75.0)
print(df_ab.head())
print("Purchase rate A:", df_ab[df_ab.experiment_group=="A"]["purchase"].mean())
print("Purchase rate B:", df_ab[df_ab.experiment_group=="B"]["purchase"].mean())
print("AOV overall:", df_ab[df_ab.purchase==1]["order_value"].mean())

df_ab.to_csv('synthetic_ab_test_data.csv', index=False)
