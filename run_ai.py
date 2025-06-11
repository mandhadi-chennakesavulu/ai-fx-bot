"""
Main loop: every minute, pull the latest EUR/USD 1-min candle and print a signal.
"""
import time, datetime
from oanda_api import get_latest_candle
from predictor import predict_signal

def main():
    print("🔁 Real-time AI-FX bot running …")
    while True:
        now = datetime.datetime.utcnow()
        seconds_to_wait = 55 - now.second
        if seconds_to_wait < 0:        # already past :55
            seconds_to_wait += 60
        time.sleep(seconds_to_wait)

        candle = get_latest_candle()
        if candle is None:
            print("⚠️  No candle received.")
            time.sleep(5)
            continue

        signal = predict_signal(candle)
        print(f"[{datetime.datetime.utcnow():%Y-%m-%d %H:%M:%S}] "
              f"O:{candle['o']}  C:{candle['c']}  ⇒  {signal}")

        time.sleep(10)                 # wait past the candle close

if __name__ == "__main__":
    main()
