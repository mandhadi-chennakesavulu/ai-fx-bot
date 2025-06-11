import random

def predict_signal(candle):
    # 🔁 Basic mock AI signal logic based on candle close and open difference
    diff = candle['close'] - candle['open']
    if diff > 0.0003:
        return "BUY"
    elif diff < -0.0003:
        return "SELL"
    else:
        return "HOLD"

# This will be replaced with full ML logic with FVG, ICT, SMC, etc.