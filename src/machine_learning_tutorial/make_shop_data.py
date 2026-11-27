"""Generate the example shop dataset shipped with this topic.

Run from this directory to (re)create ``shop_customers.csv`` and
``shop_customers.xlsx``::

    python make_shop_data.py

Deterministic (fixed seed) so the committed files are reproducible. The slide
deck ``slides_010_dataframes_and_loading`` generates this same table once (using
the identical snippet below), saves it, and then loads it back — so the file it
writes must equal the committed file. The later 470 decks load it fresh.
Requires ``openpyxl`` for the ``.xlsx`` write.
"""

import numpy as np
import pandas as pd


def make_shop_customers(n: int = 200, seed: int = 42) -> pd.DataFrame:
    """A small synthetic online-shop customer table (one row per customer).

    ``income`` is lognormal (right-skewed, realistic) — the headline
    mean-vs-median / skew example. ``age`` is ~uniform (roughly symmetric) — the
    contrast case. ``spend`` is drawn LAST so adding ``income`` above does not
    shift the earlier columns' random draws.
    """
    rng = np.random.default_rng(seed)
    df = pd.DataFrame(
        {
            "customer_id": np.arange(1, n + 1),
            "age": rng.integers(18, 70, n),
            "region": rng.choice(["North", "South", "East", "West"], n),
            "income": rng.lognormal(mean=8.0, sigma=0.4, size=n).round(0),
            "purchases": rng.integers(0, 25, n),
        }
    )
    df["spend"] = (df["purchases"] * rng.normal(40, 8, n)).round(2).clip(lower=0)
    return df


if __name__ == "__main__":
    customers = make_shop_customers()
    customers.to_csv("shop_customers.csv", index=False)
    customers.to_excel("shop_customers.xlsx", index=False)
    print(customers.head())
    print(f"\nWrote shop_customers.csv and shop_customers.xlsx ({len(customers)} rows).")
