"""Black-box plotting helpers for the Week-12 pandas decks.

This file ships in both ``topic_0620_exploratory_analysis/`` and
``topic_0650_workshop_data_analysis/`` (assets ship per topic folder). Keep the
two copies **byte-identical**: the build merges same-named files into one output
folder and only dedupes identical content — any difference makes the shipped
file race-dependent and emits conflicting-write warnings.

The decks use these as a black box (``import distribution_plots as dp``) so the
focus stays on *reading* a distribution — shape, skew, mean vs median — not on
the plotting mechanics. The matplotlib details are revealed in the Week-13
"how those plots were made" deck, which rebuilds this exact source by hand.

Labels are kept English ("Mean"/"Median") on purpose: this helper is shared
across the German and English split decks, matching the keep-English-terms
convention.
"""

import matplotlib.pyplot as plt


def plot_distribution(values, bins=15, title=None):
    """Histogram of ``values`` with the mean (dashed) and median (solid) marked.

    Returns the matplotlib ``Axes`` so a notebook renders the figure.
    """
    fig, ax = plt.subplots()
    ax.hist(values, bins=bins)
    ax.axvline(values.mean(), color="C1", linestyle="--", label="Mean")
    ax.axvline(values.median(), color="C2", linestyle="-", label="Median")
    if title:
        ax.set_title(title)
    ax.legend()
    return ax
