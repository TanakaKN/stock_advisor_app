import os
import numpy as np
import joblib
from tensorflow.keras.models import load_model

from ml.preprocessing import prepare_input_sequence

# -----------------------------
# PATH SETUP (ABSOLUTE & SAFE)
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "trained_model.h5")
SCALER_PATH = os.path.join(BASE_DIR, "model", "scaler.pkl")


def predict_next_price(close_prices):
    """
    Predict the next closing price using the trained LSTM model.

    Args:
        close_prices (array-like): Historical closing prices

    Returns:
        float: Predicted next price (original scale)
    """

    # Convert to numpy array
    close_prices = np.array(close_prices)

    # Prepare model input
    X = prepare_input_sequence(close_prices)

    # Load model and scaler
    model = load_model(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    # Predict (scaled)
    scaled_prediction = model.predict(X, verbose=0)

    # Convert back to real price
    prediction = scaler.inverse_transform(scaled_prediction)

    return float(prediction[0][0])
