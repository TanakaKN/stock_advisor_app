import os
import numpy as np
import joblib

# -----------------------------
# CONFIGURATION
# -----------------------------
WINDOW_SIZE = 60

# -----------------------------
# PATH SETUP (ABSOLUTE & SAFE)
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCALER_PATH = os.path.join(BASE_DIR, "model", "scaler.pkl")


def prepare_input_sequence(prices):
    """
    Prepare the last WINDOW_SIZE values for LSTM prediction.

    Args:
        prices (array-like): Historical closing prices

    Returns:
        np.ndarray: Scaled input shaped (1, WINDOW_SIZE, 1)
    """

    if len(prices) < WINDOW_SIZE:
        raise ValueError(
            f"At least {WINDOW_SIZE} data points are required."
        )

    # Ensure numpy array
    prices = np.array(prices).reshape(-1, 1)

    # Load scaler (trained earlier)
    scaler = joblib.load(SCALER_PATH)

    # Scale prices
    scaled_prices = scaler.transform(prices)

    # Take last WINDOW_SIZE points
    last_sequence = scaled_prices[-WINDOW_SIZE:]

    # Reshape for LSTM
    X = np.reshape(last_sequence, (1, WINDOW_SIZE, 1))

    return X
