#import requests
#import json

#OANDA_API_KEY = '0ec10b3425bf3c7cd8d5c7bcd9f2d880-576ac8bd3c585ae8cfd018ab15b2c542'
#ACCOUNT_ID = '101-001-35008001-001'
#INSTRUMENT = "EUR_USD"
#OANDA_URL = 'https://api-fxpractice.oanda.com/v3/instruments/EUR_USD/candles'

"""
Minimal OANDA helper – pulls the last 1-minute candle (mid prices).
"""
import os, requests, datetime
from dotenv import load_dotenv

load_dotenv()                                        # reads .env

API_KEY    = os.getenv("OANDA_API_KEY")
ACCOUNT_ID = os.getenv("OANDA_ACCOUNT_ID", "")
ENV        = os.getenv("OANDA_ENV", "practice")      # practice | live
BASE_URL   = "https://api-fxpractice.oanda.com" if ENV=="practice" \
           else "https://api-fxtrade.oanda.com"

PAIR       = "EUR_USD"
ENDPOINT   = f"{BASE_URL}/v3/instruments/{PAIR}/candles"
HEADERS    = {"Authorization": f"Bearer {API_KEY}"}

def get_latest_candle():
    params = {"granularity": "M1", "count": 1, "price": "M"}
    try:
        r = requests.get(ENDPOINT, headers=HEADERS, params=params, timeout=10)
        r.raise_for_status()
        c = r.json()["candles"][0]
        return {
            "time"  : c["time"],
            "o"     : float(c["mid"]["o"]),
            "h"     : float(c["mid"]["h"]),
            "l"     : float(c["mid"]["l"]),
            "c"     : float(c["mid"]["c"]),
            "volume": c["volume"]
        }
    except Exception as e:
        print("🌐 OANDA error:", e)
        return None
