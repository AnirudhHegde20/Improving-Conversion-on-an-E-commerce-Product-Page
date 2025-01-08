import numpy as np
import pandas as pd

def generate_ab_test_data(
    n_users=2000,
    control_cr=0.08,   # Baseline conversion rate for Control
    treatment_cr=0.10, # Conversion rate for Treatment
    seed=42
):
    """
    Generates a synthetic dataset for an e-commerce product page A/B test.
    
    Parameters:
        n_users (int): total number of user sessions.
        control_cr (float): average conversion rate for control group.
        treatment_cr (float): average conversion rate for treatment group.
        seed (int): random seed for reproducibility.
        
    Returns:
        pd.DataFrame: A DataFrame containing the simulated data.
    """
    np.random.seed(seed)
    
    # Assign half of users to Control (A) and half to Treatment (B)
    groups = np.random.choice(['A', 'B'], size=n_users, p=[0.5, 0.5])
    
    # Synthetic user_id
    user_ids = np.arange(1, n_users + 1)
    
    # Simulate region (e.g., North America, Europe, Asia, Others)
    regions = np.random.choice(
        ['North America', 'Europe', 'Asia', 'Other'],
        size=n_users, 
        p=[0.4, 0.3, 0.2, 0.1]
    )
    
    # Simulate device type (Desktop, Mobile, Tablet)
    devices = np.random.choice(
        ['Desktop', 'Mobile', 'Tablet'],
        size=n_users,
        p=[0.5, 0.4, 0.1]
    )
    
    # Time spent on product page in seconds (some distribution)
    # Assuming Treatment might slightly increase time on page.
    time_spent = []
    for g in groups:
        if g == 'A':
            # Control group: average ~ 40 seconds with some noise
            time_spent.append(max(0, np.random.normal(loc=40, scale=15)))
        else:
            # Treatment group: average ~ 45 seconds with some noise
            time_spent.append(max(0, np.random.normal(loc=45, scale=15)))
            
    time_spent = np.array(time_spent).round(2)
    
    # Simulate "Add to Cart" event
    # For Control group: use control_cr for conversion
    # For Treatment group: use treatment_cr
    # Assuming that "conversion" in an e-commerce context is "Purchase" or "Add to Cart".
    # Let's say 'purchase' is the ultimate conversion.
    
    add_to_cart = np.zeros(n_users, dtype=int)
    purchase = np.zeros(n_users, dtype=int)
    
    for i, g in enumerate(groups):
        if g == 'A':
            # Probability of adding to cart might be slightly higher than the final purchase
            add_to_cart_prob = control_cr + 0.05  # e.g., if final CR is 8%, add-to-cart might be 13%
            if np.random.rand() < add_to_cart_prob:
                add_to_cart[i] = 1
                # Then final purchase might happen with some fraction of those who added to cart
                if np.random.rand() < (control_cr / add_to_cart_prob):
                    purchase[i] = 1
        else:
            add_to_cart_prob = treatment_cr + 0.05  # e.g., if final CR is 10%, add-to-cart might be 15%
            if np.random.rand() < add_to_cart_prob:
                add_to_cart[i] = 1
                # Then final purchase might happen with some fraction of those who added to cart
                if np.random.rand() < (treatment_cr / add_to_cart_prob):
                    purchase[i] = 1
    
    data = {
        'user_id': user_ids,
        'experiment_group': groups,
        'region': regions,
        'device_type': devices,
        'time_spent_seconds': time_spent,
        'added_to_cart': add_to_cart,
        'purchase': purchase
    }
    
    df = pd.DataFrame(data)
    return df

# Generate the synthetic data
df_ab = generate_ab_test_data(n_users=2000, control_cr=0.08, treatment_cr=0.10, seed=42)

# Check first few rows
print(df_ab.head())

# Save to CSV
df_ab.to_csv('synthetic_ab_test_data.csv', index=False)