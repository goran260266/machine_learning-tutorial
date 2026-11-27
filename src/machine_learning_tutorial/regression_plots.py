"""Helper plots for the regression / train-test-split deck.

The plotting code lives here so the slides stay clean (one short call per
picture). In the visualization week we open this box and rebuild the plots by
hand. All data is synthetic/offline so the notebook is reproducible.
Adapted/simplified from module_540_ml_basics for AZAV.
"""

import numpy as np
import matplotlib.pyplot as plt

_rng = np.random.default_rng(0)
# A noisy but clearly linear relationship: more study hours → higher score.
_x = np.sort(_rng.uniform(0, 10, 40))
_y = 5 * _x + 40 + _rng.normal(0, 8, _x.size)


def show_line_fit():
    """A straight-line model fitted to a noisy linear relationship."""
    line = np.poly1d(np.polyfit(_x, _y, 1))
    grid = np.linspace(0, 10, 100)
    plt.figure()
    plt.scatter(_x, _y, label="data we observe")
    plt.plot(grid, line(grid), "r-", label="the model (a straight line)")
    plt.xlabel("hours studied")
    plt.ylabel("exam score")
    plt.legend()
    plt.title("A regression model predicts a number")


def plot_predicted_vs_actual(model, x_test, y_test):
    """Scatter predicted against actual values; closer to the line is better."""
    preds = model.predict(x_test)
    lo = float(min(np.min(y_test), preds.min()))
    hi = float(max(np.max(y_test), preds.max()))
    plt.figure()
    plt.scatter(y_test, preds, alpha=0.6)
    plt.plot([lo, hi], [lo, hi], "g--", label="perfect prediction")
    plt.xlabel("actual value")
    plt.ylabel("predicted value")
    plt.legend()
    plt.title("Predicted vs actual (closer to the line = better)")
