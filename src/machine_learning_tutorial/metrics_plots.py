"""Helper plots for the "classification metrics" deck.

The plotting code lives here so the slides stay clean (a one-line call per
picture). In the visualization week we open this box and rebuild the plot by
hand. Everything is offline and deterministic so the notebook is reproducible.
Adapted/simplified from module_540_ml_basics for AZAV.
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import precision_recall_curve


def plot_pr_vs_threshold(model, x_test, y_test, positive_label="malignant"):
    """Show precision and recall as the decision threshold moves from 0 to 1.

    `model` must support `predict_proba`; the positive class is column 1.
    `positive_label` names the positive class in the x-axis label.
    """
    scores = model.predict_proba(x_test)[:, 1]
    precision, recall, thresholds = precision_recall_curve(y_test, scores)
    # precision/recall carry one extra entry (threshold = +inf) — drop it.
    plt.figure()
    plt.plot(thresholds, precision[:-1], label="precision")
    plt.plot(thresholds, recall[:-1], label="recall")
    plt.xlabel(f"decision threshold (how sure before we say '{positive_label}')")
    plt.ylabel("score")
    plt.ylim(0, 1.05)
    plt.legend()
    plt.title("Lower the threshold: recall up, precision down")

def plot_f1_vs_threshold(model, x_test, y_test, positive_label="malignant"):
    """Show F1 score as the decision threshold moves from 0 to 1.

    `model` must support `predict_proba`; the positive class is column 1.
    `positive_label` names the positive class in the x-axis label.
    """
    scores = model.predict_proba(x_test)[:, 1]
    precision, recall, thresholds = precision_recall_curve(y_test, scores)
    denominator = precision + recall
    f1_scores = np.divide(
        2 * precision * recall,
        denominator,
        out=np.zeros_like(denominator),
        where=denominator > 0,
    )
    # precision/recall carry one extra entry (threshold = +inf) — drop it.
    plt.figure()
    plt.plot(thresholds, f1_scores[:-1], label="F1 score")
    plt.xlabel(f"decision threshold (how sure before we say '{positive_label}')")
    plt.ylabel("f1 score")
    plt.ylim(0, 1.05)
    plt.legend()
    plt.title("F1 score peaks where precision and recall are balanced")
