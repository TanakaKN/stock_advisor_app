import numpy as np
import joblib
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import EarlyStopping

from data_loader import load_stock_data


# -----------------------------
# CONFIGURATION
# -----------------------------
TICKER = "AAPL"          # base stock to train on
WINDOW_SIZE = 60
EPOCHS = 20
BATCH_SIZE = 32


# -----------------------------
# LOAD DATA
# -----------------------------
df = load_stock_data(TICKER)
prices = df["Close"].values.reshape(-1, 1)


# -----------------------------
# SCALE DATA
# -----------------------------
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_prices = scaler.fit_transform(prices)


# -----------------------------
# CREATE SEQUENCES
# -----------------------------
X, y = [], []

for i in range(WINDOW_SIZE, len(scaled_prices)):
    X.append(scaled_prices[i - WINDOW_SIZE:i, 0])
    y.append(scaled_prices[i, 0])

X = np.array(X)
y = np.array(y)

# reshape for LSTM: (samples, time steps, features)
X = np.reshape(X, (X.shape[0], X.shape[1], 1))


# -----------------------------
# BUILD MODEL
# -----------------------------
model = Sequential()
model.add(LSTM(50, return_sequences=False, input_shape=(WINDOW_SIZE, 1)))
model.add(Dense(1))

model.compile(
    optimizer="adam",
    loss="mean_squared_error"
)


# -----------------------------
# TRAIN MODEL
# -----------------------------
early_stop = EarlyStopping(
    monitor="loss",
    patience=5,
    restore_best_weights=True
)

model.fit(
    X,
    y,
    epochs=EPOCHS,
    batch_size=BATCH_SIZE,
    callbacks=[early_stop],
    verbose=1
)


# -----------------------------
# SAVE ARTIFACTS
# -----------------------------
model.save("model/trained_model.h5")
joblib.dump(scaler, "model/scaler.pkl")

print("✅ Training complete.")
print("📦 Files saved:")
print("- model/trained_model.h5")
print("- model/scaler.pkl")
