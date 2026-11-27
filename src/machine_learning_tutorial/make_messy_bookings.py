"""Generate the deliberately messy studio-bookings dataset shipped with this topic.

Run from this directory to (re)create ``studio_bookings_messy.csv``::

    python make_messy_bookings.py

Deterministic (fixed seed) so the committed file is reproducible. Unlike
``shop_customers.csv`` (topic_0620), this file is **not** rebuilt inside the
slide deck — the workshop's whole point is loading a file and *discovering*
that it is messy, so the deck only ever ``read_csv``\\s the committed file.

The planted problems (the workshop hunts these down):

- ``booking_date`` mixes two formats: ``2026-03-14`` and ``2026/03/14`` (two
  export tools, two separators — both year-first, so parsing stays unambiguous;
  ``pd.to_datetime`` needs ``format="mixed"`` to accept the mix)
- ``price`` contains ``"?"`` markers, so a naive load reads it as **text**
  (``"?"`` is not in pandas' default missing-value markers — ``na_values`` fixes it)
- ``class_type`` contains ``"unknown"`` markers plus a few genuinely empty cells
- four exact **duplicate rows** (the same booking exported twice)
- one unrealistic **outlier**: a single booking with ``qty`` = 500
- a terse column name ``qty`` that wants a ``rename`` to ``quantity``
"""

import numpy as np
import pandas as pd

CLASS_TYPES = ["Yoga", "Spin", "Boxing", "Pilates"]
STUDIOS = ["Downtown", "Harbor", "Uptown", "Airport"]


def make_messy_bookings(n: int = 196, seed: int = 42) -> pd.DataFrame:
    """A small synthetic booking table (one row per booking) with planted problems."""
    rng = np.random.default_rng(seed)
    dates = pd.Timestamp("2026-03-02") + pd.to_timedelta(
        rng.integers(0, 90, n), unit="D"
    )
    df = pd.DataFrame(
        {
            "booking_id": np.arange(1001, 1001 + n),
            "booking_date": dates,
            "studio": rng.choice(STUDIOS, n),
            "class_type": rng.choice(CLASS_TYPES, n),
            "price": rng.gamma(shape=4.0, scale=15.0, size=n).round(2).clip(min=5.0),
            "qty": rng.integers(1, 9, n),
        }
    )

    # Mixed date formats: ~30% slashed yyyy/mm/dd, the rest ISO yyyy-mm-dd.
    # Both are year-first (unambiguous) — dd.mm.yyyy would be silently
    # mis-parsed by pandas' mixed-format inference for days <= 12.
    slashed = rng.random(n) < 0.3
    df["booking_date"] = np.where(
        slashed,
        df["booking_date"].dt.strftime("%Y/%m/%d"),
        df["booking_date"].dt.strftime("%Y-%m-%d"),
    )

    # Missing-value markers: "?" in price (not a default NA marker → the column
    # loads as text), "unknown" plus real empty cells in class_type. The price
    # column is formatted as text first — in the CSV it is text anyway.
    df["price"] = df["price"].map(lambda v: f"{v:.2f}")
    df.loc[rng.choice(n, 6, replace=False), "price"] = "?"
    df.loc[rng.choice(n, 5, replace=False), "class_type"] = "unknown"
    df.loc[rng.choice(n, 3, replace=False), "class_type"] = ""

    # One unrealistic outlier (a typo when the booking was entered).
    df.loc[rng.integers(0, n), "qty"] = 500

    # Four exact duplicates: the same booking exported twice.
    dup_rows = df.iloc[rng.choice(n, 4, replace=False)]
    df = pd.concat([df, dup_rows], ignore_index=True)

    # Shuffle so the duplicates don't sit at the end, then keep a stable look.
    df = df.sample(frac=1.0, random_state=seed).reset_index(drop=True)
    return df


if __name__ == "__main__":
    bookings = make_messy_bookings()
    bookings.to_csv("studio_bookings_messy.csv", index=False)
    print(bookings.head())
    print(f"\nWrote studio_bookings_messy.csv ({len(bookings)} rows).")
