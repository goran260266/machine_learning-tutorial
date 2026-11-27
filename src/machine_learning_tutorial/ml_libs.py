import numpy as np

def predict_single(features, coefficients, intercept):
    """
    Make a prediction using linear regression.

    Parameters:
    - features: array of feature values
    - coefficients: array of model coefficients
    - intercept: model intercept

    Returns:
    - prediction: single predicted value
    """
    features = np.array(features)
    coefficients = np.array(coefficients)
    return features @ coefficients + intercept