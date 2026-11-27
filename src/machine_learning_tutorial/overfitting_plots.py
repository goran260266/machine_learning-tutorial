"""Helper plots for the bias-variance / under- and overfitting deck.

The plotting code lives here so the slides stay clean (one short call per
picture). In the visualization week we open this box and rebuild the plots by
hand. All data is synthetic and offline so the notebook is reproducible.
Adapted/simplified from module_540_ml_basics for AZAV. "Complexity" is the
degree of a fitted polynomial — a simple, visual stand-in for model flexibility.
"""

import warnings

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

_DEFAULT_NOISE = 0.25


def _true(x):
    """The hidden pattern the model is trying to learn."""
    return np.sin(2 * np.pi * x)


def _make(noise, seed, n):
    """A noisy sample of the true pattern (own RNG per seed → reproducible)."""
    rng = np.random.default_rng(seed)
    x = np.sort(rng.uniform(0, 1, n))
    y = _true(x) + rng.normal(0, noise, n)
    return x, y


# A small training set and a larger, separate test set from the same pattern.
_x, _y = _make(_DEFAULT_NOISE, seed=0, n=15)
_x_test, _y_test = _make(_DEFAULT_NOISE, seed=1, n=40)


def _fit(x, y, complexity):
    with warnings.catch_warnings():  # high-degree fits are ill-conditioned by design
        warnings.simplefilter("ignore")
        return np.poly1d(np.polyfit(x, y, complexity))


def _mse(model, x, y):
    return float(np.mean((model(x) - y) ** 2))


def _scatter_test(ax=None):
    """Scatter the held-out test points (orange squares) on the current/given axes."""
    scatter = ax.scatter if ax is not None else plt.scatter
    scatter(_x_test, _y_test, marker="s", color="orange", label="test data (held out)")


def show_data(show_test=False):
    """Scatter of the noisy data together with the true underlying pattern.

    Pass ``show_test=True`` to also show the held-out test points.
    """
    grid = np.linspace(0, 1, 200)
    plt.figure()
    plt.scatter(_x, _y, label="data we observe")
    if show_test:
        _scatter_test()
    plt.plot(grid, _true(grid), "g--", label="true pattern (unknown)")
    plt.ylim(-2, 2)
    plt.legend()
    plt.title("Noisy data around a true pattern")


def show_signal_and_noise():
    """Signal, noise, and the observed data, side by side.

    Left: the true pattern alone (signal). Middle: what the data adds on top
    of it (noise). Right: what we actually observe — signal + noise.
    """
    grid = np.linspace(0, 1, 200)
    noise = _y - _true(_x)
    fig, (ax_signal, ax_noise, ax_data) = plt.subplots(
        1, 3, figsize=(12, 4), sharey=False
    )
    ax_signal.plot(grid, _true(grid), "g-")
    ax_signal.set_ylim(-2, 2)
    ax_signal.set_title("signal: the true pattern")
    ax_noise.scatter(_x, noise, s=20)
    ax_noise.axhline(0, color="gray", linewidth=1)
    ax_noise.set_ylim(-2, 2)  # same scale as the other panels for an honest comparison
    ax_noise.set_title("noise: random variation")
    ax_data.scatter(_x, _y, s=20, label="data we observe")
    ax_data.plot(grid, _true(grid), "g--", label="true pattern (unknown)")
    ax_data.set_ylim(-2, 2)
    ax_data.legend()
    ax_data.set_title("observed: signal + noise")
    fig.tight_layout()


def show_fit(complexity, show_test=False):
    """Fit a model of the given complexity; plot it with train/test error.

    Pass ``show_test=True`` to also scatter the held-out test points the test
    error is computed on.
    """
    grid = np.linspace(0, 1, 200)
    model = _fit(_x, _y, complexity)
    plt.figure()
    plt.scatter(_x, _y, label="training data")
    if show_test:
        _scatter_test()
    plt.plot(grid, _true(grid), "g--", label="true pattern")
    plt.plot(grid, model(grid), "r-", label=f"model (complexity {complexity})")
    plt.ylim(-2, 2)
    plt.legend()
    plt.title(
        f"complexity {complexity}  |  "
        f"train error {_mse(model, _x, _y):.2f}, "
        f"test error {_mse(model, _x_test, _y_test):.2f}"
    )


def show_multiple_fits(complexities, show_test=False):
    """Fit several complexities; show them in a grid like ``show_fit``.

    Layout: two columns for up to four complexities, three columns beyond
    that, with as many rows as needed. Each panel shows the training data,
    the true pattern, the fitted model, and its train/test error. Pass
    ``show_test=True`` to also scatter the held-out test points in each panel.
    """
    grid = np.linspace(0, 1, 200)
    complexities = list(complexities)
    n_cols = 2 if len(complexities) <= 4 else 3
    n_rows = -(-len(complexities) // n_cols)  # ceiling division
    fig, axes = plt.subplots(
        n_rows,
        n_cols,
        figsize=(4.5 * n_cols, 3.5 * n_rows),
        sharex=True,
        sharey=True,
        squeeze=False,
    )
    for ax, complexity in zip(axes.flat, complexities):
        model = _fit(_x, _y, complexity)
        ax.scatter(_x, _y, s=15, label="training data")
        if show_test:
            _scatter_test(ax)
        ax.plot(grid, _true(grid), "g--", label="true pattern")
        ax.plot(grid, model(grid), "r-", label=f"model (complexity {complexity})")
        ax.set_ylim(-2, 2)
        ax.legend(fontsize="small")
        ax.set_title(
            f"complexity {complexity}  |  "
            f"train {_mse(model, _x, _y):.2f}, "
            f"test {_mse(model, _x_test, _y_test):.2f}"
        )
    for ax in axes.flat[len(complexities) :]:  # hide unused panels
        ax.set_visible(False)
    fig.tight_layout()


def show_generated_data(x, y):
    """Like ``show_data``, but for data the students generated themselves."""
    grid = np.linspace(0, 1, 200)
    plt.figure()
    plt.scatter(x, y, label="data we observe")
    plt.plot(grid, _true(grid), "g--", label="true pattern (unknown)")
    plt.ylim(-2, 2)
    plt.legend()
    plt.title("Noisy data around a true pattern")


def show_generated_fit(x, y, model, x_test=None, y_test=None):
    """Like ``show_fit``, but for the students' own data and trained model.

    ``model`` is anything that predicts a target from inputs — a fitted
    scikit-learn estimator (uses ``predict``) or a plain callable. The plot
    shows the training data, the true pattern, and the model's predictions,
    with the training error in the title. Pass ``x_test``/``y_test`` to also
    show held-out test points (different marker) and the test error.
    """
    grid = np.linspace(0, 1, 200)
    predict = model.predict if hasattr(model, "predict") else model

    def predict_1d(inputs):
        inputs = np.asarray(inputs)
        try:
            return predict(inputs)
        except (ValueError, IndexError):  # e.g. sklearn's 2D input contract
            return predict(inputs.reshape(-1, 1))

    predictions = np.asarray(predict_1d(grid), dtype=float)
    train_error = np.mean((predict_1d(x) - np.asarray(y)) ** 2)
    plt.figure()
    plt.scatter(x, y, label="training data")
    if x_test is not None and y_test is not None:
        plt.scatter(
            x_test, y_test, marker="s", color="orange", label="test data (held out)"
        )
    plt.plot(grid, _true(grid), "g--", label="true pattern")
    plt.plot(grid, predictions, "r-", label="your model")
    plt.ylim(-2, 2)
    plt.legend()
    title = f"train error {train_error:.2f}"
    if x_test is not None and y_test is not None:
        test_error = np.mean((predict_1d(x_test) - np.asarray(y_test)) ** 2)
        title += f", test error {test_error:.2f}"
    plt.title(title)


def error_table(complexities=(1, 2, 3, 4, 5, 6, 9)):
    """Train vs test error for several complexities (surfaces the numbers)."""
    rows = []
    for c in complexities:
        model = _fit(_x, _y, c)
        rows.append(
            {
                "complexity": c,
                "train_error": round(_mse(model, _x, _y), 3),
                "test_error": round(_mse(model, _x_test, _y_test), 3),
            }
        )
    return pd.DataFrame(rows)


def plot_error_vs_complexity(max_complexity=9):
    """The bias-variance picture: train error falls, test error is U-shaped."""
    degrees = list(range(1, max_complexity + 1))
    train = [_mse(_fit(_x, _y, c), _x, _y) for c in degrees]
    test = [_mse(_fit(_x, _y, c), _x_test, _y_test) for c in degrees]
    plt.figure()
    plt.plot(degrees, train, "o-", label="training error")
    plt.plot(degrees, test, "o-", label="test error")
    plt.xlabel("model complexity")
    plt.ylabel("error (lower is better)")
    plt.ylim(0, 0.6)  # clip: the most complex models shoot off the top
    plt.legend()
    plt.title("Underfit (left) → sweet spot (middle) → overfit (right)")


def plot_noise_grid(
    seed=10,
    noises=[("low noise", 0.01), ("medium noise", 0.2), ("high noise", 0.9)],
    complexities=[("simple model", 1), ("flexible model", 11)],
):
    """How a simple vs a flexible model react to more and more noise.

    Rows: low / medium / high noise. Columns: a simple model (complexity 1)
    and a flexible model (complexity 11). As noise grows, the flexible model
    chases it more and more; the simple model ignores it (and stays wrong).
    """
    grid = np.linspace(0, 1, 200)

    fig, axes = plt.subplots(3, 2, figsize=(9, 9), sharex=True, sharey=True)
    for r, (noise_label, noise) in enumerate(noises):
        x, y = _make(noise, seed=seed + r, n=15)
        for c, (model_label, complexity) in enumerate(complexities):
            ax = axes[r][c]
            model = _fit(x, y, complexity)
            ax.scatter(x, y, s=15)
            ax.plot(grid, _true(grid), "g--")
            ax.plot(grid, model(grid), "r-")
            ax.set_ylim(-2.5, 2.5)
            if r == 0:
                ax.set_title(model_label)
            if c == 0:
                ax.set_ylabel(noise_label)
    fig.suptitle(
        "More noise → the flexible model chases it; the simple one ignores the pattern"
    )
    fig.tight_layout()
