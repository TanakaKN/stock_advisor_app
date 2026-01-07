from data_loader import load_stock_data
from predictor import predict_next_price
from decision_engine import make_decision

ticker = "AAPL"

df = load_stock_data(ticker)
current_price = df["Close"].iloc[-1]
prices = df["Close"].values

predicted_price = predict_next_price(prices)

result = make_decision(
    ticker=ticker,
    current_price=current_price,
    predicted_price=predicted_price
)

print(result)
