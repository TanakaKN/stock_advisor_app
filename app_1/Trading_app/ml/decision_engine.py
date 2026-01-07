def make_decision(
    ticker: str,
    current_price,
    predicted_price
) -> dict:
    
    """
    Convert prediction into a trading decision.
    """

    # ✅ FORCE pure Python floats (CRITICAL FIX)
    current_price = float(current_price)
    predicted_price = float(predicted_price)

    percent_change = (
        predicted_price - current_price
    ) / current_price

    percent_change_pct = percent_change * 100

    if percent_change_pct >= 2:
        recommendation = "BUY"
        confidence = "Moderate"
        explanation = (
            f"The model expects {ticker} to rise by about "
            f"{percent_change_pct:.2f}% in the near term, "
            "suggesting a short-term buying opportunity."
        )

    elif percent_change_pct <= -2:
        recommendation = "SELL"
        confidence = "Moderate"
        explanation = (
            f"The model expects {ticker} to decline by about "
            f"{abs(percent_change_pct):.2f}% in the near term, "
            "suggesting a short-term selling opportunity."
        )

    else:
        recommendation = "HOLD"
        confidence = "Low"
        explanation = (
            f"The model predicts limited price movement "
            f"({percent_change_pct:.2f}%), indicating uncertainty. "
            "Holding may be safer at this time."
        )

    return {
        "ticker": ticker,
        "current_price": round(current_price, 2),
        "predicted_price": round(predicted_price, 2),
        "recommendation": recommendation,
        "confidence": confidence,
        "holding_period": "Short-term (5-10 trading days)",
        "explanation": explanation
    }
