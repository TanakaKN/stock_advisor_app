from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ml.data_loader import load_stock_data
from ml.predictor import predict_next_price
from ml.decision_engine import make_decision


@csrf_exempt
def analyze_stock(request):
    """
    Display form on GET, analyze stock on POST.
    """

    # ✅ GET → show empty form
    if request.method == "GET":
        return render(request, "analyze.html")

    # ✅ POST → run analysis
    if request.method == "POST":
        ticker = request.POST.get("ticker", "").upper().strip()

        if not ticker:
            return render(
                request,
                "analyze.html",
                {"error": "Ticker symbol is required."}
            )

        try:
            df = load_stock_data(ticker)

            current_price = float(df["Close"].iloc[-1])
            prices = df["Close"].values

            predicted_price = predict_next_price(prices)

            result = make_decision(
                ticker=ticker,
                current_price=current_price,
                predicted_price=predicted_price
            )

            return render(request, "analyze.html", result)

        except Exception as e:
            return render(
                request,
                "analyze.html",
                {"error": str(e)}
            )

    # ❌ Any other method
    return JsonResponse(
        {"error": "Method not allowed"},
        status=405
    )
