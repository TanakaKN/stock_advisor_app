# 📈 Stock Advisor — AI-Assisted Trading Decision App

Stock Advisor is a beginner-friendly web application built with **Python, Django, and Machine Learning** to assist traders in making **BUY / SELL / HOLD** decisions based on historical stock price patterns.

This project focuses on **decision support**, not automated trading.

---

## 🚀 Features

- 📊 Fetches real historical stock price data
- 🧠 Uses a trained LSTM (Long Short-Term Memory) neural network
- 📈 Analyzes recent price trends (last 60 trading days)
- ✅ Provides clear BUY / SELL / HOLD recommendations
- 🕒 Suggests a short-term holding period
- 💬 Explains decisions in plain English
- 🌐 Web-based interface built with Django
- ⚠️ Conservative logic to reduce overtrading

---

## 🧠 How It Works

1. A user enters a stock ticker (e.g. `AAPL`)
2. The app retrieves historical closing prices
3. Data is scaled and transformed into time sequences
4. A pre-trained LSTM model predicts the next price movement
5. The prediction is converted into a trading decision using percentage thresholds
6. Results are displayed with a clear explanation

---

## 📌 Decision Logic

| Predicted Price Change | Recommendation |
|-----------------------|----------------|
| ≥ +2% | BUY |
| ≤ −2% | SELL |
| Between −2% and +2% | HOLD |

This conservative approach helps filter market noise and encourages disciplined trading.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Machine Learning:** TensorFlow (LSTM), NumPy, Scikit-learn
- **Data Source:** Yahoo Finance
- **Frontend:** HTML, CSS
- **Deployment:** PythonAnywhere (planned)

---

## ⚠️ Disclaimer

This application is for **educational and research purposes only**.

It does **not** constitute financial advice, and the author is not responsible for any financial losses incurred from its use. Always combine model insights with personal research and risk management.

---

## 📂 Project Structure

Trading_app/
├── ml/ # Machine learning logic
│ ├── data_loader.py
│ ├── preprocessing.py
│ ├── predictor.py
│ ├── decision_engine.py
│ └── model/
│ ├── trained_model.h5
│ └── scaler.pkl
├── stock_advisor/
│ ├── advisor/
│ ├── settings.py
│ └── urls.py
└── manage.py


## 📈 Future Improvements

- Multi-day forecasting
- Risk scoring and volatility metrics
- Portfolio tracking
- Strategy comparison
- Deployment to production environment

---

## 🙌 Author

Built by **Tanaka Keith Ndopo**  
Focused on learning, discipline, and practical application of machine learning in finance.
