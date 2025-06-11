"""
VERY simple rule-based signal.
Replace this with ML or FVG/ICT/SMC logic later.
"""

def predict_signal(candle):
    open_p  = candle["o"]
    close_p = candle["c"]

    if close_p > open_p + 0.0002:
        return "BUY"
    elif close_p < open_p - 0.0002:
        return "SELL"
    else:
        return "HOLD"
