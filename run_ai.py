import time
from datetime import datetime
from oanda_api import get_latest_candle
from predictor import predict_signal

def main():
    print("🔁 Real-time AI FX bot running...\n")
    while True:
        now = datetime.utcnow()
        if now.second == 55:  # 5 seconds before minute ends
            candle = get_latest_candle()
            if candle:
                signal = predict_signal(candle)
                print(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] Signal: {signal}  (EUR/USD)")
            time.sleep(10)  # wait past the minute
        else:
            time.sleep(1)

if __name__ == "__main__":
    main()